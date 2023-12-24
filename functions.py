import io
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import pd_info
import text


def my_plot(df_period, parameter):
    plt.figure(figsize=(10, 5))
    for p in range(parameter):
        plt.plot(df_period['time'], df_period[df_period.columns[p + 1]], label=df_period.columns[p + 1])
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Graph of columns')
    plt.legend()
    plt.savefig('plot_image.jpg')
    return "Ваш график:"


def function(query, file_name, parameter, time_period):
    df = pd.read_csv(text.URL + file_name)
    columns = df.columns
    parameter = list(set([x for x in parameter if x < len(columns)]))
    if len(parameter) == 0:
        if query == text.GET_INFO_FUNCTION:
            pd_info.get_info(df)
        else:
            return text.QUERY_ERROR

    time_period[0] = datetime.strptime(time_period[0], '%H:%M')
    df[columns[0]] = pd.to_datetime(df[columns[0]], format='%H:%M')
    mas = [columns[0]] + [columns[i] for i in parameter]
    df = df[mas]
    if len(time_period) == 2:
        time_period[1] = datetime.strptime(time_period[1], '%H:%M')
        if time_period[0] > time_period[1]:
            time_period[0], time_period[1] = time_period[1], time_period[0]
        df_period = df[(df[columns[0]] >= time_period[0]) & (df[columns[0]] <= time_period[1])]
        if query == text.MIN_FUNCTION:
            df_period = df_period.drop(columns=['time'])
            return dict(zip([columns[i] for i in parameter], [x for x in df_period.min()]))
        elif query == text.MAX_FUNCTION:
            df_period = df_period.drop(columns=['time'])
            return dict(zip([columns[i] for i in parameter], [x for x in df_period.max()]))
        elif query == text.PLOT_FUNCTION:
            return my_plot(df_period, len(parameter))
        elif query == text.MEAN_FUNCTION:
            df_period = df_period.drop(columns=['time'])
            return dict(zip([columns[i] for i in parameter], [x for x in df_period.mean()]))
        elif query == text.DEVIATION_FUNCTION:
            df_period = df_period.drop(columns=['time'])
            return dict(zip([columns[i] for i in parameter], [x for x in df_period.std()]))
        elif query == text.VARIANCE_FUNCTION:
            df_period = df_period.drop(columns=['time'])
            return dict(zip([columns[i] for i in parameter], [x for x in df_period.var()]))
        elif query == text.MEDIAN_FUNCTION:
            df_period = df_period.drop(columns=['time'])
            return dict(zip([columns[i] for i in parameter], [x for x in df_period.median()]))
    elif len(time_period) == 1:
        df_period = df[df[columns[0]] == time_period[0]]
        df_period = df_period.drop(columns=['time'])
        return dict(zip([columns[i] for i in parameter], [x for x in df_period.iloc[0]]))
    else:
        return text.QUERY_ERROR

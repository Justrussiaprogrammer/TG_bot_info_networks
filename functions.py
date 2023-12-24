import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import text


def my_plot(df_period, parameter):
    plt.figure(figsize=(10, 5))
    for p in range(parameter):
        plt.plot(df_period['time'], df_period[df_period.columns[p+1]], label=df_period.columns[p+1])
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Graph of columns')
    n = len(df_period)
    step = n // 10
    plt.xticks(range(0, n, step))
    plt.legend()
    plt.savefig('plot_image.jpg')
    plt.show()


def function(query, file_name, parameter, time_period):
    df = pd.read_csv(text.URL + file_name)
    columns = df.columns
    parameter = list(set([x for x in parameter if x < len(columns)]))
    if len(parameter) == 0:
        return 'Invalid query, try again :)'

    time_period[0] = datetime.strptime(time_period[0], '%H:%M')
    df[columns[0]] = pd.to_datetime(df[columns[0]], format='%H:%M')
    mas = [columns[0]] + [columns[i] for i in parameter]
    df = df[mas]
    if len(time_period) == 2:
        time_period[1] = datetime.strptime(time_period[1], '%H:%M')
        if time_period[0] > time_period[1]:
            time_period[0], time_period[1] = time_period[1], time_period[0]
        df_period = df[(df[columns[0]] >= time_period[0]) & (df[columns[0]] <= time_period[1])]
        df_period = df_period.drop(columns=['time'])
        if query == 'min':
            return dict(zip([columns[i] for i in parameter], [x for x in df_period.min()]))
        elif query == 'max':
            return dict(zip([columns[i] for i in parameter], [x for x in df_period.max()]))
        elif query == 'plot':
            return my_plot(df_period, parameter)
        elif query == 'mean':
            return dict(zip([columns[i] for i in parameter], [x for x in df_period.mean()]))
        elif query == 'standard deviation':
            return dict(zip([columns[i] for i in parameter], [x for x in df_period.std()]))
        elif query == 'variance':
            return dict(zip([columns[i] for i in parameter], [x for x in df_period.var()]))
    elif len(time_period) == 1:
        df_period = df[df[columns[0]] == time_period[0]]
        df_period = df_period.drop(columns=['time'])
        return dict(zip([columns[i] for i in parameter], [x for x in df_period]))
    else:
        return 'Invalid query, try again :)'

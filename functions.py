import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import text


def my_plot(df_period, parameter):
    for p in parameter:
        plt.plot(df_period.index, df_period[p], label=p)
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Graph of columns')
    plt.legend()
    plt.savefig('plot_image.jpg')
    plt.show()


def function(query, file_name, parameter, time_period):
    df = pd.read_csv(text.URL + file_name)
    time_period[0] = datetime.strptime(time_period[0], '%H:%M')
    df[df.columns[0]] = pd.to_datetime(df[df.columns[0]], format='%H:%M')
    mas = [df.columns[0]] + [df.columns[i] for i in parameter]
    df = df[mas]
    if len(time_period) == 2:
        time_period[1] = datetime.strptime(time_period[1], '%H:%M')
        if time_period[0] > time_period[1]:
            time_period[0], time_period[1] = time_period[1], time_period[0]
        df_period = df[(df[df.columns[0]] >= time_period[0]) & (df[df.columns[0]] <= time_period[1])]
        if query == 'min':
            d = {}
            df_period = df_period.drop(columns=['time'])
            ans = [x for x in df_period.min()]
            for i in parameter:
                d[df.columns[i]] = ans[i - 1]
            return d
        elif query == 'max':
            d = {}
            df_period.drop([df_period.columns[0]], axis=1)
            ans = [x for x in df_period.max()]
            for i in parameter:
                d[df.columns[i]] = ans[i - 1]
            return d
        elif query == 'plot':
            my_plot(df_period, parameter)
    elif len(time_period) == 1:
        df_2 = df[df[df.columns[0]] == time_period[0]]
        d = {}
        for i in df_2.columns:
            d[i] = df_2.loc[0, i]
        return d
    else:
        return 'Invalid query, try again :)'

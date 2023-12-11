import text
import datetime
import pandas as pd


def function(query, file_name, parameter, time_period):
    df = pd.read_csv(text.URL + file_name)
    time_period[0] = datetime.datetime.strptime(time_period[0], '%H%M')
    df[df.columns[0]] = pd.to_datetime(df[df.columns[0]], format='%H%M')
    if len(time_period) == 2:
        time_period[1] = datetime.datetime.strptime(time_period[1], '%H%M')
        if time_period[0] > time_period[1]:
            time_period[0], time_period[1] = time_period[1], time_period[0]
        df_period = df[(df.index >= time_period[0]) & (df.index <= time_period[1])]
        if query == 'min':
            return my_min(df_period, parameter)
        elif query == 'max':
            return my_max(df_period, parameter)
        elif query == 'plot':
            return my_plot(df_period)
        else:
            return 'Invalid query, try again :)'
    elif len(time_period == 1):
        return my_value(df, time_period, parameter)
    else:
        return 'Invalid query, try again :)'


def my_min(df_period, parameter):
    min_values = df_period.max()
    min_values = [min_values[i] for i in parameter]
    return min_values


def my_max(df_period, parameter):
    max_values = df_period.max()
    max_values = [max_values[i] for i in parameter]
    return max_values


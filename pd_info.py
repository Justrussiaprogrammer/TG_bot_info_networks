import pandas as pd
import text


class PdInf:
    def __init__(self, df):
        self.df = df

    def display_info(self):
        num_rows = len(self.df)
        num_columns = len(self.df.columns)
        column_names = list(self.df.columns)
        data_types = self.df.dtypes
        return (f"Количество строк: {num_rows}"
                f"Количество столбцов: {num_columns}"
                f"Названия колонок: {column_names}"
                f"Тип данных: {data_types}")


def get_info(file_name):
    df = pd.read_csv(text.URL + file_name)
    info_printer = PdInf(df)
    info_printer.display_info()

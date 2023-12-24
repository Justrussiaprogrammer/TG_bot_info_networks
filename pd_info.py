class PdInf:
    def __init__(self, df):
        self.df = df

    def display_inf0(self):
        num_rows = len(self.df)
        num_columns = len(self.df.columns)
        column_names = list(self.df.columns)
        data_types = self.df.dtypes
        print (f"Количество строк: {num_rows}")
        print(f"Количество столбцов: {num_columns}")
        print(f"Названия колонок: {column_names}")
        print(f"Тип данных: {data_types}")

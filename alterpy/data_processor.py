import pandas as pd

class DataProcessor:
    def __init__(self, dataframe):
        self.df = dataframe

    def drop_nulls(self):
        return self.df.dropna()

    def fill_nulls(self, value=0):
        return self.df.fillna(value)

    def rename_columns(self, rename_dict):
        return self.df.rename(columns=rename_dict)

    def filter_rows(self, condition):
        return self.df.query(condition)

    def sort_values(self, by, ascending=True):
        return self.df.sort_values(by=by, ascending=ascending)

    def reset_index(self):
        return self.df.reset_index(drop=True)

    def set_index(self, column):
        return self.df.set_index(column)

    def group_by(self, column):
        return self.df.groupby(column)

    def drop_duplicates(self):
        return self.df.drop_duplicates()

    def convert_dtype(self, column, dtype):
        self.df[column] = self.df[column].astype(dtype)
        return self.df

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def drop_nulls(self):
        self.data = self.data.dropna()
        return self.data

    def fill_nulls(self, value):
        self.data = self.data.fillna(value)
        return self.data

    def remove_duplicates(self):
        self.data = self.data.drop_duplicates()
        return self.data

    def convert_dtype(self, column, dtype):
        self.data[column] = self.data[column].astype(dtype)
        return self.data

    def filter_rows(self, condition):
        return self.data.query(condition)

    def rename_columns(self, mapping):
        self.data = self.data.rename(columns=mapping)
        return self.data

    def reset_index(self):
        self.data = self.data.reset_index(drop=True)
        return self.data

    def drop_column(self, column):
        self.data = self.data.drop(columns=[column])
        return self.data

    def sort_by_column(self, column):
        self.data = self.data.sort_values(by=column)
        return self.data

    def group_by(self, column):
        return self.data.groupby(column).mean()

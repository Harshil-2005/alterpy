class Analyzer:
    def __init__(self, dataframe):
        self.df = dataframe

    def describe_data(self):
        return self.df.describe()

    def null_values(self):
        return self.df.isnull().sum()

    def correlation_matrix(self):
        return self.df.corr()

    def value_counts(self, column):
        return self.df[column].value_counts()

    def get_unique(self, column):
        return self.df[column].unique()

    def get_mode(self, column):
        return self.df[column].mode()

    def get_median(self, column):
        return self.df[column].median()

    def get_mean(self, column):
        return self.df[column].mean()

    def get_min(self, column):
        return self.df[column].min()

    def get_max(self, column):
        return self.df[column].max()

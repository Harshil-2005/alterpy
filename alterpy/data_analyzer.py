class Analyzer:
    def __init__(self, dataframe):
        self.df = dataframe

    def column_mean(self, column):
        return self.df[column].mean()

    def column_median(self, column):
        return self.df[column].median()

    def column_mode(self, column):
        return self.df[column].mode()

    def column_std(self, column):
        return self.df[column].std()

    def column_variance(self, column):
        return self.df[column].var()

    def column_min(self, column):
        return self.df[column].min()

    def column_max(self, column):
        return self.df[column].max()

    def correlation_matrix(self):
        return self.df.corr(numeric_only=True)

    def count_unique(self, column):
        return self.df[column].nunique()

    def value_counts(self, column):
        return self.df[column].value_counts()

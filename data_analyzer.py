import pandas as pd

class Analyzer:
    def __init__(self, data):
        """Initialize with a DataFrame."""
        self.data = data

    def calculate_mean(self, column):
        """Calculate the mean (average) of a numeric column."""
        return self.data[column].mean()

    def calculate_median(self, column):
        """Calculate the median of a numeric column."""
        return self.data[column].median()

    def calculate_mode(self, column):
        """Calculate the mode of a column."""
        return self.data[column].mode().tolist()

    def calculate_standard_deviation(self, column):
        """Calculate the standard deviation of a numeric column."""
        return self.data[column].std()

    def calculate_variance(self, column):
        """Calculate the variance of a numeric column."""
        return self.data[column].var()

    def get_min_value(self, column):
        """Get the minimum value in a numeric column."""
        return self.data[column].min()

    def get_max_value(self, column):
        """Get the maximum value in a numeric column."""
        return self.data[column].max()

    def count_unique_values(self, column):
        """Count unique values in a column."""
        return self.data[column].nunique()

    def get_value_counts(self, column):
        """Get the frequency count of unique values in a column."""
        return self.data[column].value_counts()

    def correlation_matrix(self):
        """Return the correlation matrix of numeric columns."""
        return self.data.corr()

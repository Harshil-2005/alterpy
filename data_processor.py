import pandas as pd

class DataProcessor:
    def __init__(self, data):
        """Initialize with a DataFrame."""
        self.data = data

    def drop_missing_values(self):
        """Drop rows with missing values."""
        self.data = self.data.dropna()
        return self.data

    def fill_missing_values(self, column, value):
        """Fill missing values in a specific column."""
        self.data[column] = self.data[column].fillna(value)
        return self.data

    def convert_column_type(self, column, dtype):
        """Convert a column to a specific data type."""
        try:
            self.data[column] = self.data[column].astype(dtype)
        except Exception as e:
            print(f"Error converting column {column}: {e}")
        return self.data

    def remove_duplicates(self):
        """Remove duplicate rows from the dataset."""
        self.data = self.data.drop_duplicates()
        return self.data

    def filter_by_value(self, column, value):
        """Filter data based on a column value."""
        return self.data[self.data[column] == value]

    def normalize_column(self, column):
        """Normalize a numeric column (0 to 1 scaling)."""
        if column in self.data.columns and pd.api.types.is_numeric_dtype(self.data[column]):
            self.data[column] = (self.data[column] - self.data[column].min()) / (self.data[column].max() - self.data[column].min())
        else:
            print(f"Column {column} is not numeric.")
        return self.data

    def rename_columns(self, rename_dict):
        """Rename columns using a dictionary mapping."""
        self.data = self.data.rename(columns=rename_dict)
        return self.data

    def sort_by_column(self, column, ascending=True):
        """Sort the data by a specific column."""
        self.data = self.data.sort_values(by=column, ascending=ascending)
        return self.data

    def group_by_column(self, column):
        """Group data by a column and count occurrences."""
        return self.data.groupby(column).size().reset_index(name='Count')

    def get_processed_data(self):
        """Return the processed DataFrame."""
        return self.data

import pandas as pd
import json
import sqlite3

class DataLoader:
    def __init__(self, file_path=None):
        """Initialize DataLoader with an optional file path."""
        self.file_path = file_path
        self.data = None

    def load_csv(self):
        """Load data from a CSV file."""
        try:
            self.data = pd.read_csv(self.file_path)
            return self.data
        except Exception as e:
            print(f"Error loading CSV file: {e}")

    def load_excel(self):
        """Load data from an Excel file."""
        try:
            self.data = pd.read_excel(self.file_path)
            return self.data
        except Exception as e:
            print(f"Error loading Excel file: {e}")

    def load_json(self):
        """Load data from a JSON file."""
        try:
            with open(self.file_path, 'r') as file:
                self.data = pd.DataFrame(json.load(file))
            return self.data
        except Exception as e:
            print(f"Error loading JSON file: {e}")

    def load_sql(self, db_path, table_name):
        """Load data from an SQL database."""
        try:
            conn = sqlite3.connect(db_path)
            self.data = pd.read_sql(f"SELECT * FROM {table_name}", conn)
            conn.close()
            return self.data
        except Exception as e:
            print(f"Error loading SQL data: {e}")

    def get_data(self):
        """Return the loaded data."""
        return self.data

    def preview_data(self, rows=5):
        """Preview the first few rows of the dataset."""
        if self.data is not None:
            return self.data.head(rows)
        print("No data loaded.")

    def get_summary(self):
        """Return summary statistics of the dataset."""
        if self.data is not None:
            return self.data.describe()
        print("No data loaded.")

    def get_columns(self):
        """Return the column names of the dataset."""
        if self.data is not None:
            return self.data.columns.tolist()
        print("No data loaded.")

    def check_missing_values(self):
        """Check for missing values in the dataset."""
        if self.data is not None:
            return self.data.isnull().sum()
        print("No data loaded.")

    def drop_missing_values(self):
        """Drop rows with missing values."""
        if self.data is not None:
            self.data = self.data.dropna()
            return self.data
        print("No data loaded.")

import pandas as pd

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_csv(self):
        try:
            return pd.read_csv(self.file_path)
        except Exception as e:
            print(f"Error loading CSV file: {e}")
            return None

    def load_excel(self):
        try:
            return pd.read_excel(self.file_path)
        except Exception as e:
            print(f"Error loading Excel file: {e}")
            return None

    def load_json(self):
        try:
            return pd.read_json(self.file_path)
        except Exception as e:
            print(f"Error loading JSON file: {e}")
            return None

    def preview(self, df, n=5):
        return df.head(n)

    def get_shape(self, df):
        return df.shape

    def get_columns(self, df):
        return df.columns.tolist()

    def get_dtypes(self, df):
        return df.dtypes

    def get_summary(self, df):
        return df.describe()

    def save_to_csv(self, df, filename):
        df.to_csv(filename, index=False)

    def save_to_excel(self, df, filename):
        df.to_excel(filename, index=False)

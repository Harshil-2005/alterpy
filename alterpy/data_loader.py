import pandas as pd

class DataLoader:
    def __init__(self, filepath):
        self.filepath = filepath

    def load_csv(self):
        try:
            return pd.read_csv(self.filepath)
        except Exception as e:
            print(f"Error loading CSV file: {e}")
            return None

    def load_excel(self):
        try:
            return pd.read_excel(self.filepath)
        except Exception as e:
            print(f"Error loading Excel file: {e}")
            return None

    def load_json(self):
        try:
            return pd.read_json(self.filepath)
        except Exception as e:
            print(f"Error loading JSON file: {e}")
            return None

    def load_sql(self, query, connection):
        try:
            return pd.read_sql_query(query, connection)
        except Exception as e:
            print(f"Error loading SQL data: {e}")
            return None

    def preview_data(self, df, rows=5):
        return df.head(rows)

    def get_shape(self, df):
        return df.shape

    def get_columns(self, df):
        return df.columns.tolist()

    def get_info(self, df):
        return df.info()

    def get_summary(self, df):
        return df.describe()

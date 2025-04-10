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

    def load_sql(self, con, query):
        try:
            return pd.read_sql(query, con)
        except Exception as e:
            print(f"Error loading SQL data: {e}")
            return None

    def file_info(self):
        try:
            df = pd.read_csv(self.file_path)
            return df.info()
        except:
            return "File info not available"

    def preview(self, n=5):
        try:
            df = pd.read_csv(self.file_path)
            return df.head(n)
        except:
            return None

    def column_names(self):
        try:
            df = pd.read_csv(self.file_path)
            return df.columns.tolist()
        except:
            return []

    def shape(self):
        try:
            df = pd.read_csv(self.file_path)
            return df.shape
        except:
            return (0, 0)

    def get_dtypes(self):
        try:
            df = pd.read_csv(self.file_path)
            return df.dtypes
        except:
            return None

    def is_empty(self):
        try:
            df = pd.read_csv(self.file_path)
            return df.empty
        except:
            return True

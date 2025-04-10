from datetime import datetime

class ReportGenerator:
    def __init__(self, dataframe):
        self.df = dataframe

    def generate_summary(self):
        return self.df.describe()

    def generate_null_report(self):
        return self.df.isnull().sum()

    def generate_dtype_report(self):
        return self.df.dtypes

    def generate_shape_report(self):
        return {'rows': self.df.shape[0], 'columns': self.df.shape[1]}

    def generate_column_report(self, column):
        return {
            "unique": self.df[column].nunique(),
            "top": self.df[column].mode()[0],
            "nulls": self.df[column].isnull().sum()
        }

    def save_to_csv(self, filename):
        self.df.to_csv(filename, index=False)

    def save_to_excel(self, filename):
        self.df.to_excel(filename, index=False)

    def generate_timestamped_report(self, prefix="report"):
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{prefix}_{timestamp}.csv"
        self.df.to_csv(filename, index=False)
        return filename

    def get_memory_usage(self):
        return self.df.memory_usage(deep=True)

    def get_column_distribution(self, column):
        return self.df[column].value_counts(normalize=True)

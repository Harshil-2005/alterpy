class ReportGenerator:
    def __init__(self, dataframe):
        self.df = dataframe

    def generate_summary(self):
        return self.df.describe().to_string()

    def missing_value_report(self):
        return self.df.isnull().sum().to_string()

    def data_types_report(self):
        return self.df.dtypes.to_string()

    def column_stats(self, column):
        stats = {
            'mean': self.df[column].mean(),
            'median': self.df[column].median(),
            'mode': self.df[column].mode()[0],
            'min': self.df[column].min(),
            'max': self.df[column].max()
        }
        return stats

    def save_to_csv(self, filename):
        self.df.to_csv(filename, index=False)
        return f"Saved to {filename}"

    def save_to_excel(self, filename):
        self.df.to_excel(filename, index=False)
        return f"Saved to {filename}"

    def to_html_report(self):
        return self.df.to_html()

    def count_unique_values(self):
        return self.df.nunique().to_string()

    def generate_correlation_report(self):
        return self.df.corr().to_string()

    def generate_skew_kurtosis(self):
        return {
            'skew': self.df.skew().to_dict(),
            'kurtosis': self.df.kurtosis().to_dict()
        }

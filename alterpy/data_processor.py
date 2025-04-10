import pandas as pd

class DataProcessor:
    def __init__(self, dataframe):
        self.df = dataframe

    def drop_nulls(self):
        self.df = self.df.dropna()
        return self

    def fill_nulls(self, value="Unknown"):
        self.df = self.df.fillna(value)
        return self

    def rename_columns(self, rename_dict):
        self.df = self.df.rename(columns=rename_dict)
        return self

    def filter_by_status(self, status):
        return self.df[self.df['Status'] == status]

    def get_student_attendance(self, student_id):
        return self.df[self.df['StudentID'] == student_id]

    def attendance_summary(self):
        return self.df.groupby(['StudentID', 'Name'])['Status'].value_counts().unstack(fill_value=0)

    def attendance_percentage(self):
        summary = self.attendance_summary()
        summary['Total'] = summary.sum(axis=1)
        summary['Percentage'] = (summary.get('Present', 0) / summary['Total']) * 100
        return summary

    def sort_by_date(self):
        self.df['Date'] = pd.to_datetime(self.df['Date'])
        self.df = self.df.sort_values(by='Date')
        return self

    def unique_students(self):
        return self.df[['StudentID', 'Name']].drop_duplicates()

    def drop_duplicates(self):
        self.df = self.df.drop_duplicates()
        return self

    def convert_dtype(self, column, dtype):
        self.df[column] = self.df[column].astype(dtype)
        return self

    def get_data(self):
        return self.df

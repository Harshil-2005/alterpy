import pandas as pd

class Analyzer:
    def __init__(self, dataframe):
        self.df = dataframe

    def attendance_summary(self, status_col='Status'):
        return self.df[status_col].value_counts()

    def student_attendance_stats(self):
        return self.df.groupby('Student')['Status'].value_counts().unstack(fill_value=0)

    def top_absentees(self, n=5):
        absents = self.df[self.df['Status'] == 'Absent']
        return absents['Student'].value_counts().head(n)

    def attendance_by_day(self):
        return self.df.groupby('Date')['Status'].value_counts().unstack(fill_value=0)

    def average_attendance_per_day(self):
        total_per_day = self.df.groupby('Date')['Status'].count()
        present_per_day = self.df[self.df['Status'] == 'Present'].groupby(self.df['Date']).count()['Status']
        return (present_per_day / total_per_day) * 100

    def attendance_trend(self):
        return self.df[self.df['Status'] == 'Present'].groupby('Date').count()['Status']

    def absentee_percentage_by_student(self):
        summary = self.student_attendance_stats()
        summary['Total'] = summary.sum(axis=1)
        summary['AbsentPercentage'] = (summary.get('Absent', 0) / summary['Total']) * 100
        return summary[['AbsentPercentage']]

    def most_regular_students(self, top_n=5):
        summary = self.student_attendance_stats()
        summary['Total'] = summary.sum(axis=1)
        summary['PresentRate'] = summary.get('Present', 0) / summary['Total']
        return summary.sort_values(by='PresentRate', ascending=False).head(top_n)

    def most_irregular_students(self, bottom_n=5):
        summary = self.student_attendance_stats()
        summary['Total'] = summary.sum(axis=1)
        summary['PresentRate'] = summary.get('Present', 0) / summary['Total']
        return summary.sort_values(by='PresentRate', ascending=True).head(bottom_n)

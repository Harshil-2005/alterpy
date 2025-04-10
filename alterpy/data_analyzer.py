class Analyzer:
    def __init__(self, data):
        self.data = data

    def calculate_average_attendance(self):
        return self.data['Attendance'].mean()

    def calculate_min_attendance(self):
        return self.data['Attendance'].min()

    def calculate_max_attendance(self):
        return self.data['Attendance'].max()

    def count_low_attendance(self, threshold=75):
        return (self.data['Attendance'] < threshold).sum()

    def percentage_above_threshold(self, threshold=75):
        total = len(self.data)
        above = (self.data['Attendance'] >= threshold).sum()
        return (above / total) * 100

    def std_dev_attendance(self):
        return self.data['Attendance'].std()

    def median_attendance(self):
        return self.data['Attendance'].median()

    def get_attendance_distribution(self):
        return self.data['Attendance'].value_counts(bins=5)

    def student_with_lowest_attendance(self):
        return self.data.loc[self.data['Attendance'].idxmin()]

    def student_with_highest_attendance(self):
        return self.data.loc[self.data['Attendance'].idxmax()]

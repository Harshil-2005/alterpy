import pandas as pd

class ReportGenerator:
    def __init__(self, data):
        """Initialize with a DataFrame."""
        self.data = data

    def generate_summary_report(self):
        """Generate a summary report with basic statistics."""
        return self.data.describe()

    def missing_values_report(self):
        """Generate a report on missing values."""
        return self.data.isnull().sum()

    def attendance_percentage_summary(self, column):
        """Generate a summary of attendance percentage."""
        return {
            "Mean": self.data[column].mean(),
            "Median": self.data[column].median(),
            "Min": self.data[column].min(),
            "Max": self.data[column].max()
        }

    def generate_student_report(self, student_id):
        """Generate an individual report for a specific student."""
        return self.data[self.data["StudentID"] == student_id]

    def export_to_csv(self, filename="report.csv"):
        """Export the report to a CSV file."""
        self.data.to_csv(filename, index=False)
        return f"Report saved as {filename}"

    def export_to_excel(self, filename="report.xlsx"):
        """Export the report to an Excel file."""
        self.data.to_excel(filename, index=False)
        return f"Report saved as {filename}"

    def export_to_json(self, filename="report.json"):
        """Export the report to a JSON file."""
        self.data.to_json(filename, orient="records", indent=4)
        return f"Report saved as {filename}"

    def generate_top_attendees(self, column, top_n=5):
        """Generate a report of the top N students with highest attendance."""
        return self.data.nlargest(top_n, column)

    def generate_low_attendance_report(self, column, threshold=50):
        """Generate a report of students with attendance below a certain threshold"""

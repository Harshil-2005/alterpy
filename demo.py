import pandas as pd
import os
import matplotlib.pyplot as plt
from alterpy.data_loader import DataLoader
from alterpy.data_processor import DataProcessor
from alterpy.data_analyzer import Analyzer
from alterpy.report_generator import ReportGenerator

class Visualizer:
    def __init__(self, df):
        self.df = df

    def plot_daily_attendance(self, date_col, status_col):
        plt.figure()
        daily = self.df.groupby(date_col)[status_col].value_counts().unstack().fillna(0)
        daily.plot(kind='bar', stacked=True, figsize=(12, 6))
        plt.title("Daily Attendance")
        plt.xlabel("Date")
        plt.ylabel("Count")

    def pie_chart_distribution(self, status_col):
        plt.figure()
        counts = self.df[status_col].value_counts()
        counts.plot(kind='pie', autopct='%1.1f%%', figsize=(8, 8))
        plt.title("Attendance Status Distribution")

def save_and_show_plot(name):
    os.makedirs("plots", exist_ok=True)
    plt.tight_layout()
    plt.savefig(f"plots/{name}.png")
    plt.show()
    plt.clf()  # Clear figure after saving

def main():
    loader = DataLoader("sample_attendance.csv")
    df = loader.load_csv()

    processor = DataProcessor(df)
    df = processor.drop_nulls()
    df = processor.drop_duplicates()
    df = processor.convert_dtype('Date', 'str')
    df = processor.convert_dtype('Student', 'str')
    df = processor.convert_dtype('Status', 'str')

    visualizer = Visualizer(df)

    visualizer.plot_daily_attendance('Date', 'Status')
    save_and_show_plot("daily_attendance")

    visualizer.pie_chart_distribution('Status')
    save_and_show_plot("status_pie_chart")

    analyzer = Analyzer(df)
    summary = analyzer.attendance_summary('Status')
    print(summary)

    report = ReportGenerator(df)
    report.generate_summary_report('attendance_summary_report.txt')

if __name__ == '__main__':
    main()

import matplotlib.pyplot as plt
import seaborn as sns
import os

class Visualizer:
    def __init__(self, df):
        self.df = df

    def plot_daily_bar_chart(self, date_col, status_col):
        plt.figure()
        daily = self.df.groupby(date_col)[status_col].value_counts().unstack().fillna(0)
        daily.plot(kind='bar', stacked=True, figsize=(12, 6))
        plt.title("Daily Attendance")
        plt.xlabel("Date")
        plt.ylabel("Count")
        self._save("daily_bar_chart")

    def line_chart_trend(self, date_col, status_value_col='Status', value='Present'):
        plt.figure()
        trend = self.df[self.df[status_value_col] == value]
        trend = trend.groupby(date_col).size()
        trend.plot(kind='line', marker='o', figsize=(12, 5))
        plt.title(f"{value} Attendance Over Time")
        plt.xlabel("Date")
        plt.ylabel("Count")
        self._save("line_chart_trend")

    def pie_chart_distribution(self, status_col):
        plt.figure()
        counts = self.df[status_col].value_counts()
        counts.plot(kind='pie', autopct='%1.1f%%', figsize=(8, 8))
        plt.title("Attendance Status Distribution")
        self._save("pie_chart_distribution")

    def stacked_attendance_by_student(self, student_col, status_col):
        plt.figure()
        stacked = self.df.groupby(student_col)[status_col].value_counts().unstack().fillna(0)
        stacked.plot(kind='bar', stacked=True, figsize=(14, 6))
        plt.title("Stacked Attendance by Student")
        plt.xlabel("Student")
        plt.ylabel("Count")
        self._save("stacked_by_student")

    def heatmap_attendance_trend(self, date_col, student_col, status_col):
        df_filtered = self.df[self.df[status_col] == "Present"]
        pivot = df_filtered.pivot_table(index=student_col, columns=date_col, aggfunc='size', fill_value=0)
        plt.figure(figsize=(14, 6))
        sns.heatmap(pivot, cmap="Greens", linewidths=0.5, linecolor='gray')
        plt.title("Heatmap of Present Attendance")
        self._save("heatmap_attendance")

    def _save(self, name):
        os.makedirs("plots", exist_ok=True)
        plt.tight_layout()
        plt.savefig(f"plots/{name}.png")
        plt.show()
        plt.clf()

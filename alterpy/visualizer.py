import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Visualizer:
    def __init__(self, dataframe):
        self.df = dataframe

    def pie_chart(self, labels_col, values_col, save_path=None, show=False):
        plt.figure(figsize=(6, 6))
        plt.pie(self.df[values_col], labels=self.df[labels_col], autopct='%1.1f%%', startangle=140)
        plt.axis('equal')
        if save_path:
            plt.savefig(save_path)
        if show:
            plt.show()
        plt.close()

    def bar_chart(self, x_col, y_col, title='', save_path=None, show=False):
        plt.figure(figsize=(8, 5))
        sns.barplot(data=self.df, x=x_col, y=y_col)
        plt.title(title)
        if save_path:
            plt.savefig(save_path)
        if show:
            plt.show()
        plt.close()

    def line_chart(self, x_col, y_col, title='', save_path=None):
        plt.figure(figsize=(8, 5))
        sns.lineplot(data=self.df, x=x_col, y=y_col)
        plt.title(title)
        if save_path:
            plt.savefig(save_path)
        plt.close()

    def stacked_bar_chart(self, group_col, status_cols, title='', save_path=None):
        df_grouped = self.df.groupby(group_col)[status_cols].sum()
        df_grouped.plot(kind='bar', stacked=True, figsize=(10, 6))
        plt.title(title)
        if save_path:
            plt.savefig(save_path)
        plt.close()

    def heatmap_attendance(self, pivot_index, pivot_columns, values_col, save_path=None):
        pivot_table = self.df.pivot_table(index=pivot_index, columns=pivot_columns, values=values_col, aggfunc='count', fill_value=0)
        plt.figure(figsize=(10, 6))
        sns.heatmap(pivot_table, annot=True, fmt='d', cmap='YlGnBu')
        if save_path:
            plt.savefig(save_path)
        plt.close()

    def scatter_plot(self, x_col, y_col, title='', save_path=None):
        plt.figure(figsize=(8, 5))
        sns.scatterplot(data=self.df, x=x_col, y=y_col)
        plt.title(title)
        if save_path:
            plt.savefig(save_path)
        plt.close()

    def histogram(self, col, bins=10, title='', save_path=None):
        plt.figure(figsize=(8, 5))
        sns.histplot(self.df[col], bins=bins, kde=True)
        plt.title(title)
        if save_path:
            plt.savefig(save_path)
        plt.close()

    def box_plot(self, x_col, y_col, title='', save_path=None):
        plt.figure(figsize=(8, 5))
        sns.boxplot(data=self.df, x=x_col, y=y_col)
        plt.title(title)
        if save_path:
            plt.savefig(save_path)
        plt.close()

    def violin_plot(self, x_col, y_col, title='', save_path=None):
        plt.figure(figsize=(8, 5))
        sns.violinplot(data=self.df, x=x_col, y=y_col)
        plt.title(title)
        if save_path:
            plt.savefig(save_path)
        plt.close()

    def attendance_trend_plot(self, date_col, count_col, title='', save_path=None):
        daily = self.df.groupby(date_col)[count_col].count().reset_index()
        plt.figure(figsize=(10, 5))
        sns.lineplot(data=daily, x=date_col, y=count_col)
        plt.title(title)
        if save_path:
            plt.savefig(save_path)
        plt.close()

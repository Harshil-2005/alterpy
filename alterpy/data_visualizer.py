import matplotlib.pyplot as plt
import seaborn as sns

class Visualizer:
    def __init__(self, dataframe):
        self.df = dataframe

    def bar_plot(self, x, y):
        sns.barplot(x=self.df[x], y=self.df[y])
        plt.show()

    def histogram(self, column):
        self.df[column].hist()
        plt.show()

    def box_plot(self, column):
        sns.boxplot(x=self.df[column])
        plt.show()

    def scatter_plot(self, x, y):
        self.df.plot.scatter(x=x, y=y)
        plt.show()

    def heatmap(self):
        sns.heatmap(self.df.corr(), annot=True)
        plt.show()

    def line_plot(self, x, y):
        self.df.plot.line(x=x, y=y)
        plt.show()

    def pie_chart(self, column):
        self.df[column].value_counts().plot.pie(autopct='%1.1f%%')
        plt.show()

    def kde_plot(self, column):
        sns.kdeplot(self.df[column], shade=True)
        plt.show()

    def count_plot(self, column):
        sns.countplot(x=self.df[column])
        plt.show()

    def violin_plot(self, x, y):
        sns.violinplot(x=self.df[x], y=self.df[y])
        plt.show()

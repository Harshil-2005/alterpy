import matplotlib.pyplot as plt
import seaborn as sns

class Visualizer:
    def __init__(self, dataframe):
        self.df = dataframe

    def plot_line(self, x, y):
        self.df.plot(x=x, y=y, kind='line')
        plt.show()

    def plot_bar(self, x, y):
        self.df.plot(x=x, y=y, kind='bar')
        plt.show()

    def plot_histogram(self, column):
        self.df[column].hist()
        plt.show()

    def plot_box(self, column):
        self.df.boxplot(column=column)
        plt.show()

    def plot_scatter(self, x, y):
        self.df.plot.scatter(x=x, y=y)
        plt.show()

    def plot_correlation_heatmap(self):
        sns.heatmap(self.df.corr(numeric_only=True), annot=True, cmap="coolwarm")
        plt.show()

    def plot_pie(self, column):
        self.df[column].value_counts().plot.pie(autopct='%1.1f%%')
        plt.show()

    def plot_kde(self, column):
        self.df[column].plot.kde()
        plt.show()

    def plot_violin(self, x, y):
        sns.violinplot(x=self.df[x], y=self.df[y])
        plt.show()

    def plot_pairplot(self):
        sns.pairplot(self.df)
        plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

class Visualizer:
    def __init__(self, data):
        self.data = data

    def plot_bar(self, x, y):
        self.data.plot(kind='bar', x=x, y=y)
        plt.title("Bar Chart")
        plt.show()

    def plot_line(self, x, y):
        self.data.plot(kind='line', x=x, y=y)
        plt.title("Line Chart")
        plt.show()

    def plot_pie(self, column):
        self.data[column].value_counts().plot.pie(autopct='%1.1f%%')
        plt.title("Pie Chart")
        plt.ylabel('')
        plt.show()

    def plot_histogram(self, column):
        self.data[column].plot.hist()
        plt.title("Histogram")
        plt.show()

    def plot_box(self, column):
        sns.boxplot(data=self.data[column])
        plt.title("Boxplot")
        plt.show()

    def plot_heatmap(self):
        sns.heatmap(self.data.corr(), annot=True)
        plt.title("Correlation Heatmap")
        plt.show()

    def scatter_plot(self, x, y):
        self.data.plot.scatter(x=x, y=y)
        plt.title("Scatter Plot")
        plt.show()

    def kde_plot(self, column):
        sns.kdeplot(self.data[column], shade=True)
        plt.title("KDE Plot")
        plt.show()

    def pairplot(self):
        sns.pairplot(self.data)
        plt.show()

    def distplot(self, column):
        sns.histplot(self.data[column], kde=True)
        plt.title("Distplot")
        plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

class Visualizer:
    def __init__(self, data):
        """Initialize with a DataFrame."""
        self.data = data

    def plot_histogram(self, column, bins=10):
        """Plot a histogram of a numeric column."""
        plt.figure(figsize=(8, 5))
        sns.histplot(self.data[column], bins=bins, kde=True)
        plt.title(f"Histogram of {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.show()

    def plot_bar_chart(self, column):
        """Plot a bar chart for categorical data."""
        plt.figure(figsize=(8, 5))
        self.data[column].value_counts().plot(kind="bar", color="skyblue")
        plt.title(f"Bar Chart of {column}")
        plt.xlabel(column)
        plt.ylabel("Count")
        plt.show()

    def plot_boxplot(self, column):
        """Plot a boxplot to show the distribution of a column."""
        plt.figure(figsize=(8, 5))
        sns.boxplot(y=self.data[column])
        plt.title(f"Boxplot of {column}")
        plt.show()

    def plot_scatter(self, column_x, column_y):
        """Plot a scatter plot between two numerical columns."""
        plt.figure(figsize=(8, 5))
        sns.scatterplot(x=self.data[column_x], y=self.data[column_y])
        plt.title(f"Scatter Plot: {column_x} vs {column_y}")
        plt.xlabel(column_x)
        plt.ylabel(column_y)
        plt.show()

    def plot_correlation_heatmap(self):
        """Plot a heatmap of the correlation matrix."""
        plt.figure(figsize=(8, 5))
        sns.heatmap(self.data.corr(), annot=True, cmap="coolwarm", fmt=".2f")
        plt.title("Correlation Heatmap")
        plt.show()

    def plot_pie_chart(self, column):
        """Plot a pie chart for categorical data."""
        plt.figure(figsize=(8, 5))
        self.data[column].value_counts().plot.pie(autopct="%1.1f%%", colors=sns.color_palette("pastel"))
        plt.title(f"Pie Chart of {column}")
        plt.ylabel("")
        plt.show()

    def plot_line_chart(self, column_x, column_y):
        """Plot a line chart between two numerical columns."""
        plt.figure(figsize=(8, 5))
        sns.lineplot(x=self.data[column_x], y=self.data[column_y])
        plt.title(f"Line Chart: {column_x} vs {column_y}")
        plt.xlabel(column_x)
        plt.ylabel(column_y)
        plt.show()

    def plot_violin_plot(self, column):
        """Plot a violin plot for a numeric column."""
        plt.figure(figsize=(8, 5))
        sns.violinplot(y=self.data[column])
        plt.title(f"Violin Plot of {column}")
        plt.show()

    def plot_pairplot(self):
        """Plot a pairplot to show relationships between numerical columns."""
        plt.figure(figsize=(8, 5))
        sns.pairplot(self.data)
        plt.show()

    def plot_countplot(self, column):
        """Plot a count plot for categorical data."""
        plt.figure(figsize=(8, 5))
        sns.countplot(x=self.data[column])
        plt.title(f"Count Plot of {column}")
        plt.xlabel(column)
        plt.ylabel("Count")
        plt.show()


import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from alterpy.visualizer import Visualizer
import pandas as pd

def test_plot_bar_chart():
    df = pd.DataFrame({"Student": ["A"], "Present": [5]})
    vis = Visualizer(df)
    vis.bar_chart("Student", "Present")
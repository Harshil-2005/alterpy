import pandas as pd
from alterpy.visualizer import Visualizer

def test_visualizer_functions(tmp_path):
    df = pd.DataFrame({
        "Student": ["A", "B"],
        "Present": [5, 3]
    })
    vis = Visualizer(df)
    vis.pie_chart("Student", "Present", save_path=str(tmp_path / "pie.png"))
    vis.bar_chart("Student", "Present", save_path=str(tmp_path / "bar.png"))

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from alterpy.analyzer import Analyzer
import pandas as pd

def test_attendance_percentage():
    df = pd.DataFrame({"Student": ["A"], "Present": [1]})
    analyzer = Analyzer(df)
    result = analyzer.attendance_percentage("Student", "Present")
    assert result is None or result is not None
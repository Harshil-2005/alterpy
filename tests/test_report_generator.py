import pandas as pd
from alterpy.report_generator import ReportGenerator

def test_generate_pdf(tmp_path):
    df = pd.DataFrame({
        "Name": ["A", "B"],
        "Attendance": [90, 85]
    })
    rg = ReportGenerator(df)
    rg.generate_pdf(str(tmp_path / "report.pdf"))

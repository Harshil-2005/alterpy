from fpdf import FPDF
import pandas as pd

class ReportGenerator:
    def __init__(self, dataframe):
        self.df = dataframe

    def generate_pdf(self, filename, title="Attendance Report"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.set_title(title)
        pdf.cell(200, 10, txt=title, ln=True, align='C')

        col_names = self.df.columns.tolist()
        col_width = 190 / len(col_names)
        
        pdf.set_font("Arial", 'B', size=10)
        for col in col_names:
            pdf.cell(col_width, 10, col, border=1)
        pdf.ln()

        pdf.set_font("Arial", size=10)
        for _, row in self.df.iterrows():
            for col in col_names:
                pdf.cell(col_width, 10, str(row[col]), border=1)
            pdf.ln()

        pdf.output(filename)

    def export_to_csv(self, filename):
        self.df.to_csv(filename, index=False)

    def export_to_excel(self, filename):
        self.df.to_excel(filename, index=False)

    def export_to_json(self, filename):
        self.df.to_json(filename, orient='records', indent=4)

    def generate_summary(self):
        return self.df.describe(include='all')

    def attendance_summary_table(self):
        if 'Status' in self.df.columns:
            return self.df['Status'].value_counts()
        return pd.Series()

    def top_attendees(self, top_n=5):
        if 'Attendance' in self.df.columns:
            return self.df.sort_values(by='Attendance', ascending=False).head(top_n)
        return pd.DataFrame()

    def low_attendees(self, bottom_n=5):
        if 'Attendance' in self.df.columns:
            return self.df.sort_values(by='Attendance', ascending=True).head(bottom_n)
        return pd.DataFrame()

    def missing_data_report(self):
        return self.df.isnull().sum()

    def get_data(self):
        return self.df

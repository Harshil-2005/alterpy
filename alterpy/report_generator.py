from fpdf import FPDF

class ReportGenerator:
    def __init__(self, data):
        self.data = data

    def generate_report(self, filename):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Attendance Report", ln=1, align='C')
        for index, row in self.data.iterrows():
            line = f"{row['Name']}: {row['Attendance']}%"
            pdf.cell(200, 10, txt=line, ln=1)
        pdf.output(filename)

    def add_title(self, pdf, title):
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(200, 10, txt=title, ln=True, align='C')

    def add_table(self, pdf):
        pdf.set_font("Arial", size=10)
        for index, row in self.data.iterrows():
            line = ' | '.join([str(x) for x in row])
            pdf.cell(200, 10, txt=line, ln=1)

    def add_footer(self, pdf, text):
        pdf.set_y(-15)
        pdf.set_font("Arial", size=8)
        pdf.cell(0, 10, txt=text, align='C')

    def save_as_txt(self, filename):
        with open(filename, 'w') as f:
            f.write(self.data.to_string())

    def save_as_html(self, filename):
        self.data.to_html(filename)

    def export_summary(self, filename):
        summary = self.data.describe()
        summary.to_csv(filename)

    def generate_simple_report(self, filename):
        self.data.to_csv(filename, index=False)

    def highlight_low_attendance(self, threshold=75):
        return self.data[self.data['Attendance'] < threshold]

    def attendance_summary_dict(self):
        return {
            "Average": self.data["Attendance"].mean(),
            "Min": self.data["Attendance"].min(),
            "Max": self.data["Attendance"].max()
        }

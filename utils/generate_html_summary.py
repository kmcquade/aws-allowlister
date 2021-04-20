import os
import json
import datetime
from aws_allowlister.bin.version import __version__
from jinja2 import Environment, FileSystemLoader
from aws_allowlister.database.database import connect_db
from aws_allowlister.database.compliance_data import ComplianceData

compliance_data = ComplianceData()
db_session = connect_db()


def generate_sample_data(rows: list):
    sample_data_js_file = os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        "sampleData.js"
    ))
    content = f"""var sample_data = {json.dumps(rows, indent=4)}


exports.sample_data = sample_data;

"""
    if os.path.exists(sample_data_js_file):
        print(f"Removing existing file and replacing its contents")
        os.remove(sample_data_js_file)

    with open(sample_data_js_file, "w") as f:
        f.write(content)


class HTMLReport:
    """Inject the JS files and report results into the final HTML report"""
    def __init__(self, results):
        self.report_generated_time = datetime.datetime.now().strftime("%Y-%m-%d")
        self.results = f"var report_data = {json.dumps(results)}"

    def __repr__(self):
        return self.get_html_report()

    def get_html_report(self):
        """Returns the rendered HTML report"""
        template_contents = dict(
            # results
            results=self.results,
            # report metadata
            report_generated_time=str(self.report_generated_time),
            version=__version__,
        )
        template_path = os.path.join(os.path.dirname(__file__))
        env = Environment(loader=FileSystemLoader(template_path))  # nosec
        template = env.get_template("template.html")
        return template.render(t=template_contents)


def generate_html_summary():
    rows = compliance_data.get_rows_with_emoji(db_session=db_session)
    generate_sample_data(rows=rows)
    html_report = HTMLReport(results=rows)
    rendered_report = html_report.get_html_report()
    html_output_file = os.path.join(os.path.dirname(__file__), os.path.pardir, "index.html")
    if os.path.exists(html_output_file):
        print(f"{html_output_file} exists. Removing then replacing...")
        os.remove(html_output_file)

    with open(html_output_file, "w") as f:
        f.write(rendered_report)


if __name__ == '__main__':
    download_docs = True
    generate_html_summary()


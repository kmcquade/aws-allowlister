import os
import csv
import json
import pandas as pd
from aws_allowlister.database.build import build_database
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


def generate_html_summary():
    rows = compliance_data.get_rows(db_session=db_session)
    print()
    generate_sample_data(rows=rows)
    print()


if __name__ == '__main__':
    download_docs = True
    generate_html_summary()


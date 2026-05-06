"""
Convert survey_questionnaire.md to survey_questionnaire.pdf using Python.

Dependencies:
    pip install markdown weasyprint

Usage:
    python convert_to_pdf.py
"""

import pathlib
import markdown
from weasyprint import HTML, CSS

INPUT_FILE = pathlib.Path(__file__).parent / "survey_questionnaire.md"
OUTPUT_FILE = pathlib.Path(__file__).parent / "survey_questionnaire.pdf"

CSS_STYLE = CSS(string="""
    @page {
        size: A4;
        margin: 2cm 2.5cm;
    }
    body {
        font-family: Arial, sans-serif;
        font-size: 11pt;
        line-height: 1.6;
        color: #222;
    }
    h1 {
        font-size: 16pt;
        text-align: center;
        margin-bottom: 4pt;
    }
    h2 {
        font-size: 13pt;
        color: #1a1a4e;
        border-bottom: 1px solid #aaa;
        padding-bottom: 3pt;
        margin-top: 18pt;
    }
    hr {
        border: none;
        border-top: 1px solid #ccc;
        margin: 12pt 0;
    }
    table {
        width: 100%;
        border-collapse: collapse;
        font-size: 10pt;
        margin: 8pt 0;
    }
    th, td {
        border: 1px solid #bbb;
        padding: 4pt 6pt;
        text-align: center;
    }
    th {
        background-color: #e8e8f0;
        font-weight: bold;
    }
    td:nth-child(2) {
        text-align: left;
    }
    blockquote {
        background: #f5f5f5;
        border-left: 4px solid #888;
        margin: 8pt 0;
        padding: 6pt 10pt;
        font-size: 9.5pt;
        color: #444;
    }
    ul {
        margin: 4pt 0;
        padding-left: 18pt;
    }
    li {
        margin-bottom: 2pt;
    }
    strong {
        color: #111;
    }
    p {
        margin: 6pt 0;
    }
    em {
        font-style: italic;
    }
""")


def convert():
    md_text = INPUT_FILE.read_text(encoding="utf-8")

    # Convert markdown to HTML with tables and extra extensions
    html_body = markdown.markdown(
        md_text,
        extensions=["tables", "extra", "sane_lists"],
    )

    html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Survey Questionnaire</title>
</head>
<body>
{html_body}
</body>
</html>"""

    HTML(string=html_doc, base_url=str(INPUT_FILE.parent)).write_pdf(
        OUTPUT_FILE, stylesheets=[CSS_STYLE]
    )

    print(f"PDF created: {OUTPUT_FILE}")


if __name__ == "__main__":
    convert()

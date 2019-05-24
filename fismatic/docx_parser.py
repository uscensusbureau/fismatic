from docx import Document
from . import parser


class DocxParser:
    def __init__(self, doc_path):
        self.doc = Document(docx=doc_path)

    def get_tables(self):
        return parser.get_tables(self.doc)

    def get_controls(self):
        # Control details are in tables, skip the rest
        tables = self.get_tables()
        return parser.get_controls(tables)

    def get_implementations_by_id(self):
        """The ID (key) is the control name + part."""
        result = {}

        controls = self.get_controls()
        for name, control in controls.items():
            for part, txt in control.implementation.items():
                key = ": ".join([name, part])
                val = txt.strip().lower()
                result[key] = val

        return result

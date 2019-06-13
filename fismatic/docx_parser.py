from docx import Document
from . import parser
from .control_set import ControlSet


class DocxParser:
    def __init__(self, doc_path):
        self.doc = Document(docx=doc_path)
        self.doc_path = doc_path

    def get_tables(self):
        return parser.get_tables(self.doc)

    def get_controls(self):
        # Control details are in tables, skip the rest
        tables = self.get_tables()
        return parser.get_controls(tables)

    def get_control_set(self):
        controls = list(self.get_controls().values())
        return ControlSet(controls, source=self.doc_path)

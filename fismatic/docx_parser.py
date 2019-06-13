from docx import Document
from . import parser
from .control_set import ControlSet


class DocxParser:
    def __init__(self, doc_path):
        self.doc = Document(docx=doc_path)
        controls = self.get_controls().values()
        self.control_set = ControlSet(controls, source=doc_path)

    def get_tables(self):
        return parser.get_tables(self.doc)

    def get_controls(self):
        # Control details are in tables, skip the rest
        tables = self.get_tables()
        return parser.get_controls(tables)

    def get_control_set(self):
        return self.control_set

from docx import Document
from . import parser


class FedrampParser:
    def __init__(self, doc_path):
        self.doc = Document(docx=doc_path)

    def get_tables(self):
        return parser.get_tables(self.doc)

    def get_controls(self):
        # Control details are in tables, skip the rest
        tables = self.get_tables()
        return parser.get_controls(tables)

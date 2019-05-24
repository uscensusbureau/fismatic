from docx import Document
from . import parser
from .control_set import ControlSet


class DocxParser:
    def __init__(self, doc_path):
        self.doc = Document(docx=doc_path)
        controls = self.get_controls().values()
        self.control_set = ControlSet(controls)

    def get_tables(self):
        return parser.get_tables(self.doc)

    def get_controls(self):
        # Control details are in tables, skip the rest
        tables = self.get_tables()
        return parser.get_controls(tables)

    def get_implementations_by_id(self):
        return self.control_set.get_implementations_by_id()

    def num_controls(self):
        return self.control_set.num_controls()

    def num_implementations(self):
        return self.control_set.num_implementations()

    def num_unique_implementations(self):
        return self.control_set.num_unique_implementations()

    def num_identical_implementations(self):
        return self.control_set.num_identical_implementations()

    def num_words(self):
        return self.control_set.num_words()

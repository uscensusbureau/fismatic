from docx import Document
from functools import reduce
from . import parser
from .similarity import tokenize


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

    def num_controls(self):
        controls = self.get_controls()
        return len(controls.items())

    def num_implementations(self):
        implementations_by_id = self.get_implementations_by_id()
        return len(implementations_by_id)

    def num_unique_implementations(self):
        implementations_by_id = self.get_implementations_by_id()
        return len(set(implementations_by_id.values()))

    def num_identical_implementations(self):
        return self.num_implementations() - self.num_unique_implementations()

    def num_words(self):
        implementations_by_id = self.get_implementations_by_id()
        return reduce(
            lambda sum, imp: sum + len(tokenize(imp)), implementations_by_id.values(), 0
        )

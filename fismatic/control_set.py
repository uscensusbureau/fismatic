from functools import reduce
from .similarity import tokenize


class ControlSet:
    def __init__(self, controls):
        self._controls = controls

    def get_implementations_by_id(self):
        """The ID (key) is the control name + part."""
        result = {}

        for control in self._controls:
            for part, txt in control.implementation.items():
                key = ": ".join([control.name, part])
                val = txt.strip().lower()
                result[key] = val

        return result

    def num_controls(self):
        return len(self._controls)

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


import re
from .similarity import nlp


class Control:
    def __init__(self, name=None):
        self.name = name
        """Specific to FedRAMP templates"""
        self.responsible_role = None
        self.imp_status = None
        self.origination = None
        self.implementation = {}

    @property
    def implementation(self):
        return self._implementation

    @implementation.setter
    def implementation(self, value):
        self._implementation = {part: nlp(imp) for part, imp in value.items()}

    def normalized_name(self):
        # remove any spaces
        name = self.name.replace(" ", "")
        parsed = re.match("([A-Z]{2})-(\d+)(\((\d+)\))?", name)
        family = parsed[1]
        num = parsed[2]
        enhancement = parsed[4]

        result = "{}-{}".format(family, num)
        if enhancement:
            result = "{} ({})".format(result, enhancement)
        return result

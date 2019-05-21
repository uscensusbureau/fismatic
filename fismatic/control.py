import re


class Control:
    def __init__(self, name=None):
        self.name = name
        """Specific to FedRAMP templates"""
        self.responsible_role = None
        self.imp_status = None
        self.origination = None
        self.implementation = {}

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

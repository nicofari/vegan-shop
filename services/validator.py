import re

class Validator:
    _STRING_PATTERN = "^[A-Za-z0-9 ]+$"
    _INTEGER_PATTERN = "^[0-9]+"
    _FLOAT_PATTERN = "^[0-9.]+"
    
    def __init__(self):
        self.pattern_alphanumeric_string = re.compile(self._STRING_PATTERN)
        self.pattern_integer = re.compile(self._INTEGER_PATTERN)
        self.pattern_float = re.compile(self._FLOAT_PATTERN)
    
    def validate_string(self, value):
        return self._validate(self.pattern_alphanumeric_string, value)

    def validate_not_negative_integer(self, value):
        return self._validate(self.pattern_integer, value)

    def validate_not_negative_float(self, value):
        return self._validate(self.pattern_float, value)

    def _validate(self, pattern, value):
        return pattern.match(value)
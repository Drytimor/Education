
class MyFloatConverter:
    regex = r'[+-]?(\d*\.)?\d+'

    def to_python(self, value: float):
        return float(value)

    def to_url(self, value):
        return str(value)


class SplitConvertor:
    regex = r'(\w+,)+\w+'

    def to_python(self, value: str):
        return value.split(',')

    def to_url(self, value):
        return ','.join(value)


class UpperConvertor:
    regex = r'\w+'

    def to_python(self, value: str):
        return value.upper()

    def to_url(self, value):
        return value.lower()


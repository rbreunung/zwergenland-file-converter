
from unittest import TestCase

from converter.excel_reader import ExcelReader


class TestExcelReader(TestCase):

    def test_hello(self):
        unit = ExcelReader("res/Mappe1.xlsx")
        unit.hello()
        pass


from unittest import TestCase

from converter.excel_reader import ExcelReader, KinderGardenExcelSheetConfiguration


class TestExcelReader(TestCase):

    def test_read_parent_contacts(self):
        unit = ExcelReader("res/Mappe1.xlsx")
        unit.read_parent_contacts(KinderGardenExcelSheetConfiguration())

"""Contains class ExcelReader and default behavior constants."""
from typing import List
import pandas

from converter.type.contact import Contact

# all row constants are 0 based, while Excel UI is 1 based
DEFAULT_HEADLINE_ROW = 2
DEFAULT_FIRST_DATA_ROW = 3


class ExcelReader:
    """The behavior necessary to open a .xlsx file and parse the contacts from the known format."""

    def __init__(self, file_name: str) -> None:
        self._file = pandas.read_excel(file_name, engine='openpyxl')

    def read_parent_contacts(self) -> List[Contact]:
        """Read the Excel file in the child-parent-format and parse parent contacts."""
        print("\nhello\n")
        starting_row = DEFAULT_FIRST_DATA_ROW - 1
        data_frame = self._file
        for index in range(starting_row, len(data_frame)):
            cell_value = data_frame.iloc[index, 2]
            if pandas.isna(cell_value):
                print(f"Stopping iteration at index {index} where Column 2 is empty")
                break
            print(f"{cell_value} ")
        return []

    def read_member_contacts(self) -> List[Contact]:
        """Read the excel in the association member format and parse contacts."""
        return []

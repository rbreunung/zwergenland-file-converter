
from sys import stdout
import pandas

# all row constants are 0 based, while Excel UI is 1 based
DEFAULT_HEADLINE_ROW = 2
DEFAULT_FIRST_DATA_ROW = 3


class ExcelReader:

    def __init__(self, file_name: str) -> None:
        self._file = pandas.read_excel(file_name)

    def hello(self):
        print("\nhello\n")
        starting_row = DEFAULT_FIRST_DATA_ROW - 1
        data_frame = self._file
        for index in range(starting_row, len(data_frame)):
            cell_value = data_frame.iloc[index, 2]
            if pandas.isna(cell_value):
                print(f"Stopping iteration at index {index} where Column 2 is empty")
                break
            print(f"{cell_value} ")

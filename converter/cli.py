"""Main application for CLI interaction."""


from argparse import ArgumentParser, Namespace

from converter.excel_reader import ExcelReader, KinderGardenExcelSheetConfiguration


def command_read_kindergarden_sheet(args: Namespace):
    """Read the parent list from a Kindergarden parents sheet."""

    reader = ExcelReader(args.input_file)
    contacts = reader.read_parent_contacts(KinderGardenExcelSheetConfiguration())
    for contact in contacts:
        print(contact)


def main():
    """Entry point of CLI. Initialize the parser and run the commands."""
    parser = ArgumentParser(
        prog="python converter/cli.py",
        description="This app reads .xlsx files of a well known standard and parses user data."
    )
    parser.add_argument("command", choices=["read"])
    args = parser.parse_args()
    match args.command:
        case "read":
            command_read_kindergarden_sheet(args)
        case _:
            parser.print_help()


if __name__ == '__main__':
    main()

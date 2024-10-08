"""Main application for GUI interaction."""
from tkinter import StringVar, Tk
from tkinter.ttk import Button, Entry, Frame, Label


def close(root_window: Tk):
    """Close the window and the application."""
    root_window.destroy()


def add_input_frame_widgets(frame: Frame):
    """Add all widgets to the inputs frame and connect the relevant commands."""

    entry_value = StringVar()

    label = Label(frame, text="Excel Input")
    label.grid(column=0, row=0,padx=10,pady=10)
    entry = Entry(frame, width=50, textvariable=entry_value,state="readonly")
    entry.grid(column=1, row=0)
    button = Button(frame, text="Select")
    button.grid(column=2, row=0, padx=10,pady=10)


def main():
    """Create an entry UI."""
    root_window = Tk()
    root_window.title("Converter")

    input_frame = Frame(root_window)
    input_frame.grid(column=0, row=0)
    add_input_frame_widgets(input_frame)

    close_button = Button(root_window, text="Close", command=lambda: close(root_window))
    close_button.grid(column=0, row=1, padx=10, pady=10, sticky="e")

    root_window.mainloop()


if __name__ == '__main__':
    main()

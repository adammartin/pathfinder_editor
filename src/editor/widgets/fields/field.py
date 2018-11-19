import tkinter
from tkinter import W
from editor.widgets.fields import label


class GridField():
    def __init__(self, panel, a_row, a_column, label_text, event_function):
        actual_col = a_column*2
        self._label = label.GridLabel(panel, a_row, actual_col, label_text)
        self._field = tkinter.StringVar()
        self._field.trace('w', event_function)
        self._entry = tkinter.Entry(panel, textvariable=self._field)
        self._entry.grid(row=a_row, column=actual_col+1, sticky=W)

    def update(self, function, locked):
        if self._field.get() and not locked:
            function(self._field.get())


class GridOptionMenu():
    def __init__(self, panel, a_row, a_column, label_text, choices, event_function):
        # pylint: disable=too-many-arguments
        actual_col = a_column*2
        self._label = label.GridLabel(panel, a_row, actual_col, label_text)
        self._field = tkinter.StringVar()
        self._field.trace('w', event_function)
        self._option_menu = tkinter.OptionMenu(panel, self._field, *choices)
        self._option_menu.grid(row=a_row, column=actual_col+1, sticky=W)

    def update(self, function, locked):
        if self._field.get() and not locked:
            function(self._field.get())

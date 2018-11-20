import tkinter
from tkinter import W
from editor.widgets.defaults import DEFAULT_BACKGROUND


class GridLabel():
    def __init__(self, panel, a_row, a_column, label_text):
        self._label = tkinter.Label(panel, borderwidth=1, text=label_text)
        self._label.configure(background=DEFAULT_BACKGROUND)
        self._label.grid(row=a_row, column=a_column, sticky=W)

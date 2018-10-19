from tkinter import ttk


DEFAULT_BACKGROUND = '#EBEBEB'


def default_style():
    style = ttk.Style()
    style.configure('Default.TFrame', background=DEFAULT_BACKGROUND)
    style.configure('Default.TNotebook', background=DEFAULT_BACKGROUND)
    return style

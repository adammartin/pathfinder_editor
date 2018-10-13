from tkinter import ttk


DEFAULT_BACKGROUND = '#EBEBEB'


def default_style():
    s = ttk.Style()
    s.configure('Default.TFrame', background=DEFAULT_BACKGROUND)
    s.configure('Default.TNotebook', background=DEFAULT_BACKGROUND)
    return s

from tkinter import ttk, Label, StringVar, Entry, OptionMenu
from tkinter import W, EW
from editor.widgets.defaults import DEFAULT_BACKGROUND
from editor.widgets.fields.field import GridField


class Tab():
    # pylint: disable=too-few-public-methods
    def __init__(self, notebook):
        self._panel = ttk.Frame(notebook, style='Default.TFrame')
        self._notebook = notebook
        self._dirty_lock = False

    def _append_grid_field(self, stat, fields, func):
        fields.append(
            {
                'field': GridField(self._panel,
                                   stat['position'][0],
                                   stat['position'][1],
                                   stat['label'],
                                   func),
                'getter': stat['getter'],
                'setter': stat['setter']
            }
        )

    def _add_field(self, a_row, a_col, label_text, function):
        col = a_col*2
        self._add_label(a_row, col, label_text)
        variable = StringVar()
        variable.trace('w', function)
        entry = Entry(self._panel, textvariable=variable)
        entry.grid(row=a_row, column=col+1, sticky=W)
        return variable

    def _add_dropdown(self, a_row, a_col, label, choices, function):
        # pylint: disable=too-many-arguments
        col = a_col*2
        self._add_label(a_row, col, label)
        variable = StringVar()
        variable.trace('w', function)
        entry = OptionMenu(self._panel, variable, *choices)
        entry.grid(row=a_row, column=col+1, sticky=EW)
        return variable

    def _add_label(self, a_row, a_col, label_text):
        label = Label(self._panel, text=label_text, borderwidth=1)
        label.configure(background=DEFAULT_BACKGROUND)
        label.grid(row=a_row, column=a_col, sticky=W)
        return label

    def _update(self, field, function):
        if field.get() and not self._dirty_lock:
            function(field.get())


def _set_fields(source, fields):
    for field in fields:
        _set_field(field, source)


def _set_field(field, source):
    value = getattr(source, field['getter'])()
    field['field'].set(value)


def _update_field(field, source, locked):
    field['field'].update(getattr(source, field['setter']), locked)

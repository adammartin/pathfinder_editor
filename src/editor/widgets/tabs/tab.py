from tkinter import ttk
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


def _set_fields(source, fields):
    for field in fields:
        _set_field(field, source)


def _set_field(field, source):
    value = getattr(source, field['getter'])()
    field['field'].set(value)


def _update_field(field, source, locked):
    field['field'].update(getattr(source, field['setter']), locked)

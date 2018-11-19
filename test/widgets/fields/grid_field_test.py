import pytest
import tkinter
from tkinter import W
from unittest import mock
from unittest.mock import patch
from editor.widgets.fields import label
from editor.widgets.fields.field import GridField



ROW = mock.MagicMock()
COLUMN = mock.MagicMock()
LABEL_TEXT = "SOME LABEL_TEXT"
PANEL = mock.MagicMock()
LOCKED = True
UNLOCKED = False



#    def _add_field(self, a_row, a_col, label_text, function):
#        col = a_col*2
#        self._add_label(a_row, col, label_text)
#        variable = StringVar()
#        variable.trace('w', function)
#        entry = Entry(self._panel, textvariable=variable)
#        entry.grid(row=a_row, column=col+1, sticky=W)
#        return variable

#    def _update(self, field, function):
#        if field.get() and not self._dirty_lock:
#            function(field.get())


@patch('tkinter.Entry')
@patch('tkinter.StringVar')
@patch('editor.widgets.fields.label.GridLabel')
def test_field_properly_composed(mock_label, mock_var, mock_entry):
    field = GridField(PANEL, ROW, COLUMN, LABEL_TEXT)
    mock_var.assert_called()
    var_instance = mock_var.return_value
    mock_label.assert_called_with(PANEL, ROW, COLUMN*2, LABEL_TEXT)
    mock_entry.assert_called_with(PANEL, textvariable=var_instance)


@patch('tkinter.Entry')
@patch('tkinter.StringVar')
@patch('editor.widgets.fields.label.GridLabel')
def test_field_positioned_on_grid(mock_label, mock_var, mock_entry):
    field = GridField(PANEL, ROW, COLUMN, LABEL_TEXT)
    mock_entry.return_value.grid.assert_called_with(row=ROW, column=(COLUMN*2)+2, sticky=W)


@patch('tkinter.Entry')
@patch('tkinter.StringVar')
@patch('editor.widgets.fields.label.GridLabel')
def test_field_updates_function(mock_label, mock_var, mock_entry):
    function = mock.MagicMock()
    field = GridField(PANEL, ROW, COLUMN, LABEL_TEXT)
    expected_value = '5'
    mock_var.return_value.get.return_value = expected_value
    field.update(function, UNLOCKED)
    function.assert_called_with(expected_value)


@patch('tkinter.Entry')
@patch('tkinter.StringVar')
@patch('editor.widgets.fields.label.GridLabel')
def test_field_updates_function_if_not_None(mock_label, mock_var, mock_entry):
    function = mock.MagicMock()
    field = GridField(PANEL, ROW, COLUMN, LABEL_TEXT)
    expected_value = None
    mock_var.return_value.get.return_value = expected_value
    field.update(function, UNLOCKED)
    function.assert_not_called()


@patch('tkinter.Entry')
@patch('tkinter.StringVar')
@patch('editor.widgets.fields.label.GridLabel')
def test_field_updates_function_if_not_None(mock_label, mock_var, mock_entry):
    function = mock.MagicMock()
    field = GridField(PANEL, ROW, COLUMN, LABEL_TEXT)
    expected_value = '5'
    mock_var.return_value.get.return_value = expected_value
    field.update(function, LOCKED)
    function.assert_not_called()

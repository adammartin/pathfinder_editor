import pytest
import tkinter
from tkinter import W
from unittest import mock
from unittest.mock import patch
from editor.widgets.fields import label
from editor.widgets.fields.field import GridField, GridOptionMenu



ROW = mock.MagicMock()
COLUMN = mock.MagicMock()
EVENT_FUNCTION = mock.MagicMock()
CHOICES = ['foo', 'bar']
LABEL_TEXT = "SOME LABEL_TEXT"
PANEL = mock.MagicMock()
LOCKED = True
UNLOCKED = False


@patch('tkinter.Entry')
@patch('tkinter.StringVar')
@patch('editor.widgets.fields.label.GridLabel')
def test_field_properly_composed(mock_label, mock_var, mock_entry):
    field = GridField(PANEL, ROW, COLUMN, LABEL_TEXT, EVENT_FUNCTION)
    var_instance = mock_var.return_value
    mock_label.assert_called_with(PANEL, ROW, COLUMN*2, LABEL_TEXT)
    mock_entry.assert_called_with(PANEL, textvariable=var_instance)


@patch('tkinter.Entry')
@patch('tkinter.StringVar')
@patch('editor.widgets.fields.label.GridLabel')
def test_field_positioned_on_grid(mock_label, mock_var, mock_entry):
    field = GridField(PANEL, ROW, COLUMN, LABEL_TEXT, EVENT_FUNCTION)
    mock_entry.return_value.grid.assert_called_with(row=ROW, column=(COLUMN*2)+2, sticky=W)


@patch('tkinter.Entry')
@patch('tkinter.StringVar')
@patch('editor.widgets.fields.label.GridLabel')
def test_field_will_properly_be_updated_by_entry(mock_label, mock_var, mock_entry):
    field = GridField(PANEL, ROW, COLUMN, LABEL_TEXT, EVENT_FUNCTION)
    var_instance = mock_var.return_value
    var_instance.trace.assert_called_with('w', EVENT_FUNCTION)


@patch('tkinter.Entry')
@patch('tkinter.StringVar')
@patch('editor.widgets.fields.label.GridLabel')
def test_field_updates_function(mock_label, mock_var, mock_entry):
    function = mock.MagicMock()
    field = GridField(PANEL, ROW, COLUMN, LABEL_TEXT, EVENT_FUNCTION)
    expected_value = '5'
    mock_var.return_value.get.return_value = expected_value
    field.update(function, UNLOCKED)
    function.assert_called_with(expected_value)


@patch('tkinter.Entry')
@patch('tkinter.StringVar')
@patch('editor.widgets.fields.label.GridLabel')
def test_field_updates_function_if_not_None(mock_label, mock_var, mock_entry):
    function = mock.MagicMock()
    field = GridField(PANEL, ROW, COLUMN, LABEL_TEXT, EVENT_FUNCTION)
    expected_value = None
    mock_var.return_value.get.return_value = expected_value
    field.update(function, UNLOCKED)
    function.assert_not_called()


@patch('tkinter.Entry')
@patch('tkinter.StringVar')
@patch('editor.widgets.fields.label.GridLabel')
def test_field_updates_function_if_not_None(mock_label, mock_var, mock_entry):
    function = mock.MagicMock()
    field = GridField(PANEL, ROW, COLUMN, LABEL_TEXT, EVENT_FUNCTION)
    expected_value = '5'
    mock_var.return_value.get.return_value = expected_value
    field.update(function, LOCKED)
    function.assert_not_called()


@patch('tkinter.OptionMenu')
@patch('tkinter.StringVar')
@patch('editor.widgets.fields.label.GridLabel')
def test_option_properly_composed(mock_label, mock_var, mock_option):
    field = GridOptionMenu(PANEL, ROW, COLUMN, LABEL_TEXT, CHOICES, EVENT_FUNCTION)
    var_instance = mock_var.return_value
    mock_label.assert_called_with(PANEL, ROW, COLUMN*2, LABEL_TEXT)
    mock_option.assert_called_with(PANEL, var_instance, *CHOICES)


@patch('tkinter.OptionMenu')
@patch('tkinter.StringVar')
@patch('editor.widgets.fields.label.GridLabel')
def test_option_positioned_on_grid(mock_label, mock_var, mock_option):
    field = GridOptionMenu(PANEL, ROW, COLUMN, LABEL_TEXT, CHOICES, EVENT_FUNCTION)
    mock_option.return_value.grid.assert_called_with(row=ROW, column=(COLUMN*2)+2, sticky=W)


@patch('tkinter.OptionMenu')
@patch('tkinter.StringVar')
@patch('editor.widgets.fields.label.GridLabel')
def test_field_will_properly_be_updated_by_entry(mock_label, mock_var, mock_option):
    field = GridOptionMenu(PANEL, ROW, COLUMN, LABEL_TEXT, CHOICES, EVENT_FUNCTION)
    var_instance = mock_var.return_value
    var_instance.trace.assert_called_with('w', EVENT_FUNCTION)


@patch('tkinter.OptionMenu')
@patch('tkinter.StringVar')
@patch('editor.widgets.fields.label.GridLabel')
def test_field_updates_function(mock_label, mock_var, mock_option):
    function = mock.MagicMock()
    field = GridOptionMenu(PANEL, ROW, COLUMN, LABEL_TEXT, CHOICES, EVENT_FUNCTION)
    expected_value = '5'
    mock_var.return_value.get.return_value = expected_value
    field.update(function, UNLOCKED)
    function.assert_called_with(expected_value)


@patch('tkinter.OptionMenu')
@patch('tkinter.StringVar')
@patch('editor.widgets.fields.label.GridLabel')
def test_field_updates_function_if_not_None(mock_label, mock_var, mock_option):
    function = mock.MagicMock()
    field = GridOptionMenu(PANEL, ROW, COLUMN, LABEL_TEXT, CHOICES, EVENT_FUNCTION)
    expected_value = None
    mock_var.return_value.get.return_value = expected_value
    field.update(function, UNLOCKED)
    function.assert_not_called()


@patch('tkinter.OptionMenu')
@patch('tkinter.StringVar')
@patch('editor.widgets.fields.label.GridLabel')
def test_field_updates_function_if_not_None(mock_label, mock_var, mock_option):
    function = mock.MagicMock()
    field = GridOptionMenu(PANEL, ROW, COLUMN, LABEL_TEXT, CHOICES, EVENT_FUNCTION)
    expected_value = '5'
    mock_var.return_value.get.return_value = expected_value
    field.update(function, LOCKED)
    function.assert_not_called()

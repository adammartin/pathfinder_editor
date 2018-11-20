import pytest
import tkinter
from tkinter import W, EW
from unittest import mock
from unittest.mock import patch
from editor.widgets.fields import label
from editor.widgets.fields.field import GridField, GridOptionMenu, GridPortraitMenu


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
def test_field_will_properly_set(mock_label, mock_var, mock_entry):
    value = "Some Value"
    field = GridField(PANEL, ROW, COLUMN, LABEL_TEXT, EVENT_FUNCTION)
    field.set(value)
    var_instance = mock_var.return_value
    var_instance.set.assert_called_with(value)


@patch('tkinter.Entry')
@patch('tkinter.StringVar')
@patch('editor.widgets.fields.label.GridLabel')
def test_field_will_not_be_set_to_None(mock_label, mock_var, mock_entry):
    value = None
    field = GridField(PANEL, ROW, COLUMN, LABEL_TEXT, EVENT_FUNCTION)
    field.set(value)
    var_instance = mock_var.return_value
    var_instance.set.assert_not_called()


@patch('tkinter.Entry')
@patch('tkinter.StringVar')
@patch('editor.widgets.fields.label.GridLabel')
def test_field_will_not_be_set_to_None_string(mock_label, mock_var, mock_entry):
    value = 'None'
    field = GridField(PANEL, ROW, COLUMN, LABEL_TEXT, EVENT_FUNCTION)
    field.set(value)
    var_instance = mock_var.return_value
    var_instance.set.assert_not_called()


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
    mock_option.return_value.grid.assert_called_with(row=ROW, column=(COLUMN*2)+2, sticky=EW)


@patch('tkinter.OptionMenu')
@patch('tkinter.StringVar')
@patch('editor.widgets.fields.label.GridLabel')
def test_option_will_properly_set(mock_label, mock_var, mock_option):
    value = CHOICES[0]
    field = GridOptionMenu(PANEL, ROW, COLUMN, LABEL_TEXT, CHOICES, EVENT_FUNCTION)
    field.set(value)
    var_instance = mock_var.return_value
    var_instance.set.assert_called_with(value)


@patch('tkinter.OptionMenu')
@patch('tkinter.StringVar')
@patch('editor.widgets.fields.label.GridLabel')
def test_option_will_not_set_value_not_in_options(mock_label, mock_var, mock_option):
    value = "Some Value"
    field = GridOptionMenu(PANEL, ROW, COLUMN, LABEL_TEXT, CHOICES, EVENT_FUNCTION)
    field.set(value)
    var_instance = mock_var.return_value
    var_instance.set.assert_not_called()


@patch('tkinter.OptionMenu')
@patch('tkinter.StringVar')
@patch('editor.widgets.fields.label.GridLabel')
def test_option_will_not_be_set_to_None(mock_label, mock_var, mock_option):
    value = None
    field = GridOptionMenu(PANEL, ROW, COLUMN, LABEL_TEXT, CHOICES, EVENT_FUNCTION)
    field.set(value)
    var_instance = mock_var.return_value
    var_instance.set.assert_not_called()


@patch('tkinter.OptionMenu')
@patch('tkinter.StringVar')
@patch('editor.widgets.fields.label.GridLabel')
def test_option_will_not_be_set_to_None_string(mock_label, mock_var, mock_option):
    value = 'None'
    field = GridOptionMenu(PANEL, ROW, COLUMN, LABEL_TEXT, CHOICES, EVENT_FUNCTION)
    field.set(value)
    var_instance = mock_var.return_value
    var_instance.set.assert_not_called()


@patch('tkinter.OptionMenu')
@patch('tkinter.StringVar')
@patch('editor.widgets.fields.label.GridLabel')
def test_option_will_properly_be_updated_by_entry(mock_label, mock_var, mock_option):
    field = GridOptionMenu(PANEL, ROW, COLUMN, LABEL_TEXT, CHOICES, EVENT_FUNCTION)
    var_instance = mock_var.return_value
    var_instance.trace.assert_called_with('w', EVENT_FUNCTION)


@patch('tkinter.OptionMenu')
@patch('tkinter.StringVar')
@patch('editor.widgets.fields.label.GridLabel')
def test_option_updates_function(mock_label, mock_var, mock_option):
    function = mock.MagicMock()
    field = GridOptionMenu(PANEL, ROW, COLUMN, LABEL_TEXT, CHOICES, EVENT_FUNCTION)
    expected_value = '5'
    mock_var.return_value.get.return_value = expected_value
    field.update(function, UNLOCKED)
    function.assert_called_with(expected_value)


@patch('tkinter.OptionMenu')
@patch('tkinter.StringVar')
@patch('editor.widgets.fields.label.GridLabel')
def test_option_updates_function_if_not_None(mock_label, mock_var, mock_option):
    function = mock.MagicMock()
    field = GridOptionMenu(PANEL, ROW, COLUMN, LABEL_TEXT, CHOICES, EVENT_FUNCTION)
    expected_value = None
    mock_var.return_value.get.return_value = expected_value
    field.update(function, UNLOCKED)
    function.assert_not_called()


@patch('tkinter.OptionMenu')
@patch('tkinter.StringVar')
@patch('editor.widgets.fields.label.GridLabel')
def test_option_updates_function_if_not_None(mock_label, mock_var, mock_option):
    function = mock.MagicMock()
    field = GridOptionMenu(PANEL, ROW, COLUMN, LABEL_TEXT, CHOICES, EVENT_FUNCTION)
    expected_value = '5'
    mock_var.return_value.get.return_value = expected_value
    field.update(function, LOCKED)
    function.assert_not_called()


@patch('editor.widgets.fields.field.GridOptionMenu')
def test_portraits_will_render_options_when_options_exist(mock_options):
    field = GridPortraitMenu(PANEL, ROW, COLUMN, LABEL_TEXT, CHOICES, EVENT_FUNCTION)
    mock_options.assert_called_with(PANEL, ROW, COLUMN, LABEL_TEXT, CHOICES, EVENT_FUNCTION)


@patch('editor.widgets.fields.field.GridOptionMenu')
def test_portraits_will_not_render_options_when_options_empty(mock_options):
    field = GridPortraitMenu(PANEL, ROW, COLUMN, LABEL_TEXT, [], EVENT_FUNCTION)
    mock_options.assert_not_called()


@patch('editor.widgets.fields.field.GridOptionMenu')
def test_portraits_will_not_render_options_when_options_None(mock_options):
    field = GridPortraitMenu(PANEL, ROW, COLUMN, LABEL_TEXT, None, EVENT_FUNCTION)
    mock_options.assert_not_called()


@patch('editor.widgets.fields.field.GridOptionMenu')
def test_portraits_will_delegate_update_to_option_menu(mock_options):
    field = GridPortraitMenu(PANEL, ROW, COLUMN, LABEL_TEXT, CHOICES, EVENT_FUNCTION)
    field.update(EVENT_FUNCTION, UNLOCKED)
    options_instance = mock_options.return_value
    options_instance.update.assert_called_with(EVENT_FUNCTION, UNLOCKED)


@patch('editor.widgets.fields.field.GridOptionMenu')
def test_portraits_will_do_nothing_for_update_when_no_choices(mock_options):
    field = GridPortraitMenu(PANEL, ROW, COLUMN, LABEL_TEXT, [], EVENT_FUNCTION)
    field.update(EVENT_FUNCTION, UNLOCKED)
    options_instance = mock_options.return_value
    options_instance.update.assert_not_called()


@patch('editor.widgets.fields.field.GridOptionMenu')
def test_portraits_will_delegate_set_to_option_menu(mock_options):
    field = GridPortraitMenu(PANEL, ROW, COLUMN, LABEL_TEXT, CHOICES, EVENT_FUNCTION)
    field.set(CHOICES[1])
    options_instance = mock_options.return_value
    options_instance.set.assert_called_with(CHOICES[1])


@patch('editor.widgets.fields.field.GridOptionMenu')
def test_portraits_will_do_nothing_for_set_when_no_choices(mock_options):
    field = GridPortraitMenu(PANEL, ROW, COLUMN, LABEL_TEXT, [], EVENT_FUNCTION)
    field.set(CHOICES[1])
    options_instance = mock_options.return_value
    options_instance.set.assert_not_called()

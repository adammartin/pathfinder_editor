import pytest
import tkinter
from tkinter import W
from unittest import mock
from unittest.mock import patch
from editor.widgets.fields.label import GridLabel
from editor.widgets.defaults import DEFAULT_BACKGROUND



ROW = mock.MagicMock()
COLUMN = mock.MagicMock()
LABEL_TEXT = "SOME LABEL_TEXT"
PANEL = mock.MagicMock()


@patch('tkinter.Label')
def test_label_configured(mock_label):
    label = GridLabel(PANEL, ROW, COLUMN, LABEL_TEXT)
    mock_label.assert_called_with(PANEL, text=LABEL_TEXT, borderwidth=1)
    mock_label.return_value.configure.assert_called_with(background=DEFAULT_BACKGROUND)


@patch('tkinter.Label')
def test_label_set_on_grid(mock_label):
    label = GridLabel(PANEL, ROW, COLUMN, LABEL_TEXT)
    mock_label.assert_called_with(PANEL, text=LABEL_TEXT, borderwidth=1)
    mock_label.return_value.grid.assert_called_with(row=ROW, column=COLUMN, sticky=W)

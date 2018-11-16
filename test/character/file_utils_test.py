import pytest
from pathlib import Path
from unittest import mock
from unittest.mock import patch, call
from editor.character.file_utils import list_portrait_dirs


SAVE_DIR = '/blarg/Saved Games'
PORTRAIT_DIR = '/blarg/Portraits'
PORTRAITS = ['foo', 'bar']


def walk():
    yield PORTRAIT_DIR, PORTRAITS, ['.DS_STORE']

@patch('os.walk')
def test_list_portrait_dirs(mock_os_walk):
    mock_os_walk.return_value = walk()
    expected_path = Path(SAVE_DIR).parent / 'Portraits'
    assert list_portrait_dirs(Path(SAVE_DIR)) == sorted(PORTRAITS)
    mock_os_walk.assert_called_with(expected_path)


@patch('os.walk')
def test_list_portrait_dirs(mock_os_walk):
    mock_os_walk.side_effect = StopIteration()
    expected_path = Path(SAVE_DIR).parent / 'Portraits'
    assert list_portrait_dirs(Path(SAVE_DIR)) == []
    mock_os_walk.assert_called_with(expected_path)

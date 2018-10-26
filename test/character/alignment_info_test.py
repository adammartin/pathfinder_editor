import pytest
from editor.character.alignment_info import AlignmentInfo


def test_alignment():
    alignment_info = AlignmentInfo(pytest.helpers.main_alignment(0, 0))
    assert alignment_info.alignment() == 'Neutral'


def test_update_alignment():
    alignment_block = pytest.helpers.main_alignment(0, 0)
    alignment_info = AlignmentInfo(alignment_block)
    new_alignment = 'Neutral Good'
    alignment_info.update_alignment(new_alignment)
    assert alignment_info.alignment() == new_alignment
    assert alignment_block['Vector']['x'] == 0
    assert alignment_block['Vector']['y'] == 1
    assert alignment_block['m_History'][-1]['Position']['x'] == 0
    assert alignment_block['m_History'][-1]['Position']['y'] == 1

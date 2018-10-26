import pytest
from unittest import mock
from unittest.mock import patch, MagicMock
from editor.character.character_info import CharacterInfo
from editor.character import stat_info


MAIN_CHAR_ID = '1'
COMPANION_ID = '77c11edb92ce0fd408ad96b40fd27121'
COMP_UNIT_ID = '420'
MONEY = 1000
MAIN_KEY = {
    'm_UniqueId': MAIN_CHAR_ID
}

def main_character(party):
    return party['m_EntityData'][0]

def alignment_data(character):
    return character['Descriptor']['Alignment']

def stats_data(character):
    return character['Descriptor']['Stats']

def test_name():
    party = pytest.helpers.party_base(MAIN_CHAR_ID, COMP_UNIT_ID, COMPANION_ID)
    character = CharacterInfo(party, MAIN_KEY)
    assert character.name() == main_character(party)['Descriptor']['CustomName']


def test_alignment():
    party = pytest.helpers.party_base(MAIN_CHAR_ID, COMP_UNIT_ID, COMPANION_ID)
    character = CharacterInfo(party, MAIN_KEY)
    assert character.alignment() == 'Neutral'


def test_update_alignment():
    party = pytest.helpers.party_base(MAIN_CHAR_ID, COMP_UNIT_ID, COMPANION_ID)
    character = CharacterInfo(party, MAIN_KEY)
    new_alignment = 'Neutral Good'
    character.update_alignment(new_alignment)
    assert character.alignment() == new_alignment
    assert alignment_data(main_character(party))['Vector']['x'] == 0
    assert alignment_data(main_character(party))['Vector']['y'] == 1
    assert alignment_data(main_character(party))['m_History'][-1]['Position']['x'] == 0
    assert alignment_data(main_character(party))['m_History'][-1]['Position']['y'] == 1


@patch('editor.character.stat_info.StatInfo')
def test_strength(mock_stat_info):
    strength = '50'
    mock_stat_info.return_value.strength.return_value = strength
    party = pytest.helpers.party_base(MAIN_CHAR_ID, COMP_UNIT_ID, COMPANION_ID)
    character = CharacterInfo(party, MAIN_KEY)
    assert character.strength() == strength


@patch('editor.character.stat_info.StatInfo')
def test_update_strength(mock_stat_info):
    party = pytest.helpers.party_base(MAIN_CHAR_ID, COMP_UNIT_ID, COMPANION_ID)
    character = CharacterInfo(party, MAIN_KEY)
    new_strength = '1000'
    character.update_strength(new_strength)
    mock_stat_info.return_value.update_strength.assert_called_with(new_strength)


@patch('editor.character.stat_info.StatInfo')
def test_dexterity(mock_stat_info):
    dexterity = '29'
    mock_stat_info.return_value.dexterity.return_value = dexterity
    party = pytest.helpers.party_base(MAIN_CHAR_ID, COMP_UNIT_ID, COMPANION_ID)
    character = CharacterInfo(party, MAIN_KEY)
    assert character.dexterity() == dexterity


@patch('editor.character.stat_info.StatInfo')
def test_update_dexterity(mock_stat_info):
    party = pytest.helpers.party_base(MAIN_CHAR_ID, COMP_UNIT_ID, COMPANION_ID)
    character = CharacterInfo(party, MAIN_KEY)
    new_dexterity = '247'
    character.update_dexterity(new_dexterity)
    mock_stat_info.return_value.update_dexterity.assert_called_with(new_dexterity)

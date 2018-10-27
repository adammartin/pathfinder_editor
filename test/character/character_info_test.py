import pytest
from unittest import mock
from unittest.mock import patch
from editor.character.character_info import CharacterInfo
from editor.character import stat_info, alignment_info, skills_info


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


def test_experience():
    party = pytest.helpers.party_base(MAIN_CHAR_ID, COMP_UNIT_ID, COMPANION_ID)
    progression = main_character(party)['Descriptor']['Progression']
    character = CharacterInfo(party, MAIN_KEY)
    assert character.experience() == str(progression['Experience'])


def test_update_experience():
    party = pytest.helpers.party_base(MAIN_CHAR_ID, COMP_UNIT_ID, COMPANION_ID)
    progression = main_character(party)['Descriptor']['Progression']
    character = CharacterInfo(party, MAIN_KEY)
    new_experience = str(int(character.experience())+1000)
    character.update_experience(new_experience)
    assert character.experience() == new_experience
    assert character.experience() == str(progression['Experience'])


@patch('editor.character.stat_info.StatInfo')
def test_stats_info(mock_stat_info):
    party = pytest.helpers.party_base(MAIN_CHAR_ID, COMP_UNIT_ID, COMPANION_ID)
    character = CharacterInfo(party, MAIN_KEY)
    mock_stat_info.assert_called_with(stats_data(main_character(party)))
    assert character.stats == mock_stat_info.return_value


@patch('editor.character.alignment_info.AlignmentInfo')
def test_alignment_info(mock_alignment_info):
    party = pytest.helpers.party_base(MAIN_CHAR_ID, COMP_UNIT_ID, COMPANION_ID)
    character = CharacterInfo(party, MAIN_KEY)
    mock_alignment_info.assert_called_with(alignment_data(main_character(party)))
    assert character.alignment == mock_alignment_info.return_value


@patch('editor.character.skills_info.SkillsInfo')
def test_skills_info(mock_skills_info):
    party = pytest.helpers.party_base(MAIN_CHAR_ID, COMP_UNIT_ID, COMPANION_ID)
    character = CharacterInfo(party, MAIN_KEY)
    mock_skills_info.assert_called_with(stats_data(main_character(party)))
    assert character.skills == mock_skills_info.return_value

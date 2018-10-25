import json
import pytest
from editor.character.character_info import CharacterInfo


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

def test_strength():
    party = pytest.helpers.party_base(MAIN_CHAR_ID, COMP_UNIT_ID, COMPANION_ID)
    stats = stats_data(main_character(party))
    strength = stats['SkillAthletics']['BaseStat']['m_BaseValue']
    character = CharacterInfo(party, MAIN_KEY)
    assert character.strength() == str(strength)

def test_update_strength():
    party = pytest.helpers.party_base(MAIN_CHAR_ID, COMP_UNIT_ID, COMPANION_ID)
    stats = stats_data(main_character(party))
    character = CharacterInfo(party, MAIN_KEY)
    new_strength = str(int(character.strength()) + 6)
    character.update_strength(new_strength)
    assert character.strength() == str(new_strength)
    assert character.strength() == str(stats['SkillAthletics']['BaseStat']['m_BaseValue'])


def test_dexterity():
    party = pytest.helpers.party_base(MAIN_CHAR_ID, COMP_UNIT_ID, COMPANION_ID)
    stats = stats_data(main_character(party))
    dexterity = stats['Dexterity']['m_BaseValue']
    character = CharacterInfo(party, MAIN_KEY)
    assert character.dexterity() == str(dexterity)

def test_update_dexterity():
    party = pytest.helpers.party_base(MAIN_CHAR_ID, COMP_UNIT_ID, COMPANION_ID)
    stats = stats_data(main_character(party))
    character = CharacterInfo(party, MAIN_KEY)
    new_dexterity = str(int(character.dexterity()) + 6)
    character.update_dexterity(new_dexterity)
    assert character.dexterity() == str(new_dexterity)
    assert character.dexterity() == str(stats['Dexterity']['m_BaseValue'])

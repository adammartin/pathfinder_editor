import pytest
from unittest import mock
from unittest.mock import patch, call
from editor.character.party_info import PartyInfo
from editor.character.file_utils import load_json
from editor.character.character_info import CharacterInfo


PARTY_JSON = 'party.json'
PLAYER_JSON = 'player.json'
HEADER_JSON = 'header.json'
PATH = mock.Mock()
MAIN_CHAR_ID = '1'
COMPANION_ID = '77c11edb92ce0fd408ad96b40fd27121'
COMP_UNIT_ID = '420'
MONEY = 1000
MAIN_KEY = {
    'm_UniqueId': MAIN_CHAR_ID
}
MAIN_DATA = pytest.helpers.player_base(MONEY, MAIN_CHAR_ID)
PARTY = pytest.helpers.party_base(MAIN_CHAR_ID, COMP_UNIT_ID, COMPANION_ID)
HEADER = pytest.helpers.header()


def reset_data():
    MAIN_DATA = pytest.helpers.player_base(MONEY, MAIN_CHAR_ID)
    PARTY = pytest.helpers.party_base(MAIN_CHAR_ID, COMP_UNIT_ID, COMPANION_ID)


def fake_loader(path, file):
    if path == PATH and file == PARTY_JSON:
        return PARTY
    elif path == PATH and file == PLAYER_JSON:
        return MAIN_DATA
    elif path == PATH and file == HEADER_JSON:
        return HEADER
    else:
        return None


def main_character(party):
    return party['m_EntityData'][0]


@pytest.yield_fixture(autouse=True)
def run_around_tests():
    reset_data()
    yield
    reset_data()


@patch('editor.character.file_utils.load_json')
def test_money(load_json_mock):
    load_json_mock.side_effect = fake_loader
    party_info = PartyInfo(PATH)
    assert party_info.money() == str(MONEY)


@patch('editor.character.file_utils.load_json')
def test_update_money(load_json_mock):
    load_json_mock.side_effect = fake_loader
    new_money = MONEY * 3
    party_info = PartyInfo(PATH)
    party_info.update_money(new_money)
    assert party_info.money() == str(new_money)
    assert MAIN_DATA['Money'] == new_money


@patch('editor.character.file_utils.load_json')
def test_main_character(load_json_mock):
    load_json_mock.side_effect = fake_loader
    character_name = main_character(PARTY)['Descriptor']['CustomName']
    party_info = PartyInfo(PATH)
    assert isinstance(party_info.main_character, CharacterInfo)
    assert party_info.main_character.name() == character_name


@patch('editor.character.file_utils.load_json')
def test_skills_info(load_json_mock):
    load_json_mock.side_effect = fake_loader
    party_info = PartyInfo(PATH)
    assert party_info.kingdom.has_kingdom_data()


@patch('editor.character.file_utils.save_json')
@patch('editor.character.file_utils.load_json')
def test_save_edits_header_name(load_json_mock, save_json_mock):
    load_json_mock.side_effect = fake_loader
    character_name = main_character(PARTY)['Descriptor']['CustomName']
    party_info = PartyInfo(PATH)
    expected_save_name = 'Edited - ' + HEADER['Name']
    party_info.save()
    assert HEADER['Name'] == expected_save_name



@patch('editor.character.file_utils.save_json')
@patch('editor.character.file_utils.load_json')
def test_save_data(load_json_mock, save_json_mock):
    load_json_mock.side_effect = fake_loader
    character_name = main_character(PARTY)['Descriptor']['CustomName']
    party_info = PartyInfo(PATH)
    party_info.save()
    expected_calls = [call(PATH, PLAYER_JSON, MAIN_DATA),
                      call(PATH, PARTY_JSON, PARTY),
                      call(PATH, HEADER_JSON, HEADER)]
    save_json_mock.assert_has_calls(expected_calls)

import pytest
from unittest import mock
from unittest.mock import patch
from editor.character.party_info import PartyInfo
from editor.character.file_utils import load_json


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


def fake_loader(path, file):
    if path == PATH and file == PARTY_JSON:
        return PARTY
    elif path == PATH and file == PLAYER_JSON:
        return MAIN_DATA
    else:
        return None


@patch('editor.character.file_utils.load_json')
def test_money(load_json_mock):
    load_json_mock.side_effect = fake_loader
    party_info = PartyInfo(PATH)
    assert party_info.money() == str(MONEY)

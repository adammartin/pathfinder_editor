import json
import pytest
from editor.character.character_info import CharacterInfo


MAIN_CHAR_ID = '1'
COMPANION_ID = '77c11edb92ce0fd408ad96b40fd27121'
COMP_UNIT_ID = '420'
MONEY = 1000
KEY = {
    'm_UniqueId': MAIN_CHAR_ID
}


def test_name():
    party_json = pytest.helpers.party_base(MAIN_CHAR_ID, COMP_UNIT_ID, COMPANION_ID)
    companion = pytest.helpers.companion(COMP_UNIT_ID, COMPANION_ID)
    main_character = pytest.helpers.main_character(MAIN_CHAR_ID, companion)
    character = CharacterInfo(party_json, KEY)
    assert character.name() == main_character['Descriptor']['CustomName']

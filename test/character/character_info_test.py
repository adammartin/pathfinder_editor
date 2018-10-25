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

def test_main_character():
    def test_name():
        party = pytest.helpers.party_base(MAIN_CHAR_ID, COMP_UNIT_ID, COMPANION_ID)
        main_character = party['m_EntityData'][0]
        character = CharacterInfo(party, MAIN_KEY)
        assert character.name() == main_character['Descriptor']['CustomName']


    def test_alignment():
        party = pytest.helpers.party_base(MAIN_CHAR_ID, COMP_UNIT_ID, COMPANION_ID)
        character = CharacterInfo(party, MAIN_KEY)
        assert character.alignment() == 'Neutral'


    def test_update_alignment():
        party = pytest.helpers.party_base(MAIN_CHAR_ID, COMP_UNIT_ID, COMPANION_ID)
        character = CharacterInfo(party, MAIN_KEY)
        main_character = party['m_EntityData'][0]
        new_alignment = 'Neutral Good'
        character.update_alignment(new_alignment)
        alignment_data = main_character['Descriptor']['Alignment']
        assert character.alignment() == new_alignment
        assert alignment_data['Vector']['x'] == 0
        assert alignment_data['Vector']['y'] == 1
        assert alignment_data['m_History'][-1]['Position']['x'] == 0
        assert alignment_data['m_History'][-1]['Position']['y'] == 1

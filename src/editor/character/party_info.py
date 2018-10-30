from editor.character import file_utils
from editor.character.character_info import CharacterInfo
from editor.character.companion_info import CompanionInfo
from editor.character.kingdom_info import KingdomInfo


PARTY_JSON_NAME = 'party.json'
PLAYER_JSON_NAME = 'player.json'
HEADER_JSON_NAME = 'header.json'


class PartyInfo:
    # pylint: disable=too-many-instance-attributes
    def __init__(self, path):
        self._temp_path = path
        self._party = file_utils.load_json(path, PARTY_JSON_NAME)
        self._main = file_utils.load_json(path, PLAYER_JSON_NAME)
        self.main_character = CharacterInfo(self._party,
                                            self._main['m_MainCharacter'])
        self.companions = _load_companions(self._party)
        self.kingdom = KingdomInfo(self._main)

    def money(self):
        return str(self._main['Money'])

    def update_money(self, money):
        if self._main['Money'] != int(money):
            self._main['Money'] = int(money)

    def save(self):
        header = file_utils.load_json(self._temp_path, HEADER_JSON_NAME)
        header['Name'] = 'Edited - ' + header['Name']
        file_utils.save_json(self._temp_path,
                             PLAYER_JSON_NAME,
                             self._main)
        file_utils.save_json(self._temp_path,
                             PARTY_JSON_NAME,
                             self._party)
        file_utils.save_json(self._temp_path,
                             HEADER_JSON_NAME,
                             header)


def _load_companions(party):
    companions = []
    for entity in party['m_EntityData']:
        if '$ref' in entity:
            companion = CompanionInfo(party, entity)
            if companion.name():
                companions.append(companion)
    return companions

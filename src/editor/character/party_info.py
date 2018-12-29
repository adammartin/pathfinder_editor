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
        self.members = {}
        self._add(CharacterInfo(self._party, self._main['m_MainCharacter']))
        self._load_companions()
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

    def _add(self, character):
        self.members[character.name()] = character

    def _load_companions(self):
        for entity in self._party['m_EntityData']:
            if '$ref' in entity:
                try:
                    companion = CompanionInfo(self._party, entity)
                    self._add(companion)
                except TypeError:
                    pass
            elif '$id' in entity:
                try:
                    key = {'$ref': entity['$id']}
                    companion = CompanionInfo(self._party, key)
                    self._add(companion)
                except TypeError:
                    pass

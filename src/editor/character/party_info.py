from editor.character import file_utils
from editor.character.character_info import CharacterInfo


class PartyInfo:
    def __init__(self, path):
        self._temp_path = path
        self._party_json_name = 'party.json'
        self._player_json_name = 'player.json'
        self._header_json_name = 'header.json'
        self._party = file_utils.load_json(path, self._party_json_name)
        self._main =  file_utils.load_json(path, self._player_json_name)
        self.main_character = CharacterInfo(self._party,
                                            self._main['m_MainCharacter'])

    def money(self):
        return str(self._main['Money'])


    def update_money(self, money):
        if self._main['Money'] != int(money):
            self._main['Money'] = int(money)

    def save(self):
        header = file_utils.load_json(self._temp_path, self._header_json_name)
        header['Name'] = 'Edited - ' + header['Name']
        file_utils.save_json(self._temp_path,
                             self._player_json_name,
                             self._main)
        file_utils.save_json(self._temp_path,
                             self._party_json_name,
                             self._party)
        file_utils.save_json(self._temp_path,
                             self._header_json_name,
                             header)

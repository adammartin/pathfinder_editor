from editor.character import file_utils


class PartyInfo:
    def __init__(self, path):
        self._temp_path = path
        self._party_json_name = 'party.json'
        self._player_json_name = 'player.json'
        self._header_json_name = 'header.json'
        self._party = file_utils.load_json(path, self._party_json_name)
        self._main =  file_utils.load_json(path, self._player_json_name)

    def money(self):
        return str(self._main['Money'])

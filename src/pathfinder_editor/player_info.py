from file_utils import load_json, save_json



class PlayerInfo:
    def __init__(self, path):
        self._temp_path = path
        self._player_json_name = 'player.json'
        self._header_json_name = 'header.json'

    def money(self):
        return str(self._json(self._player_json_name)["Money"])

    def update_money(self, money):
        player_json = self._json(self._player_json_name)
        player_json['Money'] = int(money)
        save_json(self._temp_path, self._player_json_name, player_json)

    def update_header_name(self):
        header_json = self._json(self._header_json_name)
        header_json["Name"] = "EDITED - " + header_json["Name"]
        save_json(self._temp_path, 'header.json', header_json)

    def _json(self, json_file_name):
        return load_json(self._temp_path, json_file_name)

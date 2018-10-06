from file_utils import load_json, save_json



class PlayerInfo:
    def __init__(self, path):
        self._temp_path = path
        self._party_json_name = "party.json"
        self._player_json_name = 'player.json'
        self._header_json_name = 'header.json'

    def money(self):
        return str(self._json(self._player_json_name)["Money"])

    def name(self):
        return self._main_character()["CustomName"]

    def strength(self):
        strength_container = self._main_character_stats()["Strength"]
        if "PermanentValue" in strength_container:
            return str(strength_container["PermanentValue"])
        return "Unknown"

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

    def _main_character(self):
        return self._json(self._party_json_name)["m_EntityData"][0]["Descriptor"]

    def _main_character_stats(self):
        return self._main_character()["Stats"]

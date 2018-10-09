from file_utils import load_json


class EntityInfo:
    # pylint: disable=too-few-public-methods
    def __init__(self, path):
        self._temp_path = path
        self._party_json_name = "party.json"
        self._player_json_name = 'player.json'
        self._header_json_name = 'header.json'

    def _json(self, json_file_name):
        return load_json(self._temp_path, json_file_name)


def main_character(data):
    return data["m_EntityData"][0]["Descriptor"]


def main_character_stats(data):
    return main_character(data)["Stats"]

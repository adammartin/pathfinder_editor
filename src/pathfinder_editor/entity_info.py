from file_utils import load_json


class EntityInfo:
    # pylint: disable=too-few-public-methods
    def __init__(self, path):
        self._temp_path = path
        self._party_json_name = "party.json"
        self._player_json_name = 'player.json'
        self._header_json_name = 'header.json'
        self.main_character_id = self._main_character_id()

    def _json(self, json_file_name):
        return load_json(self._temp_path, json_file_name)

    def _main_character_id(self):
        json = self._json(self._player_json_name)
        return json['m_MainCharacter']['m_UniqueId']

    def main_character(self, data):
        for entity in data['m_EntityData']:
            if has_unique_id(entity, self.main_character_id):
                return entity['Descriptor']
        return None

    def main_character_stats(self, data):
        return self.main_character(data)["Stats"]


def has_unique_id(entity, unique_id):
    return 'UniqueId' in entity and entity['UniqueId'] == unique_id

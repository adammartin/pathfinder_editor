from file_utils import load_json


class EntityInfo:
    # pylint: disable=too-few-public-methods
    def __init__(self, path):
        self._temp_path = path
        self._party_json_name = 'party.json'
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
                return search_for_player(entity)
        return None

    def main_character_stats(self, data):
        return search_for_stats(self.main_character(data))


def has_unique_id(entity, unique_id):
    return 'UniqueId' in entity and entity['UniqueId'] == unique_id

def search_for_player(entity):
    descriptor = entity['Descriptor']
    if 'Stats' in descriptor:
        return descriptor
    ref = descriptor['$ref']
    return search_for_caster(entity, ref)

def search_for_caster(entity, ref):
    if caster_ref_matches(entity['m_AutoUseAbility'], ref):
        return entity['m_AutoUseAbility']['Caster']
    return None

def caster_ref_matches(ability, ref):
    return is_caster(ability) and ability['Caster']['$id'] == ref

def is_caster(ability):
    return 'Caster' in ability and '$id' in ability['Caster']

def search_for_stats(player):
    stats = player['Stats']
    if '$id' in stats:
        return stats
    else:
        return search_for_stats_in_inventory(player)

def search_for_stats_in_inventory(player):
    ref = player['Stats']['$ref']
    for item in player['m_Inventory']['m_Items']:
        for child in item.values():
            result = recursive_search(child, ref)
            if id_matches(result, ref):
                return result
    return None

def recursive_search(child, ref):
    if not isinstance(child, dict):
        return None
    elif id_matches(child, ref):
        return child
    else:
        for value in child.values():
            result = recursive_search(value, ref)
            if id_matches(result, ref):
                return result
    return None

def id_matches(entity, ref):
    return entity != None and '$id' in entity and entity['$id'] == ref

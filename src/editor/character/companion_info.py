from editor.character.entity_info import EntityInfo
from editor.character.search_algorithms import search_recursively


class CompanionInfo(EntityInfo):
    def _find_character(self):
        return search_recursively(self._party_data, self._key, _key_matches)


def _key_matches(data, key):
    try:
        return 'Unit' in data and (data['Unit'] == key
                                   or _matches_by_ref(data['Unit'], key))
    except TypeError:
        return False


def _matches_by_ref(unit, key):
    return '$id' in unit and unit['$id'] == key['$ref']

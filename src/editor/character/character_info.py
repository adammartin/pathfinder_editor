from editor.character.entity_info import EntityInfo
from editor.character.search_algorithms import id_matches, search_recursively


class CharacterInfo(EntityInfo):
    def _find_character(self):
        for entity in self._party_data['m_EntityData']:
            if _has_unique_id(entity, self._key['m_UniqueId']):
                return _search_for_player(entity)
        return None


def _has_unique_id(entity, unique_id):
    return 'UniqueId' in entity and entity['UniqueId'] == unique_id


def _search_for_player(entity):
    if 'Stats' in entity['Descriptor']:
        return entity['Descriptor']
    ref = entity['Descriptor']['$ref']
    return search_recursively(entity, ref, id_matches)

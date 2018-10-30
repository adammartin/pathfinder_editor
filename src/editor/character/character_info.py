from editor.character import stat_info, alignment_info, skills_info
from editor.character.search_algorithms import id_matches, search_recursively


class CharacterInfo():
    # pylint: disable=too-few-public-methods
    def __init__(self, party_data, key):
        self._party_data = party_data
        self._key = key
        self.stats = stat_info.StatInfo(self._main_character_stats())
        self.alignment = alignment_info.AlignmentInfo(self._alignment_block())
        self.skills = skills_info.SkillsInfo(self._main_character_stats())

    def name(self):
        return self._main_character()['CustomName']

    def experience(self):
        return str(self._main_character()['Progression']['Experience'])

    def update_experience(self, value):
        if int(self.experience()) != int(value):
            self._main_character()['Progression']['Experience'] = int(value)

    def _main_character(self):
        for entity in self._party_data['m_EntityData']:
            if _has_unique_id(entity, self._key['m_UniqueId']):
                return _search_for_player(entity)
        return None

    def _main_character_stats(self):
        return _search_for_stats(self._main_character())

    def _alignment_block(self):
        return self._main_character()['Alignment']


def _has_unique_id(entity, unique_id):
    return 'UniqueId' in entity and entity['UniqueId'] == unique_id


def _search_for_player(entity):
    if 'Stats' in entity['Descriptor']:
        return entity['Descriptor']
    ref = entity['Descriptor']['$ref']
    return search_recursively(entity, ref, id_matches)


def _search_for_stats(player):
    stats = player['Stats']
    if '$id' in stats:
        return stats
    ref = player['Stats']['$ref']
    return search_recursively(player, ref, id_matches)

from editor.character import stat_info, alignment_info, skills_info


class CharacterInfo():
    # pylint: disable=too-few-public-methods
    def __init__(self, party_data, key):
        self._party_data = party_data
        self._key = key
        self.stats_info = stat_info.StatInfo(self._main_character_stats())
        self.align_info = alignment_info.AlignmentInfo(self._alignment_block())
        self.skills_info = skills_info.SkillsInfo(self._main_character_stats())

    def name(self):
        return self._main_character()['CustomName']

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
    descriptor = entity['Descriptor']
    if 'Stats' in descriptor:
        return descriptor
    ref = descriptor['$ref']
    return _search_for_caster(entity, ref)


def _search_for_caster(entity, ref):
    if caster_ref_matches(entity['m_AutoUseAbility'], ref):
        return entity['m_AutoUseAbility']['Caster']
    return None


def _caster_ref_matches(ability, ref):
    return _is_caster(ability) and ability['Caster']['$id'] == ref


def _is_caster(ability):
    return 'Caster' in ability and '$id' in ability['Caster']


def _search_for_stats(player):
    stats = player['Stats']
    if '$id' in stats:
        return stats
    return _search_for_stats_in_inventory(player)


def _search_for_stats_in_inventory(player):
    ref = player['Stats']['$ref']
    for item in player['m_Inventory']['m_Items']:
        for child in item.values():
            result = _recursive_search(child, ref)
            if _id_matches(result, ref):
                return result
    return None


def _recursive_search(child, ref):
    if not isinstance(child, dict):
        return None
    elif _id_matches(child, ref):
        return child
    else:
        for value in child.values():
            result = _recursive_search(value, ref)
            if _id_matches(result, ref):
                return result
    return None


def _id_matches(entity, ref):
    return entity is not None and '$id' in entity and entity['$id'] == ref

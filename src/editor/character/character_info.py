class CharacterInfo():
    # pylint: disable=too-few-public-methods
    def __init__(self, party_data, key):
        self.party_data = party_data
        self.key = key

    def name(self):
        return self._main_character()['CustomName']

    def _main_character(self):
        for entity in self.party_data['m_EntityData']:
            if has_unique_id(entity, self.key['m_UniqueId']):
                return search_for_player(entity)
        return None


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
    return entity is not None and '$id' in entity and entity['$id'] == ref

import math
from editor.character import stat_info


ALIGNMENTS = {
    'Neutral': {'x': 0, 'y': 0, 'angle_min': 0, 'angle_max': 0, 'radius': 0.4},
    'Chaotic Good': {'x': 0.707106769, 'y': 0.707106769,
                     'angle_min': 0, 'angle_max': 45},
    'Neutral Good': {'x': 0, 'y': 1, 'angle_min': 45, 'angle_max': 90},
    'Lawful Good': {'x': -0.707106769, 'y': 0.707106769,
                    'angle_min': 90, 'angle_max': 135},
    'Lawful Neutral': {'x': -1, 'y': 0, 'angle_min': 135, 'angle_max': 180},
    'Lawful Evil': {'x': -0.707106769, 'y': -0.707106769,
                    'angle_min': 180, 'angle_max': 225},
    'Neutral Evil': {'x': 0, 'y': -1, 'angle_min': 225, 'angle_max': 270},
    'Chaotic Evil': {'x': 0.707106769, 'y': -0.707106769,
                     'angle_min': 270, 'angle_max': 315},
    'Chaotic Neutral': {'x': 1, 'y': 0, 'angle_min': 315, 'angle_max': 360},
}


class CharacterInfo():
    # pylint: disable=too-few-public-methods
    def __init__(self, party_data, key):
        self.party_data = party_data
        self.key = key
        self.stats = stat_info.StatInfo(self._main_character_stats())

    def name(self):
        return self._main_character()['CustomName']

    def alignment(self):
        descriptor = self._main_character()
        x_axis = descriptor['Alignment']['Vector']['x']
        y_axis = descriptor['Alignment']['Vector']['y']
        return _calculate_alignment(x_axis, y_axis)

    def strength(self):
        return self.stats.strength()

    def dexterity(self):
        return self.stats.dexterity()

    def update_alignment(self, value):
        if value != self.alignment():
            vector = ALIGNMENTS[value]
            descriptor = self._main_character()
            descriptor['Alignment']['Vector'] = vector
            descriptor['Alignment']['m_History'][-1]['Position'] = vector

    def update_strength(self, value):
        self.stats.update_strength(value)

    def update_dexterity(self, value):
        self.stats.update_dexterity(value)

    def _main_character(self):
        for entity in self.party_data['m_EntityData']:
            if _has_unique_id(entity, self.key['m_UniqueId']):
                return _search_for_player(entity)
        return None

    def _main_character_stats(self):
        return _search_for_stats(self._main_character())


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


def _calculate_angle(x_axis, y_axis):
    # CCW Angle starting east
    angle = (math.atan2(y_axis, x_axis) * 180 / math.pi) - 22.5
    if angle < 0:
        angle += 360
    return angle


def _calculate_alignment(x_axis, y_axis):
    angle = _calculate_angle(x_axis, y_axis)
    radius = math.sqrt(x_axis * x_axis + y_axis * y_axis)
    for align, data in ALIGNMENTS.items():
        if 'radius' in data and radius <= data['radius']:
            return align
        elif angle >= data['angle_min'] and angle < data['angle_max']:
            return align
    return 'UNKOWN'

import math


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

    def name(self):
        return self._main_character()['CustomName']

    def alignment(self):
        descriptor = self._main_character()
        x_axis = descriptor['Alignment']['Vector']['x']
        y_axis = descriptor['Alignment']['Vector']['y']
        return calculate_alignment(x_axis, y_axis)

    def update_alignment(self, value):
        if value != self.alignment():
            vector = ALIGNMENTS[value]
            descriptor = self._main_character()
            descriptor['Alignment']['Vector'] = vector
            descriptor['Alignment']['m_History'][-1]['Position'] = vector

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


def calculate_angle(x_axis, y_axis):
    # CCW Angle starting east
    angle = (math.atan2(y_axis, x_axis) * 180 / math.pi) - 22.5
    if angle < 0:
        angle += 360
    return angle


def calculate_alignment(x_axis, y_axis):
    angle = calculate_angle(x_axis, y_axis)
    radius = math.sqrt(x_axis * x_axis + y_axis * y_axis)
    for align, data in ALIGNMENTS.items():
        if 'radius' in data and radius <= data['radius']:
            return align
        elif angle >= data['angle_min'] and angle < data['angle_max']:
            return align
    return 'UNKOWN'

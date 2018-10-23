import math
from character.entity_info import EntityInfo
from file_utils import save_json


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


class PlayerInfo(EntityInfo):
    # pylint: disable=too-many-public-methods
    def money(self):
        return str(self._json(self._player_json_name)['Money'])

    def name(self):
        data = self._json(self._party_json_name)
        return self.main_character(data)['CustomName']

    def experience(self):
        data = self._json(self._party_json_name)
        return str(self.main_character(data)['Progression']['Experience'])

    def strength(self):
        return self._load_attribute_value('Strength')

    def dexterity(self):
        return self._load_attribute_value('Dexterity')

    def constitution(self):
        return self._load_attribute_value('Constitution')

    def intelligence(self):
        return self._load_attribute_value('Intelligence')

    def wisdom(self):
        return self._load_attribute_value('Wisdom')

    def charisma(self):
        return self._load_attribute_value('Charisma')

    def alignment(self):
        data = self._json(self._party_json_name)
        descriptor = self.main_character(data)
        x_axis = descriptor['Alignment']['Vector']['x']
        y_axis = descriptor['Alignment']['Vector']['y']
        return calculate_alignment(x_axis, y_axis)

    def update_money(self, money):
        player_json = self._json(self._player_json_name)
        if player_json['Money'] != int(money):
            player_json['Money'] = int(money)
            save_json(self._temp_path, self._player_json_name, player_json)

    def update_strength(self, value):
        self._update_attribute_value('Strength', value)

    def update_experience(self, value):
        if int(self.experience()) != value:
            data = self._json(self._party_json_name)
            self.main_character(data)['Progression']['Experience'] = int(value)
            save_json(self._temp_path, self._party_json_name, data)

    def update_dexterity(self, value):
        self._update_attribute_value('Dexterity', value)

    def update_constitution(self, value):
        self._update_attribute_value('Constitution', value)

    def update_intelligence(self, value):
        self._update_attribute_value('Intelligence', value)

    def update_wisdom(self, value):
        self._update_attribute_value('Wisdom', value)

    def update_charisma(self, value):
        self._update_attribute_value('Charisma', value)

    def update_alignment(self, value):
        if value != self.alignment():
            vector = ALIGNMENTS[value]
            data = self._json(self._party_json_name)
            descriptor = self.main_character(data)
            descriptor['Alignment']['Vector'] = vector
            descriptor['Alignment']['m_History'][-1]['Position'] = vector
            save_json(self._temp_path, self._party_json_name, data)

    def update_header_name(self):
        header_json = self._json(self._header_json_name)
        header_json['Name'] = 'EDITED - ' + header_json['Name']
        save_json(self._temp_path, self._header_json_name, header_json)

    def _load_attribute_value(self, attribute_name):
        data = self._json(self._party_json_name)
        stats = self.main_character_stats(data)
        attribute = stats[attribute_name]
        if 'm_BaseValue' in attribute:
            return str(attribute['m_BaseValue'])
        return _load_attribute_ref(attribute['$ref'], stats)

    def _update_attribute_value(self, attribute_name, value):
        data = self._json(self._party_json_name)
        stats = self.main_character_stats(data)
        attribute = stats[attribute_name]
        if self._load_attribute_value(attribute_name) != int(value):
            if 'm_BaseValue' in attribute:
                attribute['m_BaseValue'] = int(value)
            else:
                _update_attribute_ref(attribute['$ref'], stats, value)
            save_json(self._temp_path, self._party_json_name, data)


def _load_attribute_ref(ref, stats):
    for stat, struct in stats.items():
        if 'BaseStat' in struct:
            if struct['BaseStat']['$id'] == ref:
                return str(stats[stat]['BaseStat']['m_BaseValue'])
    return 'UNKOWN'


def _update_attribute_ref(ref, stats, value):
    for stat, struct in stats.items():
        if 'BaseStat' in struct:
            if struct['BaseStat']['$id'] == ref:
                stats[stat]['BaseStat']['m_BaseValue'] = int(value)

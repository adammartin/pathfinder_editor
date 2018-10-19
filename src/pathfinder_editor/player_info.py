from entity_info import EntityInfo
from file_utils import save_json
import math


class PlayerInfo(EntityInfo):
    # pylint: disable=too-many-public-methods
    def money(self):
        return str(self._json(self._player_json_name)["Money"])

    def name(self):
        data = self._json(self._party_json_name)
        return self.main_character(data)["CustomName"]

    def experience(self):
        data = self._json(self._party_json_name)
        return str(self.main_character(data)["Progression"]["Experience"])

    def strength(self):
        return self._load_attribute_value("Strength")

    def dexterity(self):
        return self._load_attribute_value("Dexterity")

    def constitution(self):
        return self._load_attribute_value("Constitution")

    def intelligence(self):
        return self._load_attribute_value("Intelligence")

    def wisdom(self):
        return self._load_attribute_value("Wisdom")

    def charisma(self):
        return self._load_attribute_value("Charisma")

    def alignment(self):
        data = self._json(self._party_json_name)
        descriptor = self.main_character(data)
        x = descriptor['Alignment']['Vector']['x']
        y = descriptor['Alignment']['Vector']['y']
        angle = math.atan2(y, x) * 180 / math.pi #CCW Angle starting east
        if angle < 0:
             angle += 360
        angle -= 22.5 #let 0-45 equal chaotic good and -22.5-0 and 315-337.5 equal Chaotic Neutral
        radius = math.sqrt(x * x + y * y)
        if radius <= 0.4:
            return "Neutral"
        if angle >= 0 and angle < 45:
             return "Chaotic Good"
        if angle >= 45 and angle < 90:
            return "Neutral Good"
        if angle >= 90 and angle < 135:
             return "Lawful Good"
        if angle >= 135 and angle < 180:
             return "Lawful Netural"
        if angle >= 180 and angle < 225:
             return "Lawful Evil"
        if angle >= 225 and angle < 270:
             return "Netural Evil"
        if angle >= 270 and angle < 315:
             return "Chaotic Evil"
        return "Chaotic Neutral"

    def update_money(self, money):
        player_json = self._json(self._player_json_name)
        if player_json['Money'] != int(money):
            player_json['Money'] = int(money)
            save_json(self._temp_path, self._player_json_name, player_json)

    def update_strength(self, value):
        self._update_attribute_value("Strength", value)

    def update_experience(self, value):
        if int(self.experience()) != value:
            data = self._json(self._party_json_name)
            self.main_character(data)["Progression"]["Experience"] = int(value)
            save_json(self._temp_path, self._party_json_name, data)

    def update_dexterity(self, value):
        self._update_attribute_value("Dexterity", value)

    def update_constitution(self, value):
        self._update_attribute_value("Constitution", value)

    def update_intelligence(self, value):
        self._update_attribute_value("Intelligence", value)

    def update_wisdom(self, value):
        self._update_attribute_value("Wisdom", value)

    def update_charisma(self, value):
        self._update_attribute_value("Charisma", value)

    def update_alignment(self, value):
        alignments = {
            "Neutral" : {"x" : 0, "y": 0},
            "Chaotic Good" : {"x" : 0.707106769, "y": 0.707106769},
            "Neutral Good" : {"x" : 0, "y": 1},
            "Lawful Good" : {"x" : -0.707106769, "y": 0.707106769},
            "Lawful Neutral" : {"x" : -1, "y": 0},
            "Lawful Evil" : {"x" : -0.707106769, "y": -0.707106769},
            "Neutral Evil" : {"x" : 0, "y": -1},
            "Chaotic Evil" : {"x" : 0.707106769, "y": -0.707106769},
            "Chaotic Neutral" : {"x" : 1, "y": 0},
        }
        if not value in alignments:
            return
        vector = alignments[value]
        data = self._json(self._party_json_name)
        descriptor = self.main_character(data)
        descriptor['Alignment']['Vector'] = vector
        descriptor['Alignment']['m_History'][-1]['Position'] = vector
        save_json(self._temp_path, self._party_json_name, data)

    def update_header_name(self):
        header_json = self._json(self._header_json_name)
        header_json["Name"] = "EDITED - " + header_json["Name"]
        save_json(self._temp_path, self._header_json_name, header_json)

    def _load_attribute_value(self, attribute_name):
        data = self._json(self._party_json_name)
        stats = self.main_character_stats(data)
        attribute = stats[attribute_name]
        if "m_BaseValue" in attribute:
            return str(attribute["m_BaseValue"])
        return _load_attribute_ref(attribute["$ref"], stats)

    def _update_attribute_value(self, attribute_name, value):
        data = self._json(self._party_json_name)
        stats = self.main_character_stats(data)
        attribute = stats[attribute_name]
        if self._load_attribute_value(attribute_name) != int(value):
            if "m_BaseValue" in attribute:
                attribute["m_BaseValue"] = int(value)
            else:
                _update_attribute_ref(attribute["$ref"], stats, value)
            save_json(self._temp_path, self._party_json_name, data)


def _load_attribute_ref(ref, stats):
    for stat, struct in stats.items():
        if "BaseStat" in struct:
            if struct["BaseStat"]["$id"] == ref:
                return str(stats[stat]["BaseStat"]["m_BaseValue"])
    return "Unknown"


def _update_attribute_ref(ref, stats, value):
    for stat, struct in stats.items():
        if "BaseStat" in struct:
            if struct["BaseStat"]["$id"] == ref:
                stats[stat]["BaseStat"]["m_BaseValue"] = int(value)

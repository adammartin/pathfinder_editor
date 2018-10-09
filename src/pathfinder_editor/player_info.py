from entity_info import EntityInfo, main_character, main_character_stats
from file_utils import save_json


class PlayerInfo(EntityInfo):
    # pylint: disable=too-many-public-methods
    def money(self):
        return str(self._json(self._player_json_name)["Money"])

    def name(self):
        data = self._json(self._party_json_name)
        return main_character(data)["CustomName"]

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

    def update_money(self, money):
        player_json = self._json(self._player_json_name)
        if player_json['Money'] != int(money):
            player_json['Money'] = int(money)
            save_json(self._temp_path, self._player_json_name, player_json)

    def update_strength(self, value):
        self._update_attribute_value("Strength", value)

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

    def update_header_name(self):
        header_json = self._json(self._header_json_name)
        header_json["Name"] = "EDITED - " + header_json["Name"]
        save_json(self._temp_path, self._header_json_name, header_json)

    def _load_attribute_value(self, attribute_name):
        data = self._json(self._party_json_name)
        stats = main_character_stats(data)
        attribute = stats[attribute_name]
        if "m_BaseValue" in attribute:
            return str(attribute["m_BaseValue"])
        return _load_attribute_ref(attribute["$ref"], stats)

    def _update_attribute_value(self, attribute_name, value):
        data = self._json(self._party_json_name)
        stats = main_character_stats(data)
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

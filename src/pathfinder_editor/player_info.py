from file_utils import load_json, save_json


class PlayerInfo:
    def __init__(self, path):
        self._temp_path = path
        self._party_json_name = "party.json"
        self._player_json_name = 'player.json'
        self._header_json_name = 'header.json'

    def money(self):
        return str(self._json(self._player_json_name)["Money"])

    def name(self):
        data = self._json(self._party_json_name)
        return _main_character(data)["CustomName"]

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

    def _json(self, json_file_name):
        return load_json(self._temp_path, json_file_name)

    def _load_attribute_value(self, attribute_name):
        data = self._json(self._party_json_name)
        stats = _main_character_stats(data)
        attribute = stats[attribute_name]
        if "PermanentValue" in attribute:
            return str(attribute["m_BaseValue"])
        return _load_attribute_ref(attribute["$ref"], stats)

    def _update_attribute_value(self, attribute_name, value):
        data = self._json(self._party_json_name)
        stats = _main_character_stats(data)
        attribute = stats[attribute_name]
        if "PermanentValue" in attribute:
            attribute["m_BaseValue"] = int(value)
        else:
            _update_attribute_ref(attribute["$ref"], stats, value)
        save_json(self._temp_path, self._party_json_name, data)


def _main_character(data):
    return data["m_EntityData"][0]["Descriptor"]


def _main_character_stats(data):
    return _main_character(data)["Stats"]


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

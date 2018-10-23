from character.entity_info import EntityInfo
from character.file_utils import save_json


class KingdomInfo(EntityInfo):
    # pylint: disable=too-many-public-methods
    def has_kingdom_data(self):
        data = self._data()
        return 'Kingdom' in data and _kingdom(data) is not None

    def build_points(self):
        return self._load_attribute_value('BP')

    def kingdom_name(self):
        return self._load_attribute_value('KingdomName')

    def community(self):
        return self._load_stat_value('Community')

    def loyalty(self):
        return self._load_stat_value('Loyalty')

    def military(self):
        return self._load_stat_value('Military')

    def economy(self):
        return self._load_stat_value('Economy')

    def relations(self):
        return self._load_stat_value('Relations')

    def divine(self):
        return self._load_stat_value('Divine')

    def arcane(self):
        return self._load_stat_value('Arcane')

    def stability(self):
        return self._load_stat_value('Stability')

    def culture(self):
        return self._load_stat_value('Culture')

    def espionage(self):
        return self._load_stat_value('Espionage')

    def update_build_points(self, value):
        self._update_attribute('BP', int(value))

    def update_kingdom_name(self, value):
        self._update_attribute('KingdomName', value)

    def update_community(self, value):
        return self._update_stat('Community', value)

    def update_loyalty(self, value):
        return self._update_stat('Loyalty', value)

    def update_military(self, value):
        return self._update_stat('Military', value)

    def update_economy(self, value):
        return self._update_stat('Economy', value)

    def update_relations(self, value):
        return self._update_stat('Relations', value)

    def update_divine(self, value):
        return self._update_stat('Divine', value)

    def update_arcane(self, value):
        return self._update_stat('Arcane', value)

    def update_stability(self, value):
        return self._update_stat('Stability', value)

    def update_culture(self, value):
        return self._update_stat('Culture', value)

    def update_espionage(self, value):
        return self._update_stat('Espionage', value)

    def _load_stat_value(self, stat):
        if self.has_kingdom_data():
            stats = _kingdom_stats(_kingdom(self._data()))
            stat_block = _load_stat_block(stats, stat)
            return str(stat_block['Value'])
        return 'No Kingdom'

    def _load_attribute_value(self, attribute):
        if self.has_kingdom_data():
            return str(_kingdom(self._data())[attribute])
        return 'No Kingdom'

    def _update_attribute(self, attribute, value):
        data = self._data()
        if self.has_kingdom_data() and _kingdom(data)[attribute] != value:
            _kingdom(data)[attribute] = value
            self._save(data)

    def _update_stat(self, stat, value):
        data = self._data()
        if self.has_kingdom_data() and self._load_stat_value(stat) != value:
            stats = _kingdom_stats(_kingdom(data))
            _load_stat_block(stats, stat)['Value'] = int(value)
            self._save(data)

    def _data(self):
        return self._json(self._player_json_name)

    def _save(self, data):
        save_json(self._temp_path, self._player_json_name, data)


def _kingdom(data):
    return data['Kingdom']


def _kingdom_stats(kingdom):
    return kingdom['Stats']['m_Stats']


def _load_stat_block(stats, stat):
    return next(block for block in stats if block['Type'] == stat)

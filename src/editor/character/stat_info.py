class StatInfo():
    def __init__(self, stat_block):
        self._stat_block = stat_block

    def strength(self):
        return self._load_attribute_value('Strength')

    def update_strength(self, value):
        return self._update_attribute_value('Strength', value)

    def dexterity(self):
        return self._load_attribute_value('Dexterity')

    def update_dexterity(self, value):
        self._update_attribute_value('Dexterity', value)

    def constitution(self):
        return self._load_attribute_value('Constitution')

    def update_constitution(self, value):
        self._update_attribute_value('Constitution', value)

    def _load_attribute_value(self, attribute_name):
        attribute = self._stat_block[attribute_name]
        if 'm_BaseValue' in attribute:
            return str(attribute['m_BaseValue'])
        return _load_attribute_ref(attribute['$ref'], self._stat_block)

    def _update_attribute_value(self, attribute_name, value):
        attribute = self._stat_block[attribute_name]
        if self._load_attribute_value(attribute_name) != int(value):
            if 'm_BaseValue' in attribute:
                attribute['m_BaseValue'] = int(value)
            else:
                _update_attribute_ref(attribute['$ref'], self._stat_block, value)


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

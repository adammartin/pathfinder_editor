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

    def intelligence(self):
        return self._load_attribute_value('Intelligence')

    def update_intelligence(self, value):
        self._update_attribute_value('Intelligence', value)

    def wisdom(self):
        return self._load_attribute_value('Wisdom')

    def update_wisdom(self, value):
        self._update_attribute_value('Wisdom', value)

    def charisma(self):
        return self._load_attribute_value('Charisma')

    def update_charisma(self, value):
        self._update_attribute_value('Charisma', value)

    def base_ac(self):
        return self._load_attribute_value('AC')

    def update_base_ac(self, value):
        self._update_attribute_value('AC', value)

    def add_attack_bonus(self):
        return self._load_attribute_value('AdditionalAttackBonus')

    def update_add_attack_bonus(self, value):
        self._update_attribute_value('AdditionalAttackBonus', value)

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
                _update_attribute_ref(attribute['$ref'],
                                      self._stat_block,
                                      value)


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

from editor.widgets.tabs.tab import Tab
from editor.character.alignment_info import ALIGNMENTS


class PlayerInfoTab(Tab):
    # pylint: disable=too-many-instance-attributes, too-few-public-methods
    def __init__(self, notebook):
        super(PlayerInfoTab, self).__init__(notebook)
        func = self._update_info
        self._money = self._add_field(0, 0, 'Money:', func)
        self._experience = self._add_field(0, 1, 'Experience:', func)
        self._alignment = self._add_dropdown(1, 0, 'Alignment:',
                                             ALIGNMENTS.keys(), func)
        self._portrait = self._add_field(1, 1, 'Portrait', func)
        self._strength = self._add_field(2, 0, 'Strength:', func)
        self._dexterity = self._add_field(2, 1, 'Dexterity:', func)
        self._constitution = self._add_field(3, 0, 'Constitution:', func)
        self._intelligence = self._add_field(3, 1, 'Intelligence:', func)
        self._wisdom = self._add_field(4, 0, 'Wisdom:', func)
        self._charisma = self._add_field(4, 1, 'Charisma:', func)
        self._character = None
        self._party = None
        self._expand()

    def load_info(self, party, character):
        self._character = character
        self._party = party
        self._dirty_lock = True
        self._money.set(party.money())
        self._experience.set(character.experience())
        self._alignment.set(character.alignment.alignment())
        self._strength.set(character.stats.strength())
        self._dexterity.set(character.stats.dexterity())
        self._constitution.set(character.stats.constitution())
        self._intelligence.set(character.stats.intelligence())
        self._wisdom.set(character.stats.wisdom())
        self._charisma.set(character.stats.charisma())
        self._portrait.set(character.portrait())
        self._dirty_lock = False

    def _update_info(self, *args):
        # pylint: disable=unused-argument
        alignment = self._character.alignment
        stats = self._character.stats
        self._update(self._money, self._party.update_money)
        self._update(self._experience, self._character.update_experience)
        self._update(self._alignment, alignment.update_alignment)
        self._update(self._strength, stats.update_strength)
        self._update(self._dexterity, stats.update_dexterity)
        self._update(self._constitution, stats.update_constitution)
        self._update(self._intelligence, stats.update_intelligence)
        self._update(self._wisdom, stats.update_wisdom)
        self._update(self._charisma, stats.update_charisma)
        self._update(self._portrait, self._character.update_portrait)

    def _expand(self):
        self._notebook.add(self._panel, text="Player")
        self._panel.config()

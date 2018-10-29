from editor.widgets.tabs.tab import Tab
from editor.character.alignment_info import ALIGNMENTS


class PlayerInfoTab(Tab):
    # pylint: disable=too-many-instance-attributes
    def __init__(self, notebook):
        super(PlayerInfoTab, self).__init__(notebook)
        self._money = self._add_field(0, 0, 'Money:')
        self._experience = self._add_field(0, 1, 'Experience:')
        self._alignment = self._add_dropdown(1, 0, 'Alignment:',
                                             ALIGNMENTS.keys())
        self._strength = self._add_field(2, 0, 'Strength:')
        self._dexterity = self._add_field(2, 1, 'Dexterity:')
        self._constitution = self._add_field(3, 0, 'Constitution:')
        self._intelligence = self._add_field(3, 1, 'Intelligence:')
        self._wisdom = self._add_field(4, 0, 'Wisdom:')
        self._charisma = self._add_field(4, 1, 'Charisma:')

    def load_info(self, party):
        self._money.set(party.money())
        character = party.main_character
        self._experience.set(character.experience())
        self._alignment.set(character.alignment.alignment())
        self._strength.set(character.stats.strength())
        self._dexterity.set(character.stats.dexterity())
        self._constitution.set(character.stats.constitution())
        self._intelligence.set(character.stats.intelligence())
        self._wisdom.set(character.stats.wisdom())
        self._charisma.set(character.stats.charisma())
        self._notebook.add(self._panel, text="Player")
        self._panel.config()

    def update_info(self, party):
        character = party.main_character
        party.update_money(self._money.get())
        character.update_experience(self._experience.get())
        character.alignment.update_alignment(self._alignment.get())
        character.stats.update_strength(self._strength.get())
        character.stats.update_dexterity(self._dexterity.get())
        character.stats.update_constitution(self._constitution.get())
        character.stats.update_intelligence(self._intelligence.get())
        character.stats.update_wisdom(self._wisdom.get())
        character.stats.update_charisma(self._charisma.get())

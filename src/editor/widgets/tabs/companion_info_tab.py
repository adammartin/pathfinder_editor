from editor.widgets.tabs.tab import Tab
from editor.character.alignment_info import ALIGNMENTS


class CompanionInfoTab(Tab):
    # pylint: disable=too-many-instance-attributes
    def __init__(self, notebook):
        super(CompanionInfoTab, self).__init__(notebook)
        self._experience = self._add_field(0, 0, 'Experience:')
        self._alignment = self._add_dropdown(0, 1, 'Alignment:',
                                             ALIGNMENTS.keys())
        self._strength = self._add_field(1, 0, 'Strength:')
        self._dexterity = self._add_field(1, 1, 'Dexterity:')
        self._constitution = self._add_field(2, 0, 'Constitution:')
        self._intelligence = self._add_field(2, 1, 'Intelligence:')
        self._wisdom = self._add_field(3, 0, 'Wisdom:')
        self._charisma = self._add_field(3, 1, 'Charisma:')

    def load_info(self, companion):
        self._experience.set(companion.experience())
        self._alignment.set(companion.alignment.alignment())
        self._strength.set(companion.stats.strength())
        self._dexterity.set(companion.stats.dexterity())
        self._constitution.set(companion.stats.constitution())
        self._intelligence.set(companion.stats.intelligence())
        self._wisdom.set(companion.stats.wisdom())
        self._charisma.set(companion.stats.charisma())
        self._notebook.add(self._panel, text="Stats")
        self._panel.config()

    def update_info(self, companion):
        companion.update_experience(self._experience.get())
        companion.alignment.update_alignment(self._alignment.get())
        companion.stats.update_strength(self._strength.get())
        companion.stats.update_dexterity(self._dexterity.get())
        companion.stats.update_constitution(self._constitution.get())
        companion.stats.update_intelligence(self._intelligence.get())
        companion.stats.update_wisdom(self._wisdom.get())
        companion.stats.update_charisma(self._charisma.get())

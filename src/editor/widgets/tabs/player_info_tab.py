from editor.widgets.tabs.tab import Tab
from editor.widgets.fields.field import GridField
from editor.widgets.fields.field import GridOptionMenu
from editor.widgets.fields.field import GridPortraitMenu
from editor.character.alignment_info import ALIGNMENTS
from editor.character.file_utils import list_portrait_dirs


STATS = [
    {'label': 'Strength', 'position': [2, 0], 'getter': 'strength',
     'setter': 'update_strength'},
    {'label': 'Dexterity', 'position': [2, 1], 'getter': 'dexterity',
     'setter': 'update_dexterity'},
    {'label': 'Constitution', 'position': [3, 0], 'getter': 'constitution',
     'setter': 'update_constitution'},
    {'label': 'Intelligence', 'position': [3, 1], 'getter': 'intelligence',
     'setter': 'update_intelligence'},
    {'label': 'Wisdom', 'position': [4, 0], 'getter': 'wisdom',
     'setter': 'update_wisdom'},
    {'label': 'Charisma', 'position': [4, 1], 'getter': 'charisma',
     'setter': 'update_charisma'},
    {'label': 'Base AC', 'position': [0, 2], 'getter': 'base_ac',
     'setter': 'update_base_ac'},
    {'label': 'Attack Bonus', 'position': [1, 2], 'getter': 'add_attack_bonus',
     'setter': 'update_add_attack_bonus'},
    {'label': 'Additional CMB', 'position': [2, 2], 'getter': 'additional_cmb',
     'setter': 'update_additional_cmb'},
    {'label': 'Additional CMD', 'position': [3, 2], 'getter': 'additional_cmd',
     'setter': 'update_additional_cmd'},
    {'label': 'Additional DMG', 'position': [4, 2], 'getter': 'additional_dmg',
     'setter': 'update_additional_dmg'},
    {'label': 'Hit Points', 'position': [5, 2], 'getter': 'hit_points',
     'setter': 'update_hit_points'},
    {'label': 'Speed', 'position': [6, 2], 'getter': 'speed', 'setter':
     'update_speed'}
]


class PlayerInfoTab(Tab):
    # pylint: disable=too-many-instance-attributes, too-few-public-methods
    def __init__(self, notebook):
        super(PlayerInfoTab, self).__init__(notebook)
        func = self._update_info
        self._stat_fields = []
        self._money = GridField(self._panel, 0, 0, 'Money:', func)
        self._experience = GridField(self._panel, 0, 1, 'Experience:', func)
        self._alignment = GridOptionMenu(self._panel, 1, 0, 'Alignment:',
                                         ALIGNMENTS.keys(), func)
        self._instantiate_stats()
        self._portrait = None
        self._character = None
        self._party = None
        self._portraits = None
        self._expand()

    def load_info(self, party, character, save_dir):
        self._character = character
        self._party = party
        self._portraits = list_portrait_dirs(save_dir)
        self._portrait = GridPortraitMenu(self._panel, 1, 1, 'Portrait',
                                          self._portraits,
                                          self._update_info)
        self._dirty_lock = True
        self._set_fields(party, character)
        self._dirty_lock = False

    def _set_fields(self, party, character):
        self._money.set(party.money())
        self._experience.set(character.experience())
        self._alignment.set(character.alignment.alignment())
        self._portrait.set(character.portrait())
        for stat_field in self._stat_fields:
            _set_field(stat_field, character.stats)

    def _instantiate_stats(self):
        for stat in STATS:
            self._stat_fields.append(
                {
                    'field': GridField(self._panel,
                                       stat['position'][0],
                                       stat['position'][1],
                                       stat['label'],
                                       self._update_stats),
                    'getter': stat['getter'],
                    'setter': stat['setter']
                }
            )

    def _update_stats(self, *args):
        # pylint: disable=unused-argument
        print(args)
        stats = self._character.stats
        for stat_field in self._stat_fields:
            self._update_stat(stat_field, stats)

    def _update_stat(self, field, stats):
        field['field'].update(getattr(stats, field['setter']),
                              self._dirty_lock)

    def _update_info(self, *args):
        # pylint: disable=unused-argument
        alignment = self._character.alignment
        self._money.update(self._party.update_money, self._dirty_lock)
        self._experience.update(self._character.update_experience,
                                self._dirty_lock)
        self._alignment.update(alignment.update_alignment, self._dirty_lock)
        self._portrait.update(self._character.update_portrait,
                              self._dirty_lock)

    def _expand(self):
        self._notebook.add(self._panel, text="Player")
        self._panel.config()


def _set_field(field, stats):
    value = getattr(stats, field['getter'])()
    field['field'].set(value)

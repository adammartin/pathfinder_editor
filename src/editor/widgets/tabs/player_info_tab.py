from editor.widgets.tabs.tab import Tab
from editor.character.alignment_info import ALIGNMENTS
from editor.character.file_utils import list_portrait_dirs


class PlayerInfoTab(Tab):
    # pylint: disable=too-many-instance-attributes, too-few-public-methods
    def __init__(self, notebook):
        super(PlayerInfoTab, self).__init__(notebook)
        func = self._update_info
        self._money = self._add_field(0, 0, 'Money:', func)
        self._experience = self._add_field(0, 1, 'Experience:', func)
        self._alignment = self._add_dropdown(1, 0, 'Alignment:',
                                             ALIGNMENTS.keys(), func)
        self._portrait = None
        self._strength = self._add_field(2, 0, 'Strength:', func)
        self._dexterity = self._add_field(2, 1, 'Dexterity:', func)
        self._constitution = self._add_field(3, 0, 'Constitution:', func)
        self._intelligence = self._add_field(3, 1, 'Intelligence:', func)
        self._wisdom = self._add_field(4, 0, 'Wisdom:', func)
        self._charisma = self._add_field(4, 1, 'Charisma:', func)
        self._base_ac = self._add_field(0, 2, 'Base AC', func)
        self._add_attack_bonus = self._add_field(1, 2, 'Attack Bonus', func)
        self._additional_cmb = self._add_field(2, 2, 'Additional CMB', func)
        self._additional_cmd = self._add_field(3, 2, 'Additional CMD', func)
        self._additional_dmg = self._add_field(4, 2, 'Additional DMG', func)
        self._hit_points = self._add_field(5, 2, 'Hit Points', func)
        self._speed = self._add_field(6, 2, 'Speed', func)
        self._character = None
        self._party = None
        self._portraits = None
        self._expand()

    def load_info(self, party, character, save_dir):
        self._character = character
        self._party = party
        self._portraits = list_portrait_dirs(save_dir)
        self._dirty_lock = True
        self._set_fields(party, character)
        self._dirty_lock = False

    def _set_fields(self, party, character):
        self._money.set(party.money())
        self._experience.set(character.experience())
        self._alignment.set(character.alignment.alignment())
        self._strength.set(character.stats.strength())
        self._dexterity.set(character.stats.dexterity())
        self._constitution.set(character.stats.constitution())
        self._intelligence.set(character.stats.intelligence())
        self._wisdom.set(character.stats.wisdom())
        self._charisma.set(character.stats.charisma())
        self._base_ac.set(character.stats.base_ac())
        self._add_attack_bonus.set(character.stats.add_attack_bonus())
        self._additional_cmb.set(character.stats.additional_cmb())
        self._additional_cmd.set(character.stats.additional_cmd())
        self._additional_dmg.set(character.stats.additional_dmg())
        self._hit_points.set(character.stats.hit_points())
        self._speed.set(character.stats.speed())
        if self._portraits:
            self._add_portrait_dropdown(character)

    def _add_portrait_dropdown(self, character):
        self._portrait = self._add_dropdown(1, 1, 'Portrait',
                                            self._portraits,
                                            self._update_info)
        self._portrait.set(character.portrait())

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
        if self._has_custom_portraits() and self._portrait_exists():
            self._update(self._portrait, self._character.update_portrait)
        self._update(self._base_ac, stats.update_base_ac)
        self._update(self._add_attack_bonus, stats.update_add_attack_bonus)
        self._update(self._additional_cmb, stats.update_additional_cmb)
        self._update(self._additional_cmd, stats.update_additional_cmd)
        self._update(self._additional_dmg, stats.update_additional_dmg)
        self._update(self._hit_points, stats.update_hit_points)
        self._update(self._speed, stats.update_speed)

    def _has_custom_portraits(self):
        return self._portraits and self._portrait

    def _portrait_exists(self):
        return self._portrait.get() in self._portraits

    def _expand(self):
        self._notebook.add(self._panel, text="Player")
        self._panel.config()

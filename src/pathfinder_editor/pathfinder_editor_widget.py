import time
from pathlib import Path
from shutil import rmtree
from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlFile
from pyforms.controls import ControlButton
from pyforms.controls import ControlLabel
from file_utils import extract_file, persist_as_zip
from player_info import PlayerInfo
from skill_info import SkillInfo
from kingdom_info import KingdomInfo


class PathfinderEditorWidget(BaseWidget):
    # pylint: disable=too-many-instance-attributes
    def __init__(self, *args, **kwargs):
        super().__init__('Python editor for Pathfinder: Kingmaker')
        self._savefile = ControlFile('Save File')
        self._loadbutton = ControlButton('Load')
        self._name_field = ControlLabel('Name:')
        self._name_value = ControlLabel('')
        self._savebutton = ControlButton('Save')
        self._temp_path = Path('./tempdir/')
        # main_stats
        self._money_field = ControlText('Money')
        self._experience_field = ControlText('Experience')
        self._strength_field = ControlText('Strength')
        self._dexterity_field = ControlText('Dexterity')
        self._constitution_field = ControlText('Constitution')
        self._intelligence_field = ControlText('Intelligence')
        self._wisdom_field = ControlText('Wisdom')
        self._charisma_field = ControlText('Charisma')
        # skills
        self._athletics_field = ControlText('Athletics')
        self._arcana_field = ControlText('Knowledge Arcana')
        self._knowledge_world_field = ControlText('Knowledge World')
        self._lore_nature_field = ControlText('Lore Nature')
        self._lore_religion_field = ControlText('Lore Religion')
        self._mobility_field = ControlText('Mobility')
        self._perception_field = ControlText('Perception')
        self._persuasion_field = ControlText('Persuasion')
        self._stealth_field = ControlText('Stealth')
        self._theivery_field = ControlText('Theivery')
        self._use_magic_device_field = ControlText('Use Magic Device')
        # kingdom
        self._build_points_field = ControlText('Build Points')
        self._formset = _formset()

        self._loadbutton.value = self.__load_save_file
        self._savebutton.value = self.__update_save
        self.__clean_temp_storage()

    def before_close_event(self):
        self.__clean_temp_storage()

    def __clean_temp_storage(self):
        if self._temp_path.exists():
            rmtree(self._temp_path)

    def __load_save_file(self):
        extract_file(Path(self._savefile.value), self._temp_path)
        self.__load_player_info()
        self.__load_skill_info()
        self.__load_kingdom_info()

    def __load_player_info(self):
        player_info = PlayerInfo(self._temp_path)
        self._name_value.value = player_info.name()
        self._money_field.value = player_info.money()
        self._experience_field.value = player_info.experience()
        self._strength_field.value = player_info.strength()
        self._dexterity_field.value = player_info.dexterity()
        self._constitution_field.value = player_info.constitution()
        self._intelligence_field.value = player_info.intelligence()
        self._wisdom_field.value = player_info.wisdom()
        self._charisma_field.value = player_info.charisma()

    def __load_skill_info(self):
        skill_info = SkillInfo(self._temp_path)
        self._athletics_field.value = skill_info.athletics()
        self._arcana_field.value = skill_info.knowledge_arcana()
        self._knowledge_world_field.value = skill_info.knowledge_world()
        self._mobility_field.value = skill_info.mobility()
        self._lore_nature_field.value = skill_info.lore_nature()
        self._lore_religion_field.value = skill_info.lore_religion()
        self._perception_field.value = skill_info.perception()
        self._persuasion_field.value = skill_info.persuasion()
        self._stealth_field.value = skill_info.stealth()
        self._theivery_field.value = skill_info.theivery()
        self._use_magic_device_field.value = skill_info.use_magic_device()

    def __load_kingdom_info(self):
        kingdom_info = KingdomInfo(self._temp_path)
        if kingdom_info.has_kingdom_data():
            self._build_points_field.value = kingdom_info.build_points()
        else:
            self._build_points_field.hide()

    def __update_save(self):
        self.__update_player_info()
        self.__update_skill_info()
        self.__update_kingdom_info()

        save_root = Path(self._savefile.value).parent
        save_file = str(int(round(time.time() * 1000))) + ".zks"

        persist_as_zip(save_root, save_file, self._temp_path)
        self.__clean_temp_storage()

    def __update_player_info(self):
        player_info = PlayerInfo(self._temp_path)
        player_info.update_money(self._money_field.value)
        player_info.update_experience(self._experience_field.value)
        player_info.update_header_name()
        player_info.update_strength(self._strength_field.value)
        player_info.update_dexterity(self._dexterity_field.value)
        player_info.update_constitution(self._constitution_field.value)
        player_info.update_intelligence(self._intelligence_field.value)
        player_info.update_wisdom(self._wisdom_field.value)
        player_info.update_charisma(self._charisma_field.value)

    def __update_skill_info(self):
        skill_info = SkillInfo(self._temp_path)
        skill_info.update_athletics(self._athletics_field.value)
        skill_info.update_knowledge_arcana(self._arcana_field.value)
        skill_info.update_knowledge_world(self._knowledge_world_field.value)
        skill_info.update_mobility(self._mobility_field.value)
        skill_info.update_lore_nature(self._lore_nature_field.value)
        skill_info.update_lore_religion(self._lore_religion_field.value)
        skill_info.update_perception(self._perception_field.value)
        skill_info.update_persuasion(self._persuasion_field.value)
        skill_info.update_stealth(self._stealth_field.value)
        skill_info.update_theivery(self._theivery_field.value)
        skill_info.update_use_magic_device(self._use_magic_device_field.value)

    def __update_kingdom_info(self):
        kingdom_info = KingdomInfo(self._temp_path)
        if kingdom_info.has_kingdom_data():
            kingdom_info.update_build_points(self._build_points_field.value)


def _main_stats():
    return [('_money_field', '_experience_field'),
            ('_strength_field', '_dexterity_field', '_constitution_field'),
            ('_intelligence_field', '_wisdom_field', '_charisma_field')]


def _skills():
    return [('_athletics_field', '_arcana_field', '_knowledge_world_field'),
            ('_mobility_field', '_lore_nature_field', '_lore_religion_field'),
            ('_perception_field', '_persuasion_field'),
            ('_stealth_field', '_theivery_field', '_use_magic_device_field')]


def _kingdom():
    return [('_build_points_field')]


def _formset():
    return ['_savefile',
            '_loadbutton',
            ('_name_field', '_name_value'),
            {'1 Main Stats': _main_stats(),
             '2 Skills': _skills(),
             '3 Kingdom': _kingdom()},
            '_savebutton']

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


class PathfinderEditorWidget(BaseWidget):
    # pylint: disable=too-many-instance-attributes
    def __init__(self, *args, **kwargs):
        super().__init__('Python editor for Pathfinder: Kingmaker')
        self._savefile = ControlFile('Save File')
        self._loadbutton = ControlButton('Load')
        self._name_field = ControlLabel('Name:')
        self._name_value = ControlLabel('')
        self._money_field = ControlText('Money')
        self._experience_field = ControlText('Experience')
        self._strength_field = ControlText('Strength')
        self._dexterity_field = ControlText('Dexterity')
        self._constitution_field = ControlText('Constitution')
        self._intelligence_field = ControlText('Intelligence')
        self._wisdom_field = ControlText('Wisdom')
        self._charisma_field = ControlText('Charisma')
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
        self._savebutton = ControlButton('Save')
        self._temp_path = Path('./tempdir/')

        main_stats = [
            ('_money_field', '_experience_field'),
            ('_strength_field', '_dexterity_field', '_constitution_field'),
            ('_intelligence_field', '_wisdom_field', '_charisma_field')
        ]
        skills = [
            ('_athletics_field', '_arcana_field', '_knowledge_world_field'),
            ('_mobility_field', '_lore_nature_field', '_lore_religion_field'),
            ('_perception_field', '_persuasion_field'),
            ('_stealth_field', '_theivery_field', '_use_magic_device_field')
        ]

        self._formset = [
            '_savefile',
            '_loadbutton',
            ('_name_field', '_name_value'),
            {'Main Stats': main_stats,
             'Skills': skills},
            '_savebutton'
        ]

        self._loadbutton.value = self.__load_save_file
        self._savebutton.value = self.__update_save

    def __load_save_file(self):
        extract_file(Path(self._savefile.value), self._temp_path)
        player_info = PlayerInfo(self._temp_path)
        skill_info = SkillInfo(self._temp_path)
        self._name_value.value = player_info.name()
        self._money_field.value = player_info.money()
        self._experience_field.value = player_info.experience()
        self._strength_field.value = player_info.strength()
        self._dexterity_field.value = player_info.dexterity()
        self._constitution_field.value = player_info.constitution()
        self._intelligence_field.value = player_info.intelligence()
        self._wisdom_field.value = player_info.wisdom()
        self._charisma_field.value = player_info.charisma()
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

    def __update_save(self):
        player_info = PlayerInfo(self._temp_path)
        skill_info = SkillInfo(self._temp_path)
        player_info.update_money(self._money_field.value)
        player_info.update_experience(self._experience_field.value)
        player_info.update_header_name()
        player_info.update_strength(self._strength_field.value)
        player_info.update_dexterity(self._dexterity_field.value)
        player_info.update_constitution(self._constitution_field.value)
        player_info.update_intelligence(self._intelligence_field.value)
        player_info.update_wisdom(self._wisdom_field.value)
        player_info.update_charisma(self._charisma_field.value)
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

        save_root = Path(self._savefile.value).parent
        save_file = str(int(round(time.time() * 1000))) + ".zks"

        persist_as_zip(save_root, save_file, self._temp_path)
        rmtree(self._temp_path)

    def before_close_event(self):
        if self._temp_path.exists():
            rmtree(self._temp_path)

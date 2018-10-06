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


class PathfinderEditorWidget(BaseWidget):
    def __init__(self, *args, **kwargs):
        super().__init__('Python editor for Pathfinder: Kingmaker')
        self._savefile = ControlFile('Save File')
        self._loadbutton = ControlButton('Load')
        self._name_field = ControlLabel('Name:')
        self._name_value = ControlLabel('')
        self._money_field = ControlText('Money')
        self._strength_field = ControlText('Strength')
        self._dexterity_field = ControlText('Dexterity')
        self._constitution_field = ControlText('Constitution')
        self._intelligence_field = ControlText('Intelligence')
        self._wisdom_field = ControlText('Wisdom')
        self._charisma_field = ControlText('Charisma')
        self._savebutton = ControlButton('Save')
        self._temp_path = Path('./tempdir/')

        self._formset = [
            '_savefile',
            '_loadbutton',
            ('_name_field', '_name_value'),
            ('_money_field'),
            ('_strength_field', '_dexterity_field', '_constitution_field'),
            ('_intelligence_field', '_wisdom_field', '_charisma_field'),
            '_savebutton',
        ]

        self._loadbutton.value = self.__load_save_file
        self._savebutton.value = self.__update_save

    def __load_save_file(self):
        extract_file(Path(self._savefile.value), self._temp_path)
        player_info = PlayerInfo(self._temp_path)
        self._name_value.value = player_info.name()
        self._money_field.value = player_info.money()
        self._strength_field.value = player_info.strength()
        self._dexterity_field.value = player_info.dexterity()
        self._constitution_field.value = player_info.constitution()
        self._intelligence_field.value = player_info.intelligence()
        self._wisdom_field.value = player_info.wisdom()
        self._charisma_field.value = player_info.charisma()

    def __update_save(self):
        player_info = PlayerInfo(self._temp_path)
        player_info.update_money(self._money_field.value)
        player_info.update_header_name()
        player_info.update_strength(self._strength_field.value)
        player_info.update_dexterity(self._dexterity_field.value)
        player_info.update_constitution(self._constitution_field.value)
        player_info.update_intelligence(self._intelligence_field.value)
        player_info.update_wisdom(self._wisdom_field.value)
        player_info.update_charisma(self._charisma_field.value)

        save_root = Path(self._savefile.value).parent
        save_file = str(int(round(time.time() * 1000))) + ".zks"

        persist_as_zip(save_root, save_file, self._temp_path)
        rmtree(self._temp_path)

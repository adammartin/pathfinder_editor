import time
from pathlib import Path
from shutil import rmtree
from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlFile
from pyforms.controls import ControlButton
from file_utils import extract_file, persist_as_zip
from player_info import PlayerInfo


class PathfinderEditorWidget(BaseWidget):
    def __init__(self, *args, **kwargs):
        super().__init__('Python editor for Pathfinder: Kingmaker')
        self._savefile = ControlFile('Save File')
        self._loadbutton = ControlButton('Load')
        self._name_field = ControlText('Name')
        self._money_field = ControlText('Money')
        self._savebutton = ControlButton('Save')
        self._temp_path = Path('./tempdir/')

        self._formset = [
            '_savefile',
            '_loadbutton',
            ('_name_field', '_money_field'),
            '_savebutton',
        ]

        self._loadbutton.value = self.__load_save_file
        self._savebutton.value = self.__update_save

    def __load_save_file(self):
        extract_file(Path(self._savefile.value), self._temp_path)
        self._name_field.value = PlayerInfo(self._temp_path).name()
        self._money_field.value = PlayerInfo(self._temp_path).money()

    def __update_save(self):
        player_info = PlayerInfo(self._temp_path)
        player_info.update_money(self._money_field.value)
        player_info.update_header_name()

        save_root = Path(self._savefile.value).parent
        save_file = str(int(round(time.time() * 1000))) + ".zks"

        persist_as_zip(save_root, save_file, self._temp_path)
        rmtree(self._temp_path)

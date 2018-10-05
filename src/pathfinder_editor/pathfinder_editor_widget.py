from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlFile
from pyforms.controls import ControlButton
from file_utils import extract_file, full_path, load_json, save_json, persist_as_zip
from pathlib import Path
from shutil import rmtree
import time

class PathfinderEditorWidget(BaseWidget):
    def __init__(self, *args, **kwargs):
        super().__init__('Python editor for Pathfinder: Kingmaker')
        self._savefile = ControlFile('Save File')
        self._loadbutton = ControlButton('Load')
        self._money_field = ControlText('Money')
        self._savebutton = ControlButton('Save')
        self._temp_path = Path('./tempdir/')

        self._formset = [
            '_savefile',
            '_loadbutton',
            '_money_field',
            '_savebutton',
        ]

        self._loadbutton.value = self.__load_save_file
        self._savebutton.value = self.__update_save

    def __load_save_file(self):
        try:
            extract_file(Path(self._savefile.value), self._temp_path)
            player_json = load_json(self._temp_path, 'player.json')
            self._money_field.value = str(player_json['Money'])
        except Exception as e:
            print(e)

    def __update_save(self):
        try:
            money = int(self._money_field.value)
            player_json = load_json(self._temp_path, 'player.json')
            player_json['Money'] = int(self._money_field.value)
            save_json(self._temp_path, 'player.json', player_json)

            header_json = load_json(self._temp_path, 'header.json')
            header_json["Name"] = "EDITED - " + header_json["Name"]
            save_json(self._temp_path, 'header.json', header_json)

            save_root = Path(self._savefile.value).parent
            save_file = str(int(round(time.time() * 1000))) + ".zks"

            persist_as_zip(save_root, save_file, self._temp_path)
            rmtree(self._temp_path)
        except Exception as e:
            print(e)

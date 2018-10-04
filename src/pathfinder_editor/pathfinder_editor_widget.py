from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlFile
from pyforms.controls import ControlButton
from pathlib import Path
from zipfile import ZipFile
import json, io

def extract_file(path, temp_dir_path):
    if path.is_file():
        with ZipFile(str(path.resolve()), 'r') as save_zip:
            save_zip.extractall(path=str(temp_dir_path.resolve()))

def load_json(dir_path, file_name):
    contents = io.open(str((dir_path / file_name).resolve()), 'r', encoding='utf-8-sig').read()
    return json.loads(contents)

class PathfinderEditorWidget(BaseWidget):
    def __init__(self, *args, **kwargs):
        super().__init__('Python editor for Pathfinder: Kingmaker')
        self._savefile = ControlFile('Save File')
        self._loadbutton = ControlButton('Load')
        self._money_field = ControlText('Money')
        self._savebutton = ControlButton('Save')

        self._formset = [
            '_savefile',
            '_loadbutton',
            '_money_field',
            '_savebutton',
        ]

        self._loadbutton.value = self.__load_save_file

    def __load_save_file(self):
        try:
            temp_path = Path('./tempdir')
            extract_file(Path(self._savefile.value), temp_path)
            player_json = load_json(temp_path, 'player.json')
            self._money_field.value = str(player_json['Money'])
        except Exception as e:
            print(e)

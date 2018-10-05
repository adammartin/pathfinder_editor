from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlFile
from pyforms.controls import ControlButton
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
from shutil import rmtree
import json, io, time, os

def extract_file(path, temp_dir_path):
    if path.is_file():
        with ZipFile(str(path.resolve()), 'r') as save_zip:
            save_zip.extractall(path=str(temp_dir_path.resolve()))

def zip_dir(path, zipfile):
    for root, dirs, files in os.walk(path):
        for file in files:
            zipfile.write(os.path.join(root, file))

def load_json(dir_path, file_name):
    contents = io.open(full_path(dir_path, file_name), 'r', encoding='utf-8-sig').read()
    return json.loads(contents)

def save_json(dir_path, file_name, contents):
    with io.open(full_path(dir_path, file_name), 'w', encoding='utf-8-sig') as json_file:
        json.dump(contents, json_file)

def full_path(dir_path, file_name):
    return str((dir_path / file_name).resolve())

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
            player_json = load_json(self._temp_path, 'player.json')
            player_json['Money'] = int(self._money_field.value)
            save_json(self._temp_path, 'player.json', player_json)

            header_json = load_json(self._temp_path, 'header.json')
            header_json["Name"] = "EDITED - " + header_json["Name"]
            save_json(self._temp_path, 'header.json', header_json)

            save_root = Path(self._savefile.value).parent
            save_file = str(int(round(time.time() * 1000))) + ".zks"

            zip_path = full_path(save_root, save_file)
            zip_file = ZipFile(zip_path, 'w', ZIP_DEFLATED)
            zip_dir(self._temp_path, zip_file)
            zip_file.close()
            rmtree(self._temp_path)
        except Exception as e:
            print(e)

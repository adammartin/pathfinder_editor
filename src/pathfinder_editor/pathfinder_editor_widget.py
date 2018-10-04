from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlFile
from pyforms.controls import ControlButton
from pathlib import Path
from zipfile import ZipFile

class PathfinderEditorWidget(BaseWidget):
    def __init__(self, *args, **kwargs):
        super().__init__('Python editor for Pathfinder: Kingmaker')
        self._savefile = ControlFile('Save File')
        self._loadbutton = ControlButton('Load')
        self._savebutton = ControlButton('Save')

        self._formset = [
            '_savefile',
            '_loadbutton',
            '_savebutton',
        ]

        self._loadbutton.changed_event = self.__load_save_file

    def __load_save_file(self):
        path = Path(self._savefile.value)
        if path.is_file():
            tempDir = Path('./tempdir')
            with ZipFile(str(path.resolve()), 'r') as save_zip:
                save_zip.extractall(path=str(tempDir.resolve()))

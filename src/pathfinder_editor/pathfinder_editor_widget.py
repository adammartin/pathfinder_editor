from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlFile
from pyforms.controls import ControlButton

class PathfinderEditorWidget(BaseWidget):
    def __init__(self, *args, **kwargs):
        super().__init__('Python editor for Pathfinder: Kingmaker')
        self._savefile = ControlFile('Save File')
        self._loadbutton = ControlButton('Load')
        self._savebutton = ControlButton('Save')

        self._formset = [
            ('_savefile', '_loadbutton'),
            '_savebutton',
        ]

from tkinter import ttk, BOTH
from editor.character.party_info import PartyInfo
from editor.widgets.tabs.character_tab import CharacterTab
from editor.widgets.tabs.kingdom_info_tab import KingdomInfoTab


class Tabs():
    def __init__(self, parent):
        self._parent = parent
        self._party = None
        self._notebook = ttk.Notebook(parent, style='Default.TNotebook')
        self._main = CharacterTab(self._notebook, parent)
        self._kingdom_tab = KingdomInfoTab(self._notebook)
        self._expand()

    def load_info(self, save_dir):
        self._party = PartyInfo(self._parent.temp_path)
        self._main.load_info(self._party, save_dir)
        self._kingdom_tab.load_info(self._party)
        self._expand()

    def update_info(self):
        self._party.save()

    def _expand(self):
        self._notebook.pack(expand=1, fill=BOTH)
        self._parent.config()

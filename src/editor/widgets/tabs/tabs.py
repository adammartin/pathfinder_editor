from tkinter import ttk, BOTH
from editor.character.party_info import PartyInfo
from editor.widgets.tabs.character_tab import CharacterTab
from editor.widgets.tabs.companion_tab import CompanionTab
from editor.widgets.tabs.kingdom_info_tab import KingdomInfoTab


class Tabs():
    def __init__(self, parent):
        self._parent = parent
        self._party = None
        self._notebook = ttk.Notebook(parent, style='Default.TNotebook')
        self._main = CharacterTab(self._notebook, parent)
        self._companions = []
        self._kingdom_tab = KingdomInfoTab(self._notebook)

    def load_info(self):
        self._party = PartyInfo(self._parent.temp_path)
        self._main.load_info(self._party)
        self._load_companions()
        self._kingdom_tab.load_info(self._party)
        self._notebook.pack(expand=1, fill=BOTH)
        self._parent.config()

    def update_info(self):
        self._main.update_info(self._party)
        self._main.update_info(self._party)
        self._kingdom_tab.update_info(self._party)
        for comp_tab in self._companions:
            comp_tab.update_info()
        self._party.save()

    def _load_companions(self):
        for companion in self._party.companions:
            comp_tab = CompanionTab(self._notebook, self._parent, companion)
            comp_tab.load_info()
            self._companions.append(comp_tab)

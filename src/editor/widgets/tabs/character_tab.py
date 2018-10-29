from tkinter import ttk, BOTH
from editor.widgets.tabs.tab import Tab
from editor.widgets.tabs.skill_tab import SkillInfoTab
from editor.widgets.tabs.player_info_tab import PlayerInfoTab


class CharacterTab(Tab):
    def __init__(self, notebook, parent):
        super(CharacterTab, self).__init__(notebook)
        self._parent = parent
        self._char_book = ttk.Notebook(self._panel, style='Default.TNotebook')
        self._player_tab = PlayerInfoTab(self._char_book)
        self._skill_tab = SkillInfoTab(self._char_book)

    def load_info(self, party):
        self._notebook.add(self._panel, text=party.main_character.name())
        self._player_tab.load_info(party)
        self._skill_tab.load_info(party.main_character)
        self._notebook.pack(expand=1, fill=BOTH)
        self._char_book.pack(expand=1, fill=BOTH)
        self._panel.config()
        self._parent.config()

    def update_info(self, party):
        self._player_tab.update_info(party)
        self._skill_tab.update_info(party.main_character)

from tkinter import ttk, BOTH
from editor.widgets.tabs.tab import Tab
from editor.widgets.tabs.skill_tab import SkillInfoTab
from editor.widgets.tabs.player_info_tab import PlayerInfoTab

from tkinter import ttk, Label, StringVar, Entry, OptionMenu
from tkinter import W, EW
from editor.widgets.defaults import DEFAULT_BACKGROUND


class CharacterTab(Tab):
    def __init__(self, notebook, parent):
        super(CharacterTab, self).__init__(notebook)
        self._parent = parent
        self._sel_panel = ttk.Frame(self._panel, style='Default.TFrame')
        self._char_sel = None
        self._char_book = ttk.Notebook(self._panel, style='Default.TNotebook')
        self._character_tab = PlayerInfoTab(self._char_book)
        self._skill_tab = SkillInfoTab(self._char_book)
        self._notebook.add(self._panel, text="Character Info")
        self._party = None
        self._expand()

    def load_info(self, party):
        self._char_sel = self._add_char_dropdown(0, 0, 'Character:',
                                                list(party.members.keys()))
        selected = self._char_sel.get()
        self._party = party
        self._update_character_tab()

    def update_info(self, party):
        pass

    def _expand(self):
        self._sel_panel.pack(expand=1, fill=BOTH)
        self._notebook.pack(expand=1, fill=BOTH)
        self._char_book.pack(expand=1, fill=BOTH)
        self._sel_panel.config()
        self._panel.config()
        self._parent.config()

    def _update_character_tab(self, *args):
        party = self._party
        selected = self._char_sel.get()
        self._character_tab.load_info(party, party.members[selected])
        self._skill_tab.load_info(party.members[selected])

    def _add_char_dropdown(self, a_row, a_col, text, choices):
        col = a_col*2
        label = Label(self._sel_panel, text=text, borderwidth=1)
        label.configure(background=DEFAULT_BACKGROUND)
        label.grid(row=a_row, column=col, sticky=W)
        variable = StringVar()
        variable.set(choices[0])
        variable.trace('w', self._update_character_tab)
        entry = OptionMenu(self._sel_panel, variable, *choices)
        entry.grid(row=a_row, column=col+1, sticky=EW)
        return variable

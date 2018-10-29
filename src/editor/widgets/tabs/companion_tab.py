from tkinter import ttk, BOTH
from editor.widgets.tabs.tab import Tab
from editor.widgets.tabs.skill_tab import SkillInfoTab
from editor.widgets.tabs.companion_info_tab import CompanionInfoTab


class CompanionTab(Tab):
    def __init__(self, notebook, parent, companion):
        super(CompanionTab, self).__init__(notebook)
        self._parent = parent
        self._companion = companion
        self._char_book = ttk.Notebook(self._panel, style='Default.TNotebook')
        self._comp_tab = CompanionInfoTab(self._char_book)
        self._skill_tab = SkillInfoTab(self._char_book)

    def load_info(self):
        self._notebook.add(self._panel, text=self._companion.name())
        self._comp_tab.load_info(self._companion)
        self._skill_tab.load_info(self._companion)
        self._notebook.pack(expand=1, fill=BOTH)
        self._char_book.pack(expand=1, fill=BOTH)
        self._panel.config()
        self._parent.config()

    def update_info(self):
        self._comp_tab.update_info(self._companion)
        self._skill_tab.update_info(self._companion)

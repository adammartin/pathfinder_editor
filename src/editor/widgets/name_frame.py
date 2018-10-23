from tkinter import ttk, StringVar, Label, LEFT, E, W, BOTH
from editor.character.player_info import PlayerInfo
from editor.widgets.defaults import DEFAULT_BACKGROUND


class NameFrame(ttk.Frame):
    # pylint: disable=too-many-ancestors
    def __init__(self, master):
        ttk.Frame.__init__(self, master, style='Default.TFrame')
        label = Label(self, text='Name:', borderwidth=1)
        label.configure(background=DEFAULT_BACKGROUND)
        label.pack(expand=1, side=LEFT, anchor=E)
        self._player_name = StringVar('')
        self._player_name_field = Label(self,
                                        textvariable=self._player_name,
                                        borderwidth=1)
        self._player_name_field.configure(background=DEFAULT_BACKGROUND)
        self._player_name_field.pack(expand=1, side=LEFT, anchor=W)
        self.pack(expand=1, fill=BOTH)

    def load_info(self, path):
        player_info = PlayerInfo(path)
        self._player_name.set(player_info.name())

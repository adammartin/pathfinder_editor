import time
from pathlib import Path
from shutil import rmtree
from tkinter import Frame, filedialog, ttk, Menu, Label, StringVar
from tkinter import LEFT, E, W, BOTH
from file_utils import extract_file, persist_as_zip
from player_info import PlayerInfo
from widgets.tabs import Tabs
from widgets.defaults import DEFAULT_BACKGROUND


class PathfinderTkWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self._temp_path = Path('./tempdir/')
        self._name_panel = self._create_name_panel()
        self._tabs = Tabs(self)
        self._create_menu_bar()
        self._clean_temp_storage()
        self.pack()

    def _create_menu_bar(self):
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self._file_open)
        filemenu.add_command(label="Save", command=self._save_and_destroy)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.master.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        self.master.config(menu=menubar)

    def _create_name_panel(self):
        name_frame = NameFrame(self)
        name_frame.pack(expand=1, fill=BOTH)
        return name_frame

    def on_destroy(self):
        self._clean_temp_storage()

    def _save_and_destroy(self):
        self._tabs.update_info(self._temp_path)
        save_root = Path(self.master.filename).parent
        save_file = str(int(round(time.time() * 1000))) + ".zks"
        persist_as_zip(save_root, save_file, self._temp_path)
        self.master.quit()

    def _file_open(self):
        self.master.filename = filedialog.askopenfilename(title="Select file")
        extract_file(Path(self.master.filename), self._temp_path)
        self._name_panel.load_info(self._temp_path)
        self._tabs.load_info(self._temp_path)

    def _clean_temp_storage(self):
        if self._temp_path.exists():
            rmtree(self._temp_path)


class NameFrame(ttk.Frame):
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

    def load_info(self, path):
        player_info = PlayerInfo(path)
        self._player_name.set(player_info.name())

from pathlib import Path
from tkinter import Frame, filedialog, Menu
from editor.character.file_utils import extract_file
from editor.character.file_utils import save_game_file
from editor.character.file_utils import clean_temp_storage
from editor.widgets.tabs.tabs import Tabs


class PathfinderTkWindow(Frame):
    # pylint: disable=too-many-ancestors
    def __init__(self, master):
        Frame.__init__(self, master)
        self.temp_path = Path('./tempdir/')
        self._tabs = Tabs(self)
        self._create_menu_bar()
        clean_temp_storage(self.temp_path)
        master.minsize(700, 300)
        self.pack()

    def _create_menu_bar(self):
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open",
                             command=self._file_open,
                             accelerator='Ctrl+o')
        filemenu.add_command(label="Save",
                             command=self._save_and_destroy,
                             accelerator='Ctrl+s')
        filemenu.add_separator()
        filemenu.add_command(label="Exit",
                             command=self.master.quit,
                             accelerator='Ctrl+q')
        menubar.add_cascade(label="File", menu=filemenu)
        self.master.config(menu=menubar)
        self.bind_all("<Control-o>", self._file_open)
        self.bind_all("<Control-s>", self._save_and_destroy)
        self.bind_all("<Control-q>", self._quit)

    def on_destroy(self):
        clean_temp_storage(self.temp_path)

    def _quit(self, event=None):
        # pylint: disable=unused-argument
        self.master.quit()

    def _save_and_destroy(self, event=None):
        # pylint: disable=unused-argument
        self._tabs.update_info()
        save_game_file(self.master.filename, self.temp_path)
        self.master.quit()

    def _file_open(self, event=None):
        # pylint: disable=unused-argument
        self.master.filename = filedialog.askopenfilename(title="Select file")
        extract_file(Path(self.master.filename), self.temp_path)
        self._tabs.load_info()
        self.pack()

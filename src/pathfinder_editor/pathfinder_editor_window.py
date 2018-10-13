import wx
from functools import partial
from pathlib import Path
from shutil import rmtree
from file_utils import extract_file, persist_as_zip
from player_info import PlayerInfo
from skill_info import SkillInfo
from kingdom_info import KingdomInfo

class PathfinderEditorWindow(wx.Frame):

    def __init__(self, *args, **kw):
        super(PathfinderEditorWindow, self).__init__(*args, **kw)
        self._temp_path = Path('./tempdir/')
        self._clean_temp_storage()
        self._panel = wx.Panel(self)
        self._notebook = wx.Notebook(self._panel)
        self._player_info_tab = PlayerInfoTab(self._notebook)
        self._skill_info_tab = SkillInfoTab(self._notebook)
        self._kingdom_info_tab = KingdomInfoTab(self._notebook)
        self._top_sizer = wx.BoxSizer(wx.VERTICAL)
        self._make_menu_bar()
        self._size()
        self.Centre()

    def _on_exit(self, event):
        self._clean_temp_storage()
        self.Close(True)

    def _open_file(self, event):
        open_file_dialog = wx.FileDialog(self, "Open", "", "",
                                      "Save files (*.zks)|*.zks",
                                       wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        open_file_dialog.ShowModal()
        self._populate_data(open_file_dialog.GetPath())
        open_file_dialog.Destroy()

    def _populate_data(self, path):
        extract_file(Path(path), self._temp_path)
        self._player_info_tab.load_info(self._temp_path)
        self._skill_info_tab.load_info(self._temp_path)
        self._kingdom_info_tab.load_info(self._temp_path)

    def _make_menu_bar(self):
        file_menu = wx.Menu()
        open_file = file_menu.Append(-1, "&Open\tCtrl-o", "Save file to edit.")
        file_menu.AppendSeparator()
        exit_item = file_menu.Append(wx.ID_EXIT)
        menu_bar = wx.MenuBar()
        menu_bar.Append(file_menu, "&File")
        self.SetMenuBar(menu_bar)
        self.Bind(wx.EVT_MENU, self._on_exit, exit_item)
        self.Bind(wx.EVT_MENU, self._open_file,  open_file)

    def _add_tabs(self, sizer):
        self._notebook.AddPage(self._player_info_tab, "Player Info")
        self._notebook.AddPage(self._skill_info_tab, "Skill Info")
        self._notebook.AddPage(self._kingdom_info_tab, "Kingdom Info")

    def _size(self):
        self._panel.SetSizer(self._top_sizer)
        self._size_notebook()
        self._top_sizer.Fit(self)

    def _size_notebook(self):
        sizer = wx.BoxSizer()
        self._add_tabs(sizer)
        sizer.Add(self._notebook, 1, wx.EXPAND, 1, wx.ALL | wx.EXPAND)
        self._top_sizer.Add(sizer, wx.ALIGN_RIGHT)

    def _clean_temp_storage(self):
        if self._temp_path.exists():
            rmtree(str(self._temp_path.resolve()))


class PlayerInfoTab(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.money_label = wx.StaticText(self, -1, "Money:")
        self.money_field = wx.TextCtrl(self)
        self.experience_label = wx.StaticText(self, -1, "Experience:")
        self.experience_field = wx.TextCtrl(self)
        self.strength_label = wx.StaticText(self, -1, "Strength:")
        self.strength_field = wx.TextCtrl(self)
        self.dexterity_label = wx.StaticText(self, -1, "Dexterity:")
        self.dexterity_field = wx.TextCtrl(self)
        self.constitution_label = wx.StaticText(self, -1, "Constitution:")
        self.constitution_field = wx.TextCtrl(self)
        self.intelligence_label = wx.StaticText(self, -1, "Intelligence:")
        self.intelligence_field = wx.TextCtrl(self)
        self.wisdom_label = wx.StaticText(self, -1, "Wisdom:")
        self.wisdom_field = wx.TextCtrl(self)
        self.charisma_label = wx.StaticText(self, -1, "Charisma:")
        self.charisma_field = wx.TextCtrl(self)
        self.sizer = self._sizer()
        self.SetSizer(self.sizer)

    def load_info(self, path):
        player_info = PlayerInfo(path)
        self.money_field.SetValue(str(player_info.money()))
        self.experience_field.SetValue(str(player_info.experience()))
        self.strength_field.SetValue(str(player_info.strength()))
        self.dexterity_field.SetValue(str(player_info.dexterity()))
        self.constitution_field.SetValue(str(player_info.constitution()))
        self.intelligence_field.SetValue(str(player_info.intelligence()))
        self.wisdom_field.SetValue(str(player_info.wisdom()))
        self.charisma_field.SetValue(str(player_info.charisma()))

    def _sizer(self):
        sizer = wx.GridBagSizer(4, 4)
        sizer.Add(self.money_label, (0, 0))
        sizer.Add(self.money_field, (0, 1))
        sizer.Add(self.experience_label, (0, 3))
        sizer.Add(self.experience_field, (0, 4))
        sizer.Add(self.strength_label, (1, 0))
        sizer.Add(self.strength_field, (1, 1))
        sizer.Add(self.dexterity_label, (1, 3))
        sizer.Add(self.dexterity_field, (1, 4))
        sizer.Add(self.constitution_label, (2, 0))
        sizer.Add(self.constitution_field, (2, 1))
        sizer.Add(self.intelligence_label, (2, 3))
        sizer.Add(self.intelligence_field, (2, 4))
        sizer.Add(self.wisdom_label, (3, 0))
        sizer.Add(self.wisdom_field, (3, 1))
        sizer.Add(self.charisma_label, (3, 3))
        sizer.Add(self.charisma_field, (3, 4))
        return sizer


class SkillInfoTab(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.athletics_label = wx.StaticText(self, -1, "Athletics:")
        self.athletics_field = wx.TextCtrl(self)
        self.arcana_label = wx.StaticText(self, -1, "Knowledge Arcana:")
        self.arcana_field = wx.TextCtrl(self)
        self.world_label = wx.StaticText(self, -1, "Knowledge World:")
        self.world_field = wx.TextCtrl(self)
        self.nature_label = wx.StaticText(self, -1, "Lore Nature:")
        self.nature_field = wx.TextCtrl(self)
        self.religion_label = wx.StaticText(self, -1, "Lore Religion:")
        self.religion_field = wx.TextCtrl(self)
        self.mobility_label = wx.StaticText(self, -1, "Mobility:")
        self.mobility_field = wx.TextCtrl(self)
        self.perception_label = wx.StaticText(self, -1, "Perception:")
        self.perception_field = wx.TextCtrl(self)
        self.persuasion_label = wx.StaticText(self, -1, "Persuasion:")
        self.persuasion_field = wx.TextCtrl(self)
        self.stealth_label = wx.StaticText(self, -1, "Stealth:")
        self.stealth_field = wx.TextCtrl(self)
        self.theivery_label = wx.StaticText(self, -1, "Theivery:")
        self.theivery_field = wx.TextCtrl(self)
        self.use_magic_device_label = wx.StaticText(self, -1, "Use Magic Device:")
        self.use_magic_device_field = wx.TextCtrl(self)
        self.sizer = self._sizer()
        self.SetSizer(self.sizer)

    def load_info(self, path):
        skill_info = SkillInfo(path)
        self.athletics_field.SetValue(str(skill_info.athletics()))
        self.arcana_field.SetValue(str(skill_info.knowledge_arcana()))
        self.world_field.SetValue(str(skill_info.knowledge_world()))
        self.nature_field.SetValue(str(skill_info.lore_nature()))
        self.religion_field.SetValue(str(skill_info.lore_religion()))
        self.mobility_field.SetValue(str(skill_info.mobility()))
        self.perception_field.SetValue(str(skill_info.perception()))
        self.persuasion_field.SetValue(str(skill_info.persuasion()))
        self.stealth_field.SetValue(str(skill_info.stealth()))
        self.theivery_field.SetValue(str(skill_info.theivery()))
        self.use_magic_device_field.SetValue(str(skill_info.use_magic_device()))

    def _sizer(self):
        sizer = wx.GridBagSizer(5, 4)
        sizer.Add(self.athletics_label, (0, 0))
        sizer.Add(self.athletics_field, (0, 1))
        sizer.Add(self.arcana_label, (0, 2))
        sizer.Add(self.arcana_field, (0, 3))
        sizer.Add(self.world_label, (1, 0))
        sizer.Add(self.world_field, (1, 1))
        sizer.Add(self.nature_label, (1, 2))
        sizer.Add(self.nature_field, (1, 3))
        sizer.Add(self.religion_label, (2, 0))
        sizer.Add(self.religion_field, (2, 1))
        sizer.Add(self.mobility_label, (2, 2))
        sizer.Add(self.mobility_field, (2, 3))
        sizer.Add(self.perception_label, (3, 0))
        sizer.Add(self.perception_field, (3, 1))
        sizer.Add(self.persuasion_label, (3, 2))
        sizer.Add(self.persuasion_field, (3, 3))
        sizer.Add(self.stealth_label, (4, 0))
        sizer.Add(self.stealth_field, (4, 1))
        sizer.Add(self.theivery_label, (4, 2))
        sizer.Add(self.theivery_field, (4, 3))
        sizer.Add(self.use_magic_device_label, (5, 0))
        sizer.Add(self.use_magic_device_field, (5, 1))
        return sizer


class KingdomInfoTab(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.build_point_label = wx.StaticText(self, -1, "Build Points:")
        self.build_point_field = wx.TextCtrl(self)
        self.sizer = self._sizer()
        self.SetSizer(self.sizer)

    def load_info(self, path):
        kingdom_info = KingdomInfo(path)
        self.build_point_field.SetValue(kingdom_info.build_points()))

    def _sizer(self):
        sizer = wx.GridBagSizer(2, 2)
        sizer.Add(self.build_point_label, (0, 0))
        sizer.Add(self.build_point_field, (0, 1))
        return sizer

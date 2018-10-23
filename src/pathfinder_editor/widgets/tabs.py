from tkinter import ttk, Label, StringVar, Entry, OptionMenu, Button
from tkinter import BOTH, W, EW
from character.player_info import PlayerInfo, ALIGNMENTS
from character.skill_info import SkillInfo
from character.kingdom_info import KingdomInfo
from widgets.defaults import DEFAULT_BACKGROUND


WARNING = "USE AT YOUR OWN RISK! Save these before you save your main changes."


class Tabs():
    def __init__(self, parent):
        self._parent = parent
        self._notebook = ttk.Notebook(parent, style='Default.TNotebook')
        self._player_tab = PlayerInfoTab(self._notebook)
        self._skill_tab = SkillInfoTab(self._notebook)
        self._kingdom_tab = KingdomInfoTab(self._notebook)
        self._experimental_tab = ExperimentalInfoTab(self._notebook,
                                                     parent.temp_path)
        self._notebook.pack(expand=1, fill=BOTH)

    def load_info(self, path):
        self._player_tab.load_info(path)
        self._skill_tab.load_info(path)
        self._kingdom_tab.load_info(path)
        self._experimental_tab.load_info(path)

    def update_info(self, path):
        self._player_tab.update_info(path)
        self._skill_tab.update_info(path)
        self._kingdom_tab.update_info(path)


class Tab():
    # pylint: disable=too-few-public-methods
    def __init__(self, notebook):
        self._panel = ttk.Frame(notebook, style='Default.TFrame')

    def _add_large_label(self, a_row, colspan, label_text):
        label = Label(self._panel, text=label_text, borderwidth=1, fg='red')
        label.configure(background=DEFAULT_BACKGROUND)
        label.grid(row=a_row, columnspan=colspan, sticky=W)

    def _add_field(self, a_row, a_col, label_text):
        col = a_col*2
        label = self._add_label(a_row, col, label_text)
        variable = StringVar()
        entry = Entry(self._panel, textvariable=variable)
        entry.grid(row=a_row, column=col+1, sticky=W)
        return variable

    def _add_dropdown(self, a_row, a_col, label_text, choices):
        col = a_col*2
        label = self._add_label(a_row, col, label_text)
        variable = StringVar()
        entry = OptionMenu(self._panel, variable, *choices)
        entry.grid(row=a_row, column=col+1, sticky=EW)
        return variable

    def _add_label(self, a_row, a_col, label_text):
        label = Label(self._panel, text=label_text, borderwidth=1)
        label.configure(background=DEFAULT_BACKGROUND)
        label.grid(row=a_row, column=a_col, sticky=W)
        return label


class PlayerInfoTab(Tab):
    # pylint: disable=too-many-instance-attributes
    def __init__(self, notebook):
        super(PlayerInfoTab, self).__init__(notebook)
        notebook.add(self._panel, text="Player")
        self._money = self._add_field(0, 0, 'Money:')
        self._experience = self._add_field(0, 1, 'Experience:')
        self._strength = self._add_field(1, 0, 'Strength:')
        self._dexterity = self._add_field(1, 1, 'Dexterity:')
        self._constitution = self._add_field(2, 0, 'Constitution:')
        self._intelligence = self._add_field(2, 1, 'Intelligence:')
        self._wisdom = self._add_field(3, 0, 'Wisdom:')
        self._charisma = self._add_field(3, 1, 'Charisma:')
        self._panel.config()

    def load_info(self, path):
        player_info = PlayerInfo(path)
        self._money.set(player_info.money())
        self._experience.set(player_info.experience())
        self._strength.set(player_info.strength())
        self._dexterity.set(player_info.dexterity())
        self._constitution.set(player_info.constitution())
        self._intelligence.set(player_info.intelligence())
        self._wisdom.set(player_info.wisdom())
        self._charisma.set(player_info.charisma())

    def update_info(self, path):
        player_info = PlayerInfo(path)
        player_info.update_header_name()
        player_info.update_money(self._money.get())
        player_info.update_experience(self._experience.get())
        player_info.update_strength(self._strength.get())
        player_info.update_dexterity(self._dexterity.get())
        player_info.update_constitution(self._constitution.get())
        player_info.update_intelligence(self._intelligence.get())
        player_info.update_wisdom(self._wisdom.get())
        player_info.update_charisma(self._charisma.get())


class ExperimentalInfoTab(Tab):
    def __init__(self, notebook, temp_path):
        super(ExperimentalInfoTab, self).__init__(notebook)
        self._temp_path = temp_path
        notebook.add(self._panel, text="Experimental")
        self._warning = self._add_large_label(0, 2, WARNING)
        self._alignment = self._add_dropdown(1, 0, 'Alignment:',
                                             ALIGNMENTS.keys())
        self._save_button = Button(self._panel,
                                   text="SAVE EXPERIMENTAL",
                                   command=self.update_experimental)
        self._save_button.grid(row=3, column=0, sticky=W)

    def load_info(self, path):
        player_info = PlayerInfo(path)
        self._alignment.set(player_info.alignment())

    def update_info(self, path):
        pass

    def update_experimental(self):
        player_info = PlayerInfo(self._temp_path)
        player_info.update_alignment(self._alignment.get())


class SkillInfoTab(Tab):
    # pylint: disable=too-many-instance-attributes
    def __init__(self, notebook):
        super(SkillInfoTab, self).__init__(notebook)
        notebook.add(self._panel, text="Skills")
        self._athletics_field = self._add_field(0, 0, 'Athletics:')
        self._mobility_field = self._add_field(0, 1, 'Mobility:')
        self._arcana_field = self._add_field(1, 0, 'Knowledge Arcana:')
        self._knowledge_world_field = self._add_field(1, 1, 'Knowledge World:')
        self._lore_nature_field = self._add_field(2, 0, 'Lore Nature:')
        self._lore_religion_field = self._add_field(2, 1, 'Lore Religion:')
        self._perception_field = self._add_field(3, 0, 'Perception:')
        self._persuasion_field = self._add_field(3, 1, 'Persuasion:')
        self._stealth_field = self._add_field(4, 0, 'Stealth:')
        self._theivery_field = self._add_field(4, 1, 'Theivery:')
        self._use_magic_device_field = self._add_field(5, 0,
                                                       'Use Magic Device:')

    def load_info(self, path):
        skill_info = SkillInfo(path)
        self._athletics_field.set(skill_info.athletics())
        self._arcana_field.set(skill_info.knowledge_arcana())
        self._knowledge_world_field .set(skill_info.knowledge_world())
        self._lore_nature_field.set(skill_info.lore_nature())
        self._lore_religion_field.set(skill_info.lore_religion())
        self._mobility_field.set(skill_info.mobility())
        self._perception_field.set(skill_info.perception())
        self._persuasion_field.set(skill_info.persuasion())
        self._stealth_field.set(skill_info.stealth())
        self._theivery_field.set(skill_info.theivery())
        self._use_magic_device_field.set(skill_info.use_magic_device())

    def update_info(self, path):
        skill_info = SkillInfo(path)
        skill_info.update_athletics(self._athletics_field.get())
        skill_info.update_knowledge_arcana(self._arcana_field.get())
        skill_info.update_knowledge_world(self._knowledge_world_field.get())
        skill_info.update_mobility(self._mobility_field.get())
        skill_info.update_lore_nature(self._lore_nature_field.get())
        skill_info.update_lore_religion(self._lore_religion_field.get())
        skill_info.update_perception(self._perception_field.get())
        skill_info.update_persuasion(self._persuasion_field.get())
        skill_info.update_stealth(self._stealth_field.get())
        skill_info.update_theivery(self._theivery_field.get())
        skill_info.update_use_magic_device(self._use_magic_device_field.get())


class KingdomInfoTab(Tab):
    # pylint: disable=too-many-instance-attributes
    def __init__(self, notebook):
        super(KingdomInfoTab, self).__init__(notebook)
        notebook.add(self._panel, text="Kingdom")
        self._kingdom_name_field = self._add_field(0, 0, 'Kingdom Name:')
        self._build_points_field = self._add_field(0, 1, 'Build Points:')
        self._community_field = self._add_field(1, 0, 'Community:')
        self._loyalty_field = self._add_field(1, 1, 'Loyalty:')
        self._military_field = self._add_field(2, 0, 'Military:')
        self._economy_field = self._add_field(2, 1, 'Economy:')
        self._relations_field = self._add_field(3, 0, 'Relations:')
        self._divine_field = self._add_field(3, 1, 'Divine')
        self._arcane_field = self._add_field(4, 0, 'Arcane')
        self._stability_field = self._add_field(4, 1, 'Stability:')
        self._culture_field = self._add_field(5, 0, 'Culture:')
        self._espionage_field = self._add_field(5, 1, 'Espionage:')

    def load_info(self, path):
        kingdom_info = KingdomInfo(path)
        if kingdom_info.has_kingdom_data():
            self._kingdom_name_field.set(kingdom_info.kingdom_name())
            self._build_points_field.set(kingdom_info.build_points())
            self._community_field.set(kingdom_info.community())
            self._loyalty_field.set(kingdom_info.loyalty())
            self._military_field.set(kingdom_info.military())
            self._economy_field.set(kingdom_info.economy())
            self._relations_field.set(kingdom_info.relations())
            self._divine_field.set(kingdom_info.divine())
            self._arcane_field.set(kingdom_info.arcane())
            self._stability_field.set(kingdom_info.stability())
            self._culture_field.set(kingdom_info.culture())
            self._espionage_field.set(kingdom_info.espionage())

    def update_info(self, path):
        kingdom_info = KingdomInfo(path)
        if kingdom_info.has_kingdom_data():
            kingdom_info.update_kingdom_name(self._kingdom_name_field.get())
            kingdom_info.update_build_points(self._build_points_field.get())
            kingdom_info.update_community(self._community_field.get())
            kingdom_info.update_loyalty(self._loyalty_field.get())
            kingdom_info.update_military(self._military_field.get())
            kingdom_info.update_economy(self._economy_field.get())
            kingdom_info.update_relations(self._relations_field.get())
            kingdom_info.update_divine(self._divine_field.get())
            kingdom_info.update_arcane(self._arcane_field.get())
            kingdom_info.update_stability(self._stability_field.get())
            kingdom_info.update_culture(self._culture_field.get())
            kingdom_info.update_espionage(self._espionage_field.get())

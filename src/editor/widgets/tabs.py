from tkinter import ttk, Label, StringVar, Entry, OptionMenu, Button
from tkinter import BOTH, W, EW
from editor.character.alignment_info import ALIGNMENTS
from editor.character.kingdom_info import KingdomInfo
from editor.character.party_info import PartyInfo
from editor.widgets.defaults import DEFAULT_BACKGROUND
from editor.widgets.name_frame import NameFrame


class Tabs():
    def __init__(self, parent):
        self._parent = parent
        self._party = None
        self._name_panel = NameFrame(parent)
        self._notebook = ttk.Notebook(parent, style='Default.TNotebook')
        self._player_tab = PlayerInfoTab(self._notebook)
        self._skill_tab = SkillInfoTab(self._notebook)
        self._kingdom_tab = KingdomInfoTab(self._notebook)
        self._notebook.pack(expand=1, fill=BOTH)

    def load_info(self, path):
        self._party = PartyInfo(self._parent.temp_path)
        self._name_panel.load_info(self._party.main_character)
        self._player_tab.load_info(self._party)
        self._skill_tab.load_info(self._party)
        self._kingdom_tab.load_info(path)

    def update_info(self, path):
        self._player_tab.update_info()
        self._skill_tab.update_info()
        self._kingdom_tab.update_info(path)


class Tab():
    # pylint: disable=too-few-public-methods
    def __init__(self, notebook):
        self._panel = ttk.Frame(notebook, style='Default.TFrame')
        self._party = None

    def _add_large_label(self, a_row, colspan, label_text):
        label = Label(self._panel, text=label_text, borderwidth=1, fg='red')
        label.configure(background=DEFAULT_BACKGROUND)
        label.grid(row=a_row, columnspan=colspan, sticky=W)

    def _add_field(self, a_row, a_col, label_text):
        col = a_col*2
        self._add_label(a_row, col, label_text)
        variable = StringVar()
        entry = Entry(self._panel, textvariable=variable)
        entry.grid(row=a_row, column=col+1, sticky=W)
        return variable

    def _add_dropdown(self, a_row, a_col, label_text, choices):
        col = a_col*2
        self._add_label(a_row, col, label_text)
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
        self._alignment = self._add_dropdown(1, 0, 'Alignment:',
                                             ALIGNMENTS.keys())
        self._strength = self._add_field(2, 0, 'Strength:')
        self._dexterity = self._add_field(2, 1, 'Dexterity:')
        self._constitution = self._add_field(3, 0, 'Constitution:')
        self._intelligence = self._add_field(3, 1, 'Intelligence:')
        self._wisdom = self._add_field(4, 0, 'Wisdom:')
        self._charisma = self._add_field(4, 1, 'Charisma:')
        self._panel.config()

    def load_info(self, party):
        self._money.set(party.money())
        character = party.main_character
        self._experience.set(character.experience())
        self._alignment.set(character.alignment.alignment())
        self._strength.set(character.stats.strength())
        self._dexterity.set(character.stats.dexterity())
        self._constitution.set(character.stats.constitution())
        self._intelligence.set(character.stats.intelligence())
        self._wisdom.set(character.stats.wisdom())
        self._charisma.set(character.stats.charisma())

    def update_info(self, party):
        character = party.main_character
        character.stats.update_money(self._money.get())
        character.update_experience(self._experience.get())
        character.alignment.update_alignment(self._alignment.get())
        character.stats.update_strength(self._strength.get())
        character.stats.update_dexterity(self._dexterity.get())
        character.stats.update_constitution(self._constitution.get())
        character.stats.update_intelligence(self._intelligence.get())
        character.stats.update_wisdom(self._wisdom.get())
        character.stats.update_charisma(self._charisma.get())


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

    def load_info(self, party):
        character = party.main_character
        self._athletics_field.set(character.skills.athletics())
        self._arcana_field.set(character.skills.knowledge_arcana())
        self._knowledge_world_field .set(character.skills.knowledge_world())
        self._lore_nature_field.set(character.skills.lore_nature())
        self._lore_religion_field.set(character.skills.lore_religion())
        self._mobility_field.set(character.skills.mobility())
        self._perception_field.set(character.skills.perception())
        self._persuasion_field.set(character.skills.persuasion())
        self._stealth_field.set(character.skills.stealth())
        self._theivery_field.set(character.skills.theivery())
        self._use_magic_device_field.set(character.skills.use_magic_device())

    def update_info(self, party):
        character = party.main_character
        character.skills.update_athletics(self._athletics_field.get())
        character.skills.update_knowledge_arcana(self._arcana_field.get())
        character.skills.update_knowledge_world(self._knowledge_world_field.get())
        character.skills.update_mobility(self._mobility_field.get())
        character.skills.update_lore_nature(self._lore_nature_field.get())
        character.skills.update_lore_religion(self._lore_religion_field.get())
        character.skills.update_perception(self._perception_field.get())
        character.skills.update_persuasion(self._persuasion_field.get())
        character.skills.update_stealth(self._stealth_field.get())
        character.skills.update_theivery(self._theivery_field.get())
        character.skills.update_use_magic_device(self._use_magic_device_field.get())


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

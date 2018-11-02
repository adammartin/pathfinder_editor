from editor.widgets.tabs.tab import Tab


class SkillInfoTab(Tab):
    # pylint: disable=too-many-instance-attributes, too-few-public-methods
    def __init__(self, notebook):
        super(SkillInfoTab, self).__init__(notebook)
        func = self._update_info
        self._athletics = self._add_field(0, 0, 'Athletics:', func)
        self._mobility = self._add_field(0, 1, 'Mobility:', func)
        self._arcana = self._add_field(1, 0, 'Knowledge Arcana:', func)
        self._world = self._add_field(1, 1, 'Knowledge World:', func)
        self._lore_nature = self._add_field(2, 0, 'Lore Nature:', func)
        self._lore_religion = self._add_field(2, 1, 'Lore Religion:', func)
        self._perception = self._add_field(3, 0, 'Perception:', func)
        self._persuasion = self._add_field(3, 1, 'Persuasion:', func)
        self._stealth = self._add_field(4, 0, 'Stealth:', func)
        self._theivery = self._add_field(4, 1, 'Theivery:', func)
        self._magic_dev = self._add_field(5, 0, 'Use Magic Device:', func)
        self._notebook.add(self._panel, text="Skills")
        self._character = None
        self._panel.config()

    def load_info(self, character):
        self._character = character
        self._dirty_lock = True
        self._athletics.set(character.skills.athletics())
        self._arcana.set(character.skills.knowledge_arcana())
        self._world .set(character.skills.knowledge_world())
        self._lore_nature.set(character.skills.lore_nature())
        self._lore_religion.set(character.skills.lore_religion())
        self._mobility.set(character.skills.mobility())
        self._perception.set(character.skills.perception())
        self._persuasion.set(character.skills.persuasion())
        self._stealth.set(character.skills.stealth())
        self._theivery.set(character.skills.theivery())
        self._magic_dev.set(character.skills.use_magic_device())
        self._dirty_lock = False
        self._panel.config()

    def _update_info(self, *args):
        # pylint: disable=unused-argument
        skills = self._character.skills
        self._update(self._athletics, skills.update_athletics)
        self._update(self._arcana, skills.update_knowledge_arcana)
        self._update(self._world, skills.update_knowledge_world)
        self._update(self._mobility, skills.update_mobility)
        self._update(self._lore_nature, skills.update_lore_nature)
        self._update(self._lore_religion, skills.update_lore_religion)
        self._update(self._perception, skills.update_perception)
        self._update(self._persuasion, skills.update_persuasion)
        self._update(self._stealth, skills.update_stealth)
        self._update(self._theivery, skills.update_theivery)
        self._update(self._magic_dev, skills.update_use_magic_device)

from editor.widgets.tabs.tab import Tab


class SkillInfoTab(Tab):
    # pylint: disable=too-many-instance-attributes
    def __init__(self, notebook):
        super(SkillInfoTab, self).__init__(notebook)
        self._athletics_field = self._add_field(0, 0, 'Athletics:',
                                                self._update_info)
        self._mobility_field = self._add_field(0, 1, 'Mobility:',
                                               self._update_info)
        self._arcana_field = self._add_field(1, 0, 'Knowledge Arcana:',
                                             self._update_info)
        self._world_field = self._add_field(1, 1, 'Knowledge World:',
                                            self._update_info)
        self._lore_nature_field = self._add_field(2, 0, 'Lore Nature:',
                                                  self._update_info)
        self._lore_religion_field = self._add_field(2, 1, 'Lore Religion:',
                                                    self._update_info)
        self._perception_field = self._add_field(3, 0, 'Perception:',
                                                 self._update_info)
        self._persuasion_field = self._add_field(3, 1, 'Persuasion:',
                                                 self._update_info)
        self._stealth_field = self._add_field(4, 0, 'Stealth:',
                                              self._update_info)
        self._theivery_field = self._add_field(4, 1, 'Theivery:',
                                               self._update_info)
        self._magic_dev_field = self._add_field(5, 0, 'Use Magic Device:',
                                                self._update_info)
        self._notebook.add(self._panel, text="Skills")
        self._character = None
        self._panel.config()

    def load_info(self, character):
        self._character = character
        self._dirty_lock = True
        self._athletics_field.set(character.skills.athletics())
        self._arcana_field.set(character.skills.knowledge_arcana())
        self._world_field .set(character.skills.knowledge_world())
        self._lore_nature_field.set(character.skills.lore_nature())
        self._lore_religion_field.set(character.skills.lore_religion())
        self._mobility_field.set(character.skills.mobility())
        self._perception_field.set(character.skills.perception())
        self._persuasion_field.set(character.skills.persuasion())
        self._stealth_field.set(character.skills.stealth())
        self._theivery_field.set(character.skills.theivery())
        self._magic_dev_field.set(character.skills.use_magic_device())
        self._dirty_lock = False
        self._panel.config()

    def _update_info(self, *args):
        skills = self._character.skills
        self._update(self._athletics_field, skills.update_athletics)
        self._update(self._arcana_field, skills.update_knowledge_arcana)
        self._update(self._world_field, skills.update_knowledge_world)
        self._update(self._mobility_field, skills.update_mobility)
        self._update(self._lore_nature_field, skills.update_lore_nature)
        self._update(self._lore_religion_field, skills.update_lore_religion)
        self._update(self._perception_field, skills.update_perception)
        self._update(self._persuasion_field, skills.update_persuasion)
        self._update(self._stealth_field, skills.update_stealth)
        self._update(self._theivery_field, skills.update_theivery)
        self._update(self._magic_dev_field, skills.update_use_magic_device)

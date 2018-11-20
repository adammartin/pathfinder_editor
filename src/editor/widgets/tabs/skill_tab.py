from editor.widgets.tabs.tab import Tab, _set_fields, _update_field

SKILLS = [
    {'label': 'Athletics', 'position': [0, 0], 'getter': 'athletics',
     'setter': 'update_athletics'},
    {'label': 'Mobility', 'position': [0, 1],
     'getter': 'knowledge_arcana', 'setter': 'update_knowledge_arcana'},
    {'label': 'Knowledge Arcana', 'position': [1, 0],
     'getter': 'knowledge_world', 'setter': 'update_knowledge_world'},
    {'label': 'Knowledge World', 'position': [1, 1], 'getter': 'lore_nature',
     'setter': 'update_mobility'},
    {'label': 'Lore Nature', 'position': [2, 0], 'getter': 'lore_religion',
     'setter': 'update_lore_nature'},
    {'label': 'Lore Religion', 'position': [2, 1], 'getter': 'mobility',
     'setter': 'update_lore_religion'},
    {'label': 'Perception', 'position': [3, 0], 'getter': 'perception',
     'setter': 'update_perception'},
    {'label': 'Persuasion', 'position': [3, 1], 'getter': 'persuasion',
     'setter': 'update_persuasion'},
    {'label': 'Stealth', 'position': [4, 0], 'getter': 'stealth',
     'setter': 'update_stealth'},
    {'label': 'Theivery', 'position': [4, 1], 'getter': 'theivery',
     'setter': 'update_theivery'},
    {'label': 'Use Magic Device', 'position': [5, 0],
     'getter': 'use_magic_device', 'setter': 'update_use_magic_device'},
]


class SkillInfoTab(Tab):
    # pylint: disable=too-many-instance-attributes, too-few-public-methods
    def __init__(self, notebook):
        super(SkillInfoTab, self).__init__(notebook)
        self._skill_fields = []
        self._instantiate_skills()
        self._notebook.add(self._panel, text="Skills")
        self._character = None
        self._panel.config()

    def load_info(self, character):
        self._character = character
        self._dirty_lock = True
        _set_fields(character.skills, self._skill_fields)
        self._dirty_lock = False
        self._panel.config()

    def _instantiate_skills(self):
        for skill in SKILLS:
            self._append_grid_field(skill, self._skill_fields,
                                    self._update_skills)

    def _update_skills(self, *args):
        # pylint: disable=unused-argument
        skills = self._character.skills
        for field in self._skill_fields:
            _update_field(field, skills, self._dirty_lock)

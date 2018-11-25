from editor.widgets.tabs.tab import Tab, _set_fields, _update_field


KINGDOM_INFO = [
    {'label': 'Kingdom Name', 'position': [0, 0], 'getter': 'kingdom_name',
     'setter': 'update_kingdom_name'},
    {'label': 'Build Points', 'position': [0, 1], 'getter': 'build_points',
     'setter': 'update_build_points'},
    {'label': 'Community', 'position': [1, 0], 'getter': 'community',
     'setter': 'update_community'},
    {'label': 'Loyalty', 'position': [1, 1], 'getter': 'loyalty',
     'setter': 'update_loyalty'},
    {'label': 'Military', 'position': [2, 0], 'getter': 'military',
     'setter': 'update_military'},
    {'label': 'Economy', 'position': [2, 1], 'getter': 'economy',
     'setter': 'update_economy'},
    {'label': 'Relations', 'position': [3, 0], 'getter': 'relations',
     'setter': 'update_relations'},
    {'label': 'Divine', 'position': [3, 1], 'getter': 'divine',
     'setter': 'update_divine'},
    {'label': 'Arcane', 'position': [4, 0], 'getter': 'arcane',
     'setter': 'update_arcane'},
    {'label': 'Stability', 'position': [4, 1], 'getter': 'stability',
     'setter': 'update_stability'},
    {'label': 'Culture', 'position': [5, 0], 'getter': 'culture',
     'setter': 'update_culture'},
    {'label': 'Espionage', 'position': [5, 1], 'getter': 'espionage',
     'setter': 'update_espionage'}
]


class KingdomInfoTab(Tab):
    # pylint: disable=too-many-instance-attributes, too-few-public-methods
    def __init__(self, notebook):
        super(KingdomInfoTab, self).__init__(notebook)
        self._kingdom_fields = []
        self._instantiate_kingdom_info()
        self._kingdom_info = None

    def load_info(self, party):
        self._kingdom_info = party.kingdom
        if self._kingdom_info.has_kingdom_data():
            self._dirty_lock = True
            _set_fields(self._kingdom_info, self._kingdom_fields)
            self._dirty_lock = False
            self._notebook.add(self._panel, text="Kingdom")
            self._panel.config()

    def _instantiate_kingdom_info(self):
        for info in KINGDOM_INFO:
            self._append_grid_field(info, self._kingdom_fields,
                                    self._update_kingdom_info)

    def _update_kingdom_info(self, *args):
        # pylint: disable=unused-argument
        for field in self._kingdom_fields:
            _update_field(field, self._kingdom_info, self._dirty_lock)

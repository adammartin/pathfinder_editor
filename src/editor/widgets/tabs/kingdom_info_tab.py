from editor.widgets.tabs.tab import Tab


class KingdomInfoTab(Tab):
    # pylint: disable=too-many-instance-attributes
    def __init__(self, notebook):
        super(KingdomInfoTab, self).__init__(notebook)
        self._kingdom_name = self._add_field(0, 0, 'Kingdom Name:', self._update_info)
        self._build_points = self._add_field(0, 1, 'Build Points:', self._update_info)
        self._community = self._add_field(1, 0, 'Community:', self._update_info)
        self._loyalty = self._add_field(1, 1, 'Loyalty:', self._update_info)
        self._military = self._add_field(2, 0, 'Military:', self._update_info)
        self._economy = self._add_field(2, 1, 'Economy:', self._update_info)
        self._relations = self._add_field(3, 0, 'Relations:', self._update_info)
        self._divine = self._add_field(3, 1, 'Divine', self._update_info)
        self._arcane = self._add_field(4, 0, 'Arcane', self._update_info)
        self._stability = self._add_field(4, 1, 'Stability:', self._update_info)
        self._culture = self._add_field(5, 0, 'Culture:', self._update_info)
        self._espionage = self._add_field(5, 1, 'Espionage:', self._update_info)
        self._kingdom_info = None

    def load_info(self, party):
        self._kingdom_info = party.kingdom
        kingdom_info = self._kingdom_info
        if kingdom_info.has_kingdom_data():
            self._dirty_lock = True
            self._kingdom_name.set(kingdom_info.kingdom_name())
            self._build_points.set(kingdom_info.build_points())
            self._community.set(kingdom_info.community())
            self._loyalty.set(kingdom_info.loyalty())
            self._military.set(kingdom_info.military())
            self._economy.set(kingdom_info.economy())
            self._relations.set(kingdom_info.relations())
            self._divine.set(kingdom_info.divine())
            self._arcane.set(kingdom_info.arcane())
            self._stability.set(kingdom_info.stability())
            self._culture.set(kingdom_info.culture())
            self._espionage.set(kingdom_info.espionage())
            self._dirty_lock = False
            self._notebook.add(self._panel, text="Kingdom")
            self._panel.config()

    def _update_info(self, *args):
        kingdom_info = self._kingdom_info
        self._update(self._kingdom_name, kingdom_info.update_kingdom_name)
        self._update(self._build_points, kingdom_info.update_build_points)
        self._update(self._community, kingdom_info.update_community)
        self._update(self._loyalty, kingdom_info.update_loyalty)
        self._update(self._military, kingdom_info.update_military)
        self._update(self._economy, kingdom_info.update_economy)
        self._update(self._relations, kingdom_info.update_relations)
        self._update(self._divine, kingdom_info.update_divine)
        self._update(self._arcane, kingdom_info.update_arcane)
        self._update(self._stability, kingdom_info.update_stability)
        self._update(self._culture, kingdom_info.update_culture)
        self._update(self._espionage, kingdom_info.update_espionage)

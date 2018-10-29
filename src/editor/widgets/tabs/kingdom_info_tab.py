from editor.widgets.tabs.tab import Tab


class KingdomInfoTab(Tab):
    # pylint: disable=too-many-instance-attributes
    def __init__(self, notebook):
        super(KingdomInfoTab, self).__init__(notebook)
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

    def load_info(self, party):
        kingdom_info = party.kingdom
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
            self._notebook.add(self._panel, text="Kingdom")
            self._panel.config()

    def update_info(self, party):
        kingdom_info = party.kingdom
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

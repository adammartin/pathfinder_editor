class SkillsInfo():
    # pylint: disable=too-many-public-methods
    def __init__(self, stat_block):
        self.stat_block = stat_block

    def athletics(self):
        return self._load_skill_value("SkillAthletics")

    def update_athletics(self, value):
        return self._update_skill_value("SkillAthletics", value)

    def knowledge_arcana(self):
        return self._load_skill_value("SkillKnowledgeArcana")

    def update_knowledge_arcana(self, value):
        return self._update_skill_value("SkillKnowledgeArcana", value)

    def knowledge_world(self):
        return self._load_skill_value("SkillKnowledgeWorld")

    def update_knowledge_world(self, value):
        return self._update_skill_value("SkillKnowledgeWorld", value)

    def lore_nature(self):
        return self._load_skill_value("SkillLoreNature")

    def update_lore_nature(self, value):
        return self._update_skill_value("SkillLoreNature", value)

    def lore_religion(self):
        return self._load_skill_value("SkillLoreReligion")

    def update_lore_religion(self, value):
        return self._update_skill_value("SkillLoreReligion", value)

    def _load_skill_value(self, skill_name):
        skill = self.stat_block[skill_name]
        if "m_BaseValue" in skill:
            return str(skill["m_BaseValue"])
        return self._load_skill_ref(skill["$ref"])

    def _update_skill_value(self, skill_name, value):
        skill = self.stat_block[skill_name]
        if self._load_skill_value(skill_name) != int(value):
            if "m_BaseValue" in skill:
                skill["m_BaseValue"] = int(value)
            else:
                self._update_skill_ref(skill["$ref"], value)

    def _load_skill_ref(self, ref):
        for struct in self.stat_block.values():
            value = _load_direct_dependent_skill_ref(ref, struct)
            if not value and "BaseStat" in struct:
                value = _load_direct_dependent_skill_ref(ref,
                                                         struct["BaseStat"])
            if value:
                return value
        return "Unknown"

    def _update_skill_ref(self, ref, value):
        for struct in self.stat_block.values():
            result = _update_direct_dependent_skills_ref(ref, struct, value)
            if not result and "BaseStat" in struct:
                result = _update_direct_dependent_skills_ref(ref,
                                                             struct["BaseStat"],
                                                             value)
            if result:
                break


def _load_direct_dependent_skill_ref(ref, struct):
    if "m_Dependents" in struct and struct["m_Dependents"]:
        for dependent in struct["m_Dependents"]:
            if "$id" in dependent and dependent["$id"] == ref:
                return str(dependent["m_BaseValue"])
    return None


def _update_direct_dependent_skills_ref(ref, struct, value):
    if "m_Dependents" in struct and struct["m_Dependents"]:
        for dependent in struct["m_Dependents"]:
            if "$id" in dependent and dependent["$id"] == ref:
                dependent["m_BaseValue"] = int(value)
                return int(value)
    return None

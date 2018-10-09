from entity_info import EntityInfo, main_character_stats
from file_utils import save_json


class SkillInfo(EntityInfo):
    # pylint: disable=too-many-public-methods
    def athletics(self):
        return self._load_skill_value("SkillAthletics")

    def knowledge_arcana(self):
        return self._load_skill_value("SkillKnowledgeArcana")

    def knowledge_world(self):
        return self._load_skill_value("SkillKnowledgeWorld")

    def lore_nature(self):
        return self._load_skill_value("SkillLoreNature")

    def lore_religion(self):
        return self._load_skill_value("SkillLoreReligion")

    def mobility(self):
        return self._load_skill_value("SkillMobility")

    def perception(self):
        return self._load_skill_value("SkillPerception")

    def persuasion(self):
        return self._load_skill_value("SkillPersuasion")

    def stealth(self):
        return self._load_skill_value("SkillStealth")

    def theivery(self):
        return self._load_skill_value("SkillThievery")

    def use_magic_device(self):
        return self._load_skill_value("SkillUseMagicDevice")

    def update_athletics(self, value):
        return self._update_skill_value("SkillAthletics", value)

    def update_knowledge_arcana(self, value):
        return self._update_skill_value("SkillKnowledgeArcana", value)

    def update_knowledge_world(self, value):
        return self._update_skill_value("SkillKnowledgeWorld", value)

    def update_lore_nature(self, value):
        return self._update_skill_value("SkillLoreNature", value)

    def update_lore_religion(self, value):
        return self._update_skill_value("SkillLoreReligion", value)

    def update_mobility(self, value):
        return self._update_skill_value("SkillMobility", value)

    def update_perception(self, value):
        return self._update_skill_value("SkillPerception", value)

    def update_persuasion(self, value):
        return self._update_skill_value("SkillPersuasion", value)

    def update_stealth(self, value):
        return self._update_skill_value("SkillStealth", value)

    def update_theivery(self, value):
        return self._update_skill_value("SkillThievery", value)

    def update_use_magic_device(self, value):
        return self._update_skill_value("SkillUseMagicDevice", value)

    def _load_skill_value(self, skill_name):
        data = self._json(self._party_json_name)
        stats = main_character_stats(data)
        skill = stats[skill_name]
        if "m_BaseValue" in skill:
            return str(skill["m_BaseValue"])
        return _load_skill_ref(skill["$ref"], stats)

    def _update_skill_value(self, skill_name, value):
        data = self._json(self._party_json_name)
        stats = main_character_stats(data)
        skill = stats[skill_name]
        if self._load_skill_value(skill_name) != int(value):
            if "m_BaseValue" in skill:
                skill["m_BaseValue"] = int(value)
            else:
                _update_skill_ref(skill["$ref"], stats, value)
            save_json(self._temp_path, self._party_json_name, data)


def _load_skill_ref(ref, stats):
    for struct in stats.values():
        value = _load_direct_dependent_skill_ref(ref, struct)
        if not value and "BaseStat" in struct:
            value = _load_direct_dependent_skill_ref(ref, struct["BaseStat"])
        if value:
            return value
    return "Unknown"


def _load_direct_dependent_skill_ref(ref, struct):
    if "m_Dependents" in struct and struct["m_Dependents"]:
        for dependent in struct["m_Dependents"]:
            if "$id" in dependent and dependent["$id"] == ref:
                return str(dependent["m_BaseValue"])
    return None


def _update_skill_ref(ref, stats, value):
    for struct in stats.values():
        result = _update_direct_dependent_skills_ref(ref, struct, value)
        if not result and "BaseStat" in struct:
            result = _update_direct_dependent_skills_ref(ref,
                                                         struct["BaseStat"],
                                                         value)
        if result:
            break


def _update_direct_dependent_skills_ref(ref, struct, value):
    if "m_Dependents" in struct and struct["m_Dependents"]:
        for dependent in struct["m_Dependents"]:
            if "$id" in dependent and dependent["$id"] == ref:
                dependent["m_BaseValue"] = int(value)
                return int(value)
    return None

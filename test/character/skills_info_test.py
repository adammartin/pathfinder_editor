import pytest
from editor.character.skills_info import SkillsInfo


STATS = pytest.helpers.main_stat_block()


def reset_data():
    STATS = pytest.helpers.main_stat_block()


@pytest.yield_fixture(autouse=True)
def run_around_tests():
    reset_data()
    yield
    reset_data()


def test_athletics():
    athletics = str(STATS['SkillAthletics']['m_BaseValue'])
    skills_info = SkillsInfo(STATS)
    assert skills_info.athletics() == str(athletics)


def test_update_athletics():
    skills_info = SkillsInfo(STATS)
    new_athletics = str(int(skills_info.athletics()) + 6)
    skills_info.update_athletics(new_athletics)
    assert skills_info.athletics() == str(new_athletics)
    assert skills_info.athletics() == str(STATS['SkillAthletics']['m_BaseValue'])


def test_knowledge_arcana():
    arcana = str(STATS['Intelligence']['m_Dependents'][0]['m_BaseValue'])
    skills_info = SkillsInfo(STATS)
    assert skills_info.knowledge_arcana() == str(arcana)


def test_update_knowledge_arcana():
    skills_info = SkillsInfo(STATS)
    arcana = str(int(skills_info.knowledge_arcana()) + 6)
    skills_info.update_knowledge_arcana(arcana)
    final_arcana = STATS['Intelligence']['m_Dependents'][0]['m_BaseValue']
    assert skills_info.knowledge_arcana() == str(arcana)
    assert skills_info.knowledge_arcana() == str(final_arcana)


def test_knowledge_world():
    world = str(STATS['Intelligence']['m_Dependents'][1]['m_BaseValue'])
    skills_info = SkillsInfo(STATS)
    assert skills_info.knowledge_world() == str(world)


def test_update_knowledge_world():
    skills_info = SkillsInfo(STATS)
    world = str(int(skills_info.knowledge_world()) + 6)
    skills_info.update_knowledge_world(world)
    final_world = STATS['Intelligence']['m_Dependents'][1]['m_BaseValue']
    assert skills_info.knowledge_world() == str(world)
    assert skills_info.knowledge_world() == str(final_world)


def test_lore_nature():
    nature = str(STATS['SaveWill']['BaseStat']['m_Dependents'][2]['m_BaseValue'])
    skills_info = SkillsInfo(STATS)
    assert skills_info.lore_nature() == str(nature)


def test_update_lore_nature():
    skills_info = SkillsInfo(STATS)
    nature = str(int(skills_info.lore_nature()) + 6)
    skills_info.update_lore_nature(nature)
    final_nature = STATS['SaveWill']['BaseStat']['m_Dependents'][2]['m_BaseValue']
    assert skills_info.lore_nature() == str(nature)
    assert skills_info.lore_nature() == str(final_nature)


def test_lore_religion():
    religion = str(STATS['SaveWill']['BaseStat']['m_Dependents'][3]['m_BaseValue'])
    skills_info = SkillsInfo(STATS)
    assert skills_info.lore_religion() == str(religion)


def test_update_lore_religion():
    skills_info = SkillsInfo(STATS)
    religion = str(int(skills_info.lore_religion()) + 6)
    skills_info.update_lore_religion(religion)
    final_religion = STATS['SaveWill']['BaseStat']['m_Dependents'][3]['m_BaseValue']
    assert skills_info.lore_nature() == str(religion)
    assert skills_info.lore_nature() == str(final_religion)


def test_mobility():
    mobility = str(STATS['Dexterity']['m_Dependents'][2]['m_BaseValue'])
    skills_info = SkillsInfo(STATS)
    assert skills_info.mobility() == str(mobility)


def test_update_mobility():
    skills_info = SkillsInfo(STATS)
    mobility = str(int(skills_info.mobility()) + 6)
    skills_info.update_mobility(mobility)
    final_mobility = STATS['Dexterity']['m_Dependents'][2]['m_BaseValue']
    assert skills_info.mobility() == str(mobility)
    assert skills_info.mobility() == str(final_mobility)


def test_perception():
    perception = str(STATS['SaveWill']['BaseStat']['m_Dependents'][1]['m_BaseValue'])
    skills_info = SkillsInfo(STATS)
    assert skills_info.perception() == str(perception)


def test_update_perception():
    skills_info = SkillsInfo(STATS)
    perception = str(int(skills_info.perception()) + 6)
    skills_info.update_perception(perception)
    final_perception = STATS['SaveWill']['BaseStat']['m_Dependents'][1]['m_BaseValue']
    assert skills_info.perception() == str(perception)
    assert skills_info.perception() == str(final_perception)


def test_persuasion():
    persuasion = str(STATS['Charisma']['m_Dependents'][0]['m_BaseValue'])
    skills_info = SkillsInfo(STATS)
    assert skills_info.persuasion() == str(persuasion)


def test_update_persuasion():
    skills_info = SkillsInfo(STATS)
    persuasion = str(int(skills_info.persuasion()) + 6)
    skills_info.update_persuasion(persuasion)
    final_persuasion = STATS['Charisma']['m_Dependents'][0]['m_BaseValue']
    assert skills_info.persuasion() == str(persuasion)
    assert skills_info.persuasion() == str(final_persuasion)


def test_stealth():
    stealth = str(STATS['Dexterity']['m_Dependents'][4]['m_BaseValue'])
    skills_info = SkillsInfo(STATS)
    assert skills_info.stealth() == str(stealth)


def test_update_stealth():
    skills_info = SkillsInfo(STATS)
    stealth = str(int(skills_info.stealth()) + 6)
    skills_info.update_stealth(stealth)
    final_stealth = STATS['Dexterity']['m_Dependents'][4]['m_BaseValue']
    assert skills_info.stealth() == str(stealth)
    assert skills_info.stealth() == str(final_stealth)


def test_theivery():
    theivery = str(STATS['Dexterity']['m_Dependents'][3]['m_BaseValue'])
    skills_info = SkillsInfo(STATS)
    assert skills_info.theivery() == str(theivery)


def test_update_theivery():
    skills_info = SkillsInfo(STATS)
    theivery = str(int(skills_info.theivery()) + 6)
    skills_info.update_theivery(theivery)
    final_theivery = STATS['Dexterity']['m_Dependents'][3]['m_BaseValue']
    assert skills_info.theivery() == str(theivery)
    assert skills_info.theivery() == str(final_theivery)


def test_use_magic_device():
    use_magic_device = str(STATS['Charisma']['m_Dependents'][1]['m_BaseValue'])
    skills_info = SkillsInfo(STATS)
    assert skills_info.use_magic_device() == str(use_magic_device)


def test_update_use_magic_device():
    skills_info = SkillsInfo(STATS)
    use_magic_device = str(int(skills_info.use_magic_device()) + 6)
    skills_info.update_use_magic_device(use_magic_device)
    final_use_magic_device = STATS['Charisma']['m_Dependents'][1]['m_BaseValue']
    assert skills_info.use_magic_device() == str(use_magic_device)
    assert skills_info.use_magic_device() == str(final_use_magic_device)

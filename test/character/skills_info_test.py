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

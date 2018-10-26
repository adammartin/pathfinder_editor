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

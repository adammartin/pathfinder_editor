import pytest
from editor.character.stat_info import StatInfo


def test_strength():
    stats = pytest.helpers.main_stat_block()
    strength = str(stats['SkillAthletics']['BaseStat']['m_BaseValue'])
    stat_info = StatInfo(stats)
    assert stat_info.strength() == str(strength)


def test_update_strength():
    stats = pytest.helpers.main_stat_block()
    strength = str(stats['SkillAthletics']['BaseStat']['m_BaseValue'])
    stat_info = StatInfo(stats)
    new_strength = str(int(stat_info.strength()) + 6)
    stat_info.update_strength(new_strength)
    assert stat_info.strength() == str(new_strength)
    assert stat_info.strength() == str(stats['SkillAthletics']['BaseStat']['m_BaseValue'])


def test_dexterity():
    stats = pytest.helpers.main_stat_block()
    dexterity = stats['Dexterity']['m_BaseValue']
    stat_info = StatInfo(stats)
    assert stat_info.dexterity() == str(dexterity)

def test_update_dexterity():
    stats = pytest.helpers.main_stat_block()
    dexterity = stats['Dexterity']['m_BaseValue']
    stat_info = StatInfo(stats)
    new_dexterity = str(int(stat_info.dexterity()) + 6)
    stat_info.update_dexterity(new_dexterity)
    assert stat_info.dexterity() == str(new_dexterity)
    assert stat_info.dexterity() == str(stats['Dexterity']['m_BaseValue'])

import pytest
from editor.character.stat_info import StatInfo


STATS = pytest.helpers.main_stat_block()


def reset_data():
    STATS = pytest.helpers.main_stat_block()


@pytest.yield_fixture(autouse=True)
def run_around_tests():
    reset_data()
    yield
    reset_data()


def test_strength():
    strength = str(STATS['SkillAthletics']['BaseStat']['m_BaseValue'])
    stat_info = StatInfo(STATS)
    assert stat_info.strength() == str(strength)


def test_update_strength():
    stat_info = StatInfo(STATS)
    new_strength = str(int(stat_info.strength()) + 6)
    stat_info.update_strength(new_strength)
    assert stat_info.strength() == str(new_strength)
    assert stat_info.strength() == str(STATS['SkillAthletics']['BaseStat']['m_BaseValue'])


def test_dexterity():
    dexterity = STATS['Dexterity']['m_BaseValue']
    stat_info = StatInfo(STATS)
    assert stat_info.dexterity() == str(dexterity)

def test_update_dexterity():
    stat_info = StatInfo(STATS)
    new_dexterity = str(int(stat_info.dexterity()) + 6)
    stat_info.update_dexterity(new_dexterity)
    assert stat_info.dexterity() == str(new_dexterity)
    assert stat_info.dexterity() == str(STATS['Dexterity']['m_BaseValue'])


def test_constitution():
    constitution = str(STATS['Constitution']['m_BaseValue'])
    stat_info = StatInfo(STATS)
    assert stat_info.constitution() == str(constitution)


def test_update_constitution():
    stat_info = StatInfo(STATS)
    new_constitution = str(int(stat_info.constitution()) + 6)
    stat_info.update_constitution(new_constitution)
    assert stat_info.constitution() == str(new_constitution)
    assert stat_info.constitution() == str(STATS['Constitution']['m_BaseValue'])


def test_intelligence():
    intelligence = str(STATS['Intelligence']['m_BaseValue'])
    stat_info = StatInfo(STATS)
    assert stat_info.intelligence() == str(intelligence)


def test_update_intelligence():
    stat_info = StatInfo(STATS)
    new_intelligence = str(int(stat_info.intelligence()) + 6)
    stat_info.update_intelligence(new_intelligence)
    assert stat_info.intelligence() == str(new_intelligence)
    assert stat_info.intelligence() == str(STATS['Intelligence']['m_BaseValue'])


def test_wisdom():
    wisdom = str(STATS['SaveWill']['BaseStat']['m_BaseValue'])
    stat_info = StatInfo(STATS)
    assert stat_info.wisdom() == str(wisdom)


def test_update_wisdom():
    stat_info = StatInfo(STATS)
    new_wisdom = str(int(stat_info.wisdom()) + 6)
    stat_info.update_wisdom(new_wisdom)
    assert stat_info.wisdom() == str(new_wisdom)
    assert stat_info.wisdom() == str(STATS['SaveWill']['BaseStat']['m_BaseValue'])


def test_charisma():
    charisma = str(STATS['Charisma']['m_BaseValue'])
    stat_info = StatInfo(STATS)
    assert stat_info.charisma() == str(charisma)


def test_update_charisma():
    stat_info = StatInfo(STATS)
    new_charisma = str(int(stat_info.charisma()) + 6)
    stat_info.update_charisma(new_charisma)
    assert stat_info.charisma() == str(new_charisma)
    assert stat_info.charisma() == str(STATS['Charisma']['m_BaseValue'])

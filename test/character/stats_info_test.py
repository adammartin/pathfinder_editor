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


def test_base_ac():
    base_ac = str(STATS['AC']['m_BaseValue'])
    stat_info = StatInfo(STATS)
    assert stat_info.base_ac() == str(base_ac)


def test_update_base_ac():
    stat_info = StatInfo(STATS)
    new_base_ac = str(int(stat_info.base_ac()) + 6)
    stat_info.update_base_ac(new_base_ac)
    assert stat_info.base_ac() == str(new_base_ac)
    assert stat_info.base_ac() == str(STATS['AC']['m_BaseValue'])


def test_add_attack_bonus():
    add_attack_bonus = str(STATS['AdditionalAttackBonus']['m_BaseValue'])
    stat_info = StatInfo(STATS)
    assert stat_info.add_attack_bonus() == str(add_attack_bonus)


def test_update_add_attack_bonus():
    stat_info = StatInfo(STATS)
    new_add_attack_bonus = str(int(stat_info.add_attack_bonus()) + 6)
    stat_info.update_add_attack_bonus(new_add_attack_bonus)
    assert stat_info.add_attack_bonus() == str(new_add_attack_bonus)
    assert stat_info.add_attack_bonus() == str(STATS['AdditionalAttackBonus']['m_BaseValue'])


def test_additional_cmb():
    additional_cmb = str(STATS['AdditionalCMB']['m_BaseValue'])
    stat_info = StatInfo(STATS)
    assert stat_info.additional_cmb() == str(additional_cmb)


def test_update_additional_cmb():
    stat_info = StatInfo(STATS)
    new_additional_cmb = str(int(stat_info.additional_cmb()) + 6)
    stat_info.update_additional_cmb(new_additional_cmb)
    assert stat_info.additional_cmb() == str(new_additional_cmb)
    assert stat_info.additional_cmb() == str(STATS['AdditionalCMB']['m_BaseValue'])


def test_additional_cmd():
    additional_cmd = str(STATS['AdditionalCMD']['m_BaseValue'])
    stat_info = StatInfo(STATS)
    assert stat_info.additional_cmd() == str(additional_cmd)


def test_update_additional_cmd():
    stat_info = StatInfo(STATS)
    new_additional_cmd = str(int(stat_info.additional_cmd()) + 6)
    stat_info.update_additional_cmd(new_additional_cmd)
    assert stat_info.additional_cmd() == str(new_additional_cmd)
    assert stat_info.additional_cmd() == str(STATS['AdditionalCMD']['m_BaseValue'])

import pytest
from unittest import mock
from unittest.mock import patch
from editor.character.companion_info import CompanionInfo
from editor.character.entity_info import BLUEPRINTS
from editor.character.search_algorithms import next_id


MAIN_CHAR_ID = '1'
COMPANION_ID = '77c11edb92ce0fd408ad96b40fd27121'
COMP_UNIT_ID = '420'
CUST_COMP_UNIT_ID = '3641'
MONEY = 1000
COMPANION_KEY = {
    '$ref': COMP_UNIT_ID
}
CUST_COMP_KEY = {
    '$ref': CUST_COMP_UNIT_ID
}


def companion(party):
    # dirty shortcut to get testing rolling
    return party['m_EntityData'][0]['Descriptor']['m_Inventory']['m_Items'][0]['Wielder']


def cust_companion(party):
    # dirty shortcut to get testing rolling
    inventory = party['m_EntityData'][0]['Descriptor']['m_Inventory']
    item = inventory['m_Items'][1]
    enchantment = item['ArmorComponent']['m_Enchantments']['m_Facts'][0]
    return enchantment['m_CurrentContext']['m_OwnerDescriptor']


def alignment_data(character):
    return character['Alignment']


def stats_data(character):
    return character['Stats']


def companion_expected_name(blueprint_id):
    comp_info = (comp_info for comp_info in BLUEPRINTS if comp_info['blueprint'] == blueprint_id)
    return next(comp_info)['name']


def test_name():
    party = pytest.helpers.party_base(MAIN_CHAR_ID, COMP_UNIT_ID, COMPANION_ID)
    character = CompanionInfo(party, COMPANION_KEY)
    assert character.name() == companion_expected_name(COMPANION_ID)


def test_companion_portrait():
    party = pytest.helpers.party_base(MAIN_CHAR_ID, COMP_UNIT_ID, COMPANION_ID)
    character = CompanionInfo(party, COMPANION_KEY)
    assert character.portrait() == None


def test_companion_update_portrait():
    party = pytest.helpers.party_base(MAIN_CHAR_ID, COMP_UNIT_ID, COMPANION_ID)
    character = CompanionInfo(party, COMPANION_KEY)
    new_portrait = 'blarg'
    assert character.portrait() != new_portrait
    character.update_portrait(new_portrait)
    assert character.portrait() == new_portrait
    assert new_portrait == companion(party)['UISettings']['m_CustomPortrait']['m_CustomPortraitId']


def test_companion_update_portrait_id():
    party = pytest.helpers.party_base(MAIN_CHAR_ID, COMP_UNIT_ID, COMPANION_ID)
    expected_id = next_id(party)
    character = CompanionInfo(party, COMPANION_KEY)
    character.update_portrait('blarg')
    assert companion(party)['UISettings']['m_CustomPortrait']['$id'] == str(expected_id)
    assert next_id(party) == expected_id+1


def test_cust_comp_name_pre_stag_lord_defeated():
    party = pytest.helpers.party_base(MAIN_CHAR_ID, COMP_UNIT_ID, COMPANION_ID, CUST_COMP_UNIT_ID)
    character = CompanionInfo(party, CUST_COMP_KEY)
    assert character.name() == 'Elizabeth'


def test_experience():
    party = pytest.helpers.party_base(MAIN_CHAR_ID, COMP_UNIT_ID, COMPANION_ID)
    progression = companion(party)['Progression']
    character = CompanionInfo(party, COMPANION_KEY)
    assert character.experience() == str(progression['Experience'])


def test_update_experience():
    party = pytest.helpers.party_base(MAIN_CHAR_ID, COMP_UNIT_ID, COMPANION_ID)
    progression = companion(party)['Progression']
    character = CompanionInfo(party, COMPANION_KEY)
    new_experience = str(int(character.experience())+1000)
    character.update_experience(new_experience)
    assert character.experience() == new_experience
    assert character.experience() == str(progression['Experience'])


@patch('editor.character.stat_info.StatInfo')
def test_stats_info(mock_stat_info):
    party = pytest.helpers.party_base(MAIN_CHAR_ID, COMP_UNIT_ID, COMPANION_ID)
    character = CompanionInfo(party, COMPANION_KEY)
    mock_stat_info.assert_called_with(stats_data(companion(party)))
    assert character.stats == mock_stat_info.return_value


@patch('editor.character.alignment_info.AlignmentInfo')
def test_alignment_info(mock_alignment_info):
    party = pytest.helpers.party_base(MAIN_CHAR_ID, COMP_UNIT_ID, COMPANION_ID)
    character = CompanionInfo(party, COMPANION_KEY)
    mock_alignment_info.assert_called_with(alignment_data(companion(party)))
    assert character.alignment == mock_alignment_info.return_value


@patch('editor.character.skills_info.SkillsInfo')
def test_skills_info(mock_skills_info):
    party = pytest.helpers.party_base(MAIN_CHAR_ID, COMP_UNIT_ID, COMPANION_ID)
    character = CompanionInfo(party, COMPANION_KEY)
    mock_skills_info.assert_called_with(stats_data(companion(party)))
    assert character.skills == mock_skills_info.return_value

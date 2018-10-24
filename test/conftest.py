pytest_plugins = ['helpers_namespace']


import pytest


@pytest.helpers.register
def player_base(money, id):
    return {
        'Money': money,
        'm_MainCharacter': {
            'm_UniqueId': id
        }
    }


@pytest.helpers.register
def main_character(character_id, companion):
    return {
        '$id': '99',
        'Descriptor': {
            'Alignment': {
                'Vector': {
                    'x': 0,
                    'y': 0
                }
            },
            'CustomName': 'Main Character',
            'Progression': {
                'Experience': 1234
            },
            'Stats': {
                '$id': '6544',
                'Charisma': {
                    '$id': '6557',
                    'm_BaseValue': 14,
                    'm_Dependents': [
                        {
                            '$id': '6559',
                            'm_BaseValue': 6
                        },
                        {
                            '$id': '6564',
                            'm_BaseValue': 0
                        }
                    ]
                },
                'Constitution': {
                    '$id': '6568',
                    'm_BaseValue': 14,
                    'm_Dependents': [
                        {
                            '$ref': '6545'
                        },
                        {
                            '$id': '6570',
                            'm_BaseValue': 5
                        }
                    ]
                },
                'Dexterity': {
                    '$id': '6571',
                    'm_BaseValue': 19,
                    'm_Dependents': [
                        {
                            '$ref': '6548'
                        },
                        {
                            '$id': '6573',
                            'm_BaseValue': 5
                        },
                        {
                            '$id': '6574',
                            'm_BaseValue': 5
                        },
                        {
                            '$id': '6576',
                            'm_BaseValue': 0
                        },
                        {
                            '$id': '6578',
                            'm_BaseValue': 2
                        },
                        {
                            '$id': '6581',
                            'm_BaseValue': 0
                        }
                    ]
                },
                'Initiative': {
                    '$ref': '6581'
                },
                'Intelligence': {
                    '$id': '6583',
                    'm_BaseValue': 12,
                    'm_Dependents': [
                        {
                            '$id': '6585',
                            'm_BaseValue': 0
                        },
                        {
                            '$id': '6587',
                            'm_BaseValue': 1
                        }
                    ]
                },
                'SaveWill': {
                    '$id': '6589',
                    'BaseStat': {
                        '$id': '6590',
                        'm_BaseValue': 16,
                        'm_Dependents': [
                            {
                                '$ref': '6589'
                            },
                            {
                                '$id': '6592',
                                'm_BaseValue': 6
                            },
                            {
                                '$id': '6594',
                                'm_BaseValue': 0
                            },
                            {
                                '$id': '6596',
                                'm_BaseValue': 0
                            }
                        ]
                    },
                    'm_BaseValue': 5
                },
                'SkillAthletics': {
                    '$id': '6598',
                    'BaseStat': {
                        '$id': '6599',
                        'm_BaseValue': 14,
                        'm_Dependents': [
                            {
                                '$ref': '6598'
                            }
                        ]
                    },
                    'm_BaseValue': 6
                },
                'SkillKnowledgeArcana': {
                    '$ref': '6585'
                },
                'SkillKnowledgeWorld': {
                    '$ref': '6587'
                },
                'SkillLoreNature': {
                    '$ref': '6594'
                },
                'SkillLoreReligion': {
                    '$ref': '6596'
                },
                'SkillMobility': {
                    '$ref': '6574'
                },
                'SkillPerception': {
                    '$ref': '6592'
                },
                'SkillPersuasion': {
                    '$ref': '6559'
                },
                'SkillStealth': {
                    '$ref': '6578'
                },
                'SkillThievery': {
                    '$ref': '6576'
                },
                'SkillUseMagicDevice': {
                    '$ref': '6564'
                },
                'Strength': {
                    '$ref': '6599'
                },
                'Wisdom': {
                    '$ref': '6590'
                }
            },
            'm_Inventory': {
                'm_Items': [
                    {
                        '$id': '19',
                        'Wielder': companion
                    }
                ]
            }
        },
        'UniqueId': character_id
    }


@pytest.helpers.register
def companion(unit_id, comp_blueprint_id):
    return {
        '$id': '20',
        'Alignment': {
            '$id': '570',
            'Vector': {
                'x': 0.707106769,
                'y': 0.707106769
            },
        },
        'Blueprint': comp_blueprint_id,
        'CustomName': '',
        'Progression': {
            '$id': '295',
            'Experience': 25243
        },
        'Stats': {
            '$id': '65',
            'Charisma': {
                '$id': '92',
                'm_BaseValue': 15,
                'm_Dependents': [
                    {
                        '$id': '94',
                        'm_BaseValue': 1
                    },
                    {
                        '$id': '99',
                        'm_BaseValue': 1
                    }
                ]
            },
            'Constitution': {
                '$id': '103',
                'm_BaseValue': 14,
                'm_Dependents': [
                    {
                        '$ref': '66'
                    },
                    {
                        '$id': '105',
                        'm_BaseValue': 1
                    }
                ]
            },
            'Dexterity': {
                '$id': '106',
                'm_BaseValue': 14,
                'm_Dependents': [
                    {
                        '$ref': '69'
                    },
                    {
                        '$id': '108',
                        'm_BaseValue': 3
                    },
                    {
                        '$id': '109',
                        'm_BaseValue': 0
                    },
                    {
                        '$id': '111',
                        'm_BaseValue': 6
                    },
                    {
                        '$id': '113',
                        'm_BaseValue': 0
                    },
                    {
                        '$id': '116',
                        'm_BaseValue': 0
                    }
                ]
            },
            'Initiative': {
                '$ref': '116'
            },
            'Intelligence': {
                '$id': '118',
                'm_BaseValue': 14,
                'm_Dependents': [
                    {
                        '$id': '120',
                        'm_BaseValue': 6
                    },
                    {
                        '$id': '122',
                        'm_BaseValue': 6
                    }
                ]
            },
            'SaveWill': {
                '$id': '124',
                'BaseStat': {
                    '$id': '125',
                    'm_BaseValue': 10,
                    'm_Dependents': [
                        {
                            '$ref': '124'
                        },
                        {
                            '$id': '127',
                            'm_BaseValue': 0
                        },
                        {
                            '$id': '129',
                            'm_BaseValue': 0
                        },
                        {
                            '$id': '131',
                            'm_BaseValue': 0
                        }
                    ]
                },
                'm_BaseValue': 6
            },
            'SkillAthletics': {
                '$id': '133',
                'BaseStat': {
                    '$id': '134',
                    'm_BaseValue': 10,
                    'm_Dependents': [
                        {
                            '$ref': '133'
                        }
                    ]
                },
                'm_BaseValue': 0
            },
            'SkillKnowledgeArcana': {
                '$ref': '120'
            },
            'SkillKnowledgeWorld': {
                '$ref': '122'
            },
            'SkillLoreNature': {
                '$ref': '129'
            },
            'SkillLoreReligion': {
                '$ref': '131'
            },
            'SkillMobility': {
                '$ref': '109'
            },
            'SkillPerception': {
                '$ref': '127'
            },
            'SkillPersuasion': {
                '$ref': '94'
            },
            'SkillStealth': {
                '$ref': '113'
            },
            'SkillThievery': {
                '$ref': '111'
            },
            'SkillUseMagicDevice': {
                '$ref': '99'
            },
            'Strength': {
                '$ref': '134'
            },
            'Wisdom': {
                '$ref': '125'
            }
        },
        'Unit': {
            '$ref': unit_id
        }
    }


@pytest.helpers.register
def party_base(main_char_id, comp_unit_id, comp_blue_print_id):
    comp = companion(comp_unit_id, comp_blue_print_id)
    return {
        'm_EntityData': [
            main_character(main_char_id, comp),
            {
                '$ref': comp_unit_id
            }
        ]
    }

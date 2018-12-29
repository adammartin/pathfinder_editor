pytest_plugins = ['helpers_namespace']


import pytest


@pytest.helpers.register
def kingdom():
    return {
        'BP': 11500,
        'KingdomName': 'Blargh',
        'Stats': {
            '$id': '1919',
            'm_Stats': [
                {
                    '$id': '1920',
                    'Rank': 1,
                    'Type': 'Community',
                    'Value': 30
                },
                {
                    '$id': '1921',
                    'Rank': 2,
                    'Type': 'Loyalty',
                    'Value': 28
                },
                {
                    '$id': '1922',
                    'Rank': 1,
                    'Type': 'Military',
                    'Value': 25
                },
                {
                    '$id': '1923',
                    'Rank': 1,
                    'Type': 'Economy',
                    'Value': 21
                },
                {
                    '$id': '1924',
                    'Rank': 0,
                    'Type': 'Relations',
                    'Value': 4
                },
                {
                    '$id': '1925',
                    'Rank': 1,
                    'Type': 'Divine',
                    'Value': 10
                },
                {
                    '$id': '1926',
                    'Rank': 0,
                    'Type': 'Arcane',
                    'Value': 3
                },
                {
                    '$id': '1927',
                    'Rank': 0,
                    'Type': 'Stability',
                    'Value': 10
                },
                {
                    '$id': '1928',
                    'Rank': 0,
                    'Type': 'Culture',
                    'Value': 5
                },
                {
                    '$id': '1929',
                    'Rank': 0,
                    'Type': 'Espionage',
                    'Value': 0
                }
            ]
        }
    }

@pytest.helpers.register
def player_base(money, id):
    return {
        'Kingdom': kingdom(),
        'Money': money,
        'm_MainCharacter': {
            'm_UniqueId': id
        }
    }


@pytest.helpers.register
def header():
    return {
        'Name': 'Quicksave3'
    }


@pytest.helpers.register
def main_stat_block():
    return {
        '$id': '6544',
        'AC': {
            '$id': '6545',
            'PermanentValue': 10,
            'Type': 'AC',
            'm_BaseValue': 10
        },
        'AdditionalAttackBonus': {
            '$id': '6546',
            'PermanentValue': 0,
            'Type': 'AdditionalAttackBonus',
            'm_BaseValue': 0
        },
        'AdditionalCMB': {
            '$id': '6547',
            'PermanentValue': 0,
            'Type': 'AdditionalCMB',
            'm_BaseValue': 0
        },
        'AdditionalCMD': {
            '$id': '6548',
            'PermanentValue': 0,
            'Type': 'AdditionalCMD',
            'm_BaseValue': 0
        },
        'AdditionalDamage': {
            '$id': '6549',
            'PermanentValue': 0,
            'Type': 'AdditionalDamage',
            'm_BaseValue': 0
        },
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
        'HitPoints': {
            '$id': '6572',
            'PermanentValue': 37,
            'Type': 'HitPoints',
            'm_BaseValue': 37
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
        'Speed': {
            '$id': '6591',
            'PermanentValue': 30,
            'Type': 'Speed',
            'm_BaseValue': 30
        },
        'Strength': {
            '$ref': '6599'
        },
        'Wisdom': {
            '$ref': '6590'
        }
    }


@pytest.helpers.register
def main_alignment(x_axis=0, y_axis=0):
    return {
        'Vector': {
            'x': x_axis,
            'y': y_axis
        },
        'm_History': [
            {
                'Position': {
                    'x': -0.713193357,
                    'y': 0.7009674
                }
            },
            {
                'Position': {
                    'x': -0.6990331,
                    'y': 0.715089262
                }
            }
        ]
    }

@pytest.helpers.register
def main_character(character_id, companion, companion2=None):
    return {
        '$id': '99',
        'Descriptor': {
            'Alignment': main_alignment(),
            'CustomName': 'Main Character',
            'Progression': {
                'Experience': 1234
            },
            'Stats': main_stat_block(),
            'UISettings': {
                '$id': '3950',
                'm_CustomPortrait': {
                    '$id': '3993',
                    'm_CustomPortraitId': 'Sorcerer_Dark'
                },
            },
            'm_Inventory': {
                'm_Items': [
                    {
                        '$id': '19',
                        'Wielder': companion
                    },
                    {
                        '$id': '3203',
                        'ArmorComponent': {
                            '$id': '3204',
                            'm_Enchantments': {
                                '$id': '3210',
                                'Owner': {
                                    '$ref': '3204'
                                },
                                'm_Facts': [
                                    {
                                        '$id': '3211',
                                        'm_CurrentContext': {
                                            '$id': '3212',
                                            'AssociatedBlueprint': 'e90c252e08035294eba39bafce76c119',
                                            'm_CasterReference': {
                                                'm_UniqueId': '0813922c-8863-4ce8-afea-6781d861e93f'
                                            },
                                            'm_OwnerDescriptor': companion2
                                        }
                                    }
                                ]
                            }
                        }
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
        'UISettings': {
            '$id': '498',
            'm_CustomPortrait': None
        },
        'Unit': {
            '$ref': unit_id
        }
    }


@pytest.helpers.register
def respec_companion(unit_id, comp_blueprint_id):
    return {
        '$id': str(unit_id),
        'Alignment': {
            '$id': '5700',
            'Vector': {
                'x': 0.707106769,
                'y': 0.707106769
            },
        },
        'Blueprint': comp_blueprint_id,
        'CustomName': '',
        'Progression': {
            '$id': '2950',
            'Experience': 25243
        },
        'Stats': {
            '$id': '650',
            'Charisma': {
                '$id': '920',
                'm_BaseValue': 15,
                'm_Dependents': [
                    {
                        '$id': '940',
                        'm_BaseValue': 1
                    },
                    {
                        '$id': '990',
                        'm_BaseValue': 1
                    }
                ]
            },
            'Constitution': {
                '$id': '1030',
                'm_BaseValue': 14,
                'm_Dependents': [
                    {
                        '$ref': '660'
                    },
                    {
                        '$id': '1050',
                        'm_BaseValue': 1
                    }
                ]
            },
            'Dexterity': {
                '$id': '1060',
                'm_BaseValue': 14,
                'm_Dependents': [
                    {
                        '$ref': '690'
                    },
                    {
                        '$id': '1080',
                        'm_BaseValue': 3
                    },
                    {
                        '$id': '1090',
                        'm_BaseValue': 0
                    },
                    {
                        '$id': '1110',
                        'm_BaseValue': 6
                    },
                    {
                        '$id': '1130',
                        'm_BaseValue': 0
                    },
                    {
                        '$id': '1160',
                        'm_BaseValue': 0
                    }
                ]
            },
            'Initiative': {
                '$ref': '1160'
            },
            'Intelligence': {
                '$id': '1180',
                'm_BaseValue': 14,
                'm_Dependents': [
                    {
                        '$id': '1200',
                        'm_BaseValue': 6
                    },
                    {
                        '$id': '1220',
                        'm_BaseValue': 6
                    }
                ]
            },
            'SaveWill': {
                '$id': '1240',
                'BaseStat': {
                    '$id': '1250',
                    'm_BaseValue': 10,
                    'm_Dependents': [
                        {
                            '$ref': '1240'
                        },
                        {
                            '$id': '1270',
                            'm_BaseValue': 0
                        },
                        {
                            '$id': '1290',
                            'm_BaseValue': 0
                        },
                        {
                            '$id': '1310',
                            'm_BaseValue': 0
                        }
                    ]
                },
                'm_BaseValue': 6
            },
            'SkillAthletics': {
                '$id': '1330',
                'BaseStat': {
                    '$id': '1340',
                    'm_BaseValue': 10,
                    'm_Dependents': [
                        {
                            '$ref': '1330'
                        }
                    ]
                },
                'm_BaseValue': 0
            },
            'SkillKnowledgeArcana': {
                '$ref': '1200'
            },
            'SkillKnowledgeWorld': {
                '$ref': '1220'
            },
            'SkillLoreNature': {
                '$ref': '1290'
            },
            'SkillLoreReligion': {
                '$ref': '1310'
            },
            'SkillMobility': {
                '$ref': '1090'
            },
            'SkillPerception': {
                '$ref': '1270'
            },
            'SkillPersuasion': {
                '$ref': '940'
            },
            'SkillStealth': {
                '$ref': '1130'
            },
            'SkillThievery': {
                '$ref': '1110'
            },
            'SkillUseMagicDevice': {
                '$ref': '990'
            },
            'Strength': {
                '$ref': '1340'
            },
            'Wisdom': {
                '$ref': '1250'
            }
        },
        'UISettings': {
            '$id': '4980',
            'm_CustomPortrait': None
        },
        'Unit': {
            '$ref': str(unit_id)
        }
    }


@pytest.helpers.register
def custom_companion(unit_id):
    return {
        '$id': '3213',
        'Alignment': {
            '$id': '3637',
            'Vector': {
                'x': -4.371139e-08,
                'y': 1.0
            },
            'm_History': [
                {
                    '$id': '3638',
                    'Position': {
                        'x': 0.0,
                        'y': 0.0
                    }
                },
                {
                    '$id': '3639',
                    'Position': {
                        'x': -4.371139e-08,
                        'y': 1.0
                    }
                }
            ],
            'm_Owner': {
                '$ref': '3213'
            }
        },
        'Blueprint': 'baaff53a675a84f4983f1e2113b24552',
        'CustomName': 'Elizabeth',
        'Progression': {
            '$id': '3439',
            'Experience': 2000,
            'Owner': {
                '$ref': '3213'
            }
        },
        'Stats': {
            '$ref': '3254'
        },
        'UISettings': {
            '$id': '3579',
            'm_CustomPortrait': {
                '$id': '3580',
                'm_CustomPortraitId': '840'
            }
        },
        'Unit': {
            '$id': unit_id
        },
        'm_Parts': {
            '$id': '3243',
            'm_Owner': {
                '$ref': '3213'
            },
            'm_Parts': [
                {
                    'Key': 'Kingmaker.UnitLogic.Parts.UnitPartEncumbrance, Assembly-CSharp, Version=0.0.0.0, Culture=neutral, PublicKeyToken=null',
                    'Value': {
                        '$id': '3246',
                        'Owner': {
                            '$ref': '3213'
                        },
                        'm_DexBonusLimiter': {
                            '$id': '3252',
                            'AppliedTo': {
                                '$id': '3253',
                                'm_Stats': {
                                    '$id': '3254',
                                    'Charisma': {
                                        '$id': '3274',
                                        'm_BaseValue': 16
                                    },
                                    'Constitution': {
                                        '$id': '3285',
                                        'm_BaseValue': 10
                                    },
                                    'Dexterity': {
                                        '$id': '3288',
                                        'm_BaseValue': 10
                                    },
                                    'Intelligence': {
                                        '$id': '3300',
                                        'm_BaseValue': 10
                                    },
                                    'Owner': {
                                        '$ref': '3213'
                                    },
                                    'SaveWill': {
                                        '$id': '3306',
                                        'BaseStat': {
                                            '$id': '3307',
                                            'm_BaseValue': 16
                                        }
                                    },
                                    'SkillAthletics': {
                                        '$id': '3318',
                                        'BaseStat': {
                                            '$id': '3319',
                                            'm_BaseValue': 10
                                        }
                                    },
                                    'Strength': {
                                        '$ref': '3319'
                                    },
                                    'Wisdom': {
                                        '$ref': '3307'
                                    }
                                }
                            }
                        }
                    }
                }
            ]
        }
    }


@pytest.helpers.register
def party_base(main_char_id, comp_unit_id, comp_blue_print_id, cust_comp_unit_id=None, respec_comp_bp_id=None, respec_companion_unit_id=None):
    comp = companion(comp_unit_id, comp_blue_print_id)
    cust_comp = custom_companion(cust_comp_unit_id)
    data = {
        'm_EntityData': [
            main_character(main_char_id, comp, cust_comp),
            {
                '$ref': comp_unit_id
            }
        ]
    }

    if respec_comp_bp_id:
        data['m_EntityData'].append(respec_companion(respec_companion_unit_id, respec_comp_bp_id))

    return data

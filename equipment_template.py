#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

from util.macro import *

'''
Attribute_Name = ["血量", "最大血量", "攻击", "防御", "冷却加速",
                "施法加速", "命中","闪避", "暴击", "抗暴", "破击", "格挡"]
'''

ETM = {
    1: {
        "part": Equip_Hat,
        "attr": {
            Quality_White: {
                "na": [{"k": 24, "v": 2}, {"k": 29, "v": 3}],
                "attr_l": [Attribute_Hp, Attribute_Defense, Attribute_Hit, Attribute_Crit_Seal, Attribute_Parry],
                "attr_v": {
                    Attribute_Hp: [121, 141],
                    Attribute_Defense: [2, 5],
                    Attribute_Hit: [1.2, 1.5],
                    Attribute_Crit_Seal: [1, 1],
                    Attribute_Parry: [2, 4]
                }
            },
            Quality_Green: {
                "na": [{"k": 13, "v": 2}, {"k": 33, "v": 3}],
                "attr_l": [Attribute_Hp, Attribute_Defense, Attribute_Hit, Attribute_Crit_Seal, Attribute_Parry],
                "attr_v": {
                    Attribute_Hp: [121, 182],
                    Attribute_Defense: [2, 8],
                    Attribute_Hit: [1.2, 1.5],
                    Attribute_Crit_Seal: [1, 1],
                    Attribute_Parry: [2, 4]
                }
            },
            Quality_Blue: {
                "na": [{"k": 29, "v": 3}],
                "attr_l": [Attribute_Hp, Attribute_Defense, Attribute_Hit, Attribute_Crit_Seal, Attribute_Parry],
                "attr_v": {
                    Attribute_Hp: [121, 220],
                    Attribute_Defense: [2, 11],
                    Attribute_Hit: [1.2, 1.5],
                    Attribute_Crit_Seal: [1, 1],
                    Attribute_Parry: [2, 4]
                }
            },
            Quality_Purple: {
                "na": [{"k": 43, "v": 3}, {"k": 11, "v": 4}],
                "attr_l": [Attribute_Hp, Attribute_Defense, Attribute_Hit, Attribute_Crit_Seal, Attribute_Parry],
                "attr_v": {
                    Attribute_Hp: [121, 240],
                    Attribute_Defense: [5, 13],
                    Attribute_Hit: [1.2, 1.5],
                    Attribute_Crit_Seal: [1, 1],
                    Attribute_Parry: [2, 4]
                }
            },
            Quality_Red: {
                "na": [{"k": 11, "v": 3}, {"k": 45, "v": 4}],
                "attr_l": [Attribute_Hp, Attribute_Defense, Attribute_Hit, Attribute_Crit_Seal, Attribute_Parry],
                "attr_v": {
                    Attribute_Hp: [121, 294],
                    Attribute_Defense: [8, 15],
                    Attribute_Hit: [1.2, 1.5],
                    Attribute_Crit_Seal: [1, 1],
                    Attribute_Parry: [2, 4]
                }
            },
            Quality_Gold: {
                "na": [{"k": 45, "v": 5}],
                "attr_l": [Attribute_Hp, Attribute_Defense, Attribute_Hit, Attribute_Crit_Seal, Attribute_Parry],
                "attr_v": {
                    Attribute_Hp: [121, 350],
                    Attribute_Defense: [10, 23],
                    Attribute_Hit: [1.2, 1.5],
                    Attribute_Crit_Seal: [1, 1],
                    Attribute_Parry: [2, 4]
                }
            }
        }
    },
    2: {
        "part": Equip_Clothes,
        "m_attr": Attribute_Hp,
        "attr": {
            Quality_White: {
                "na": [{"k": 24, "v": 1}, {"k": 29, "v": 2}],
                "attr_l": [Attribute_Defense, Attribute_Hit, Attribute_Crit_Seal, Attribute_Parry],
                "attr_v": {
                    Attribute_Hp: [121, 141],
                    Attribute_Defense: [2, 5],
                    Attribute_Hit: [1.2, 1.5],
                    Attribute_Crit_Seal: [1, 1],
                    Attribute_Parry: [2, 4]
                }
            },
            Quality_Green: {
                "na": [{"k": 13, "v": 1}, {"k": 33, "v": 2}],
                "attr_l": [Attribute_Defense, Attribute_Hit, Attribute_Crit_Seal, Attribute_Parry],
                "attr_v": {
                    Attribute_Hp: [121, 141],
                    Attribute_Defense: [2, 5],
                    Attribute_Hit: [1.2, 1.5],
                    Attribute_Crit_Seal: [1, 1],
                    Attribute_Parry: [2, 4]
                }
            },
            Quality_Blue: {
                "na": [{"k": 29, "v": 2}],
                "attr_l": [Attribute_Defense, Attribute_Hit, Attribute_Crit_Seal, Attribute_Parry],
                "attr_v": {
                    Attribute_Hp: [121, 141],
                    Attribute_Defense: [2, 5],
                    Attribute_Hit: [1.2, 1.5],
                    Attribute_Crit_Seal: [1, 1],
                    Attribute_Parry: [2, 4]
                }
            },
            Quality_Purple: {
                "na": [{"k": 43, "v": 2}, {"k": 11, "v": 3}],
                "attr_l": [Attribute_Defense, Attribute_Hit, Attribute_Crit_Seal, Attribute_Parry],
                "attr_v": {
                    Attribute_Hp: [121, 141],
                    Attribute_Defense: [2, 5],
                    Attribute_Hit: [1.2, 1.5],
                    Attribute_Crit_Seal: [1, 1],
                    Attribute_Parry: [2, 4]
                }
            },
            Quality_Red: {
                "na": [{"k": 11, "v": 2}, {"k": 45, "v": 3}],
                "attr_l": [Attribute_Defense, Attribute_Hit, Attribute_Crit_Seal, Attribute_Parry],
                "attr_v": {
                    Attribute_Hp: [121, 141],
                    Attribute_Defense: [2, 5],
                    Attribute_Hit: [1.2, 1.5],
                    Attribute_Crit_Seal: [1, 1],
                    Attribute_Parry: [2, 4]
                }
            },
            Quality_Gold: {
                "na": [{"k": 45, "v": 4}],
                "attr_l": [Attribute_Defense, Attribute_Hit, Attribute_Crit_Seal, Attribute_Parry],
                "attr_v": {
                    Attribute_Hp: [121, 141],
                    Attribute_Defense: [2, 5],
                    Attribute_Hit: [1.2, 1.5],
                    Attribute_Crit_Seal: [1, 1],
                    Attribute_Parry: [2, 4]
                }
            }
        }
    },
    3: {
        "part": Equip_Necklace,
        "attr": {
            Quality_White: {
                "na": [{"k": 24, "v": 2}, {"k": 29, "v": 3}],
                "attr_l": [Attribute_Hp, Attribute_Defense, Attribute_Hit, Attribute_Crit_Seal, Attribute_Parry],
                "attr_v": {
                    Attribute_Hp: [121, 141],
                    Attribute_Defense: [2, 5],
                    Attribute_Hit: [1.2, 1.5],
                    Attribute_Crit_Seal: [1, 1],
                    Attribute_Parry: [2, 4]
                }
            },
            Quality_Green: {
                "na": [{"k": 13, "v": 2}, {"k": 33, "v": 3}],
                "attr_l": [Attribute_Hp, Attribute_Defense, Attribute_Hit, Attribute_Crit_Seal, Attribute_Parry],
                "attr_v": {
                    Attribute_Hp: [121, 141],
                    Attribute_Defense: [2, 5],
                    Attribute_Hit: [1.2, 1.5],
                    Attribute_Crit_Seal: [1, 1],
                    Attribute_Parry: [2, 4]
                }
            },
            Quality_Blue: {
                "na": [{"k": 29, "v": 3}],
                "attr_l": [Attribute_Hp, Attribute_Defense, Attribute_Hit, Attribute_Crit_Seal, Attribute_Parry],
                "attr_v": {
                    Attribute_Hp: [121, 141],
                    Attribute_Defense: [2, 5],
                    Attribute_Hit: [1.2, 1.5],
                    Attribute_Crit_Seal: [1, 1],
                    Attribute_Parry: [2, 4]
                }
            },
            Quality_Purple: {
                "na": [{"k": 43, "v": 3}, {"k": 11, "v": 4}],
                "attr_l": [Attribute_Hp, Attribute_Defense, Attribute_Hit, Attribute_Crit_Seal, Attribute_Parry],
                "attr_v": {
                    Attribute_Hp: [121, 141],
                    Attribute_Defense: [2, 5],
                    Attribute_Hit: [1.2, 1.5],
                    Attribute_Crit_Seal: [1, 1],
                    Attribute_Parry: [2, 4]
                }
            },
            Quality_Red: {
                "na": [{"k": 11, "v": 3}, {"k": 45, "v": 4}],
                "attr_l": [Attribute_Hp, Attribute_Defense, Attribute_Hit, Attribute_Crit_Seal, Attribute_Parry],
                "attr_v": {
                    Attribute_Hp: [121, 141],
                    Attribute_Defense: [2, 5],
                    Attribute_Hit: [1.2, 1.5],
                    Attribute_Crit_Seal: [1, 1],
                    Attribute_Parry: [2, 4]
                }
            },
            Quality_Gold: {
                "na": [{"k": 45, "v": 5}],
                "attr_l": [Attribute_Hp, Attribute_Defense, Attribute_Hit, Attribute_Crit_Seal, Attribute_Parry],
                "attr_v": {
                    Attribute_Hp: [121, 141],
                    Attribute_Defense: [2, 5],
                    Attribute_Hit: [1.2, 1.5],
                    Attribute_Crit_Seal: [1, 1],
                    Attribute_Parry: [2, 4]
                }
            }
        }
    },
    4: {
        "part": Equip_Left_Weapon,
        "skill": {
            Quality_White: [{"k": 24, "v": {"id": 1, "lv": 1}}],
            Quality_Green: [{"k": 24, "v": {"id": 1, "lv": 1}}, {"k": 29, "v": {"id": 1, "lv": 2}}],
            Quality_Blue: [{"k": 24, "v": {"id": 1, "lv": 2}}, {"k": 3, "v": {"id": 1, "lv": 3}}],
            Quality_Purple: [{"k": 24, "v": {"id": 1, "lv": 3}}, {"k": 29, "v": {"id": 1, "lv": 4}}],
            Quality_Red: [{"k": 24, "v": {"id": 1, "lv": 4}}, {"k": 4, "v": {"id": 1, "lv": 5}}],
            Quality_Gold: [{"k": 24, "v": {"id": 1, "lv": 5}}]
        },
        "m_attr": Attribute_Attack,
        "attr": {
            Quality_White: {
                "na": [{"k": 24, "v": 1}, {"k": 29, "v": 2}],
                "attr_l": [Attribute_Hit, Attribute_Crit, Attribute_Wreck, Attribute_Speed2],
                "attr_v": {
                    Attribute_Attack: [17, 23],
                    Attribute_Hit: [2, 5],
                    Attribute_Crit: [1.2, 1.5],
                    Attribute_Wreck: [1, 5],
                    Attribute_Speed2: [2, 4]
                }
            },
            Quality_Green: {
                "na": [{"k": 13, "v": 1}, {"k": 33, "v": 2}],
                "attr_l": [Attribute_Hit, Attribute_Crit, Attribute_Wreck, Attribute_Speed2],
                "attr_v": {
                    Attribute_Attack: [19, 27],
                    Attribute_Hit: [2, 5],
                    Attribute_Crit: [1.2, 1.5],
                    Attribute_Wreck: [1, 1],
                    Attribute_Speed2: [2, 4]
                }
            },
            Quality_Blue: {
                "na": [{"k": 29, "v": 2}],
                "attr_l": [Attribute_Hit, Attribute_Crit, Attribute_Wreck, Attribute_Speed2],
                "attr_v": {
                    Attribute_Attack: [21, 30],
                    Attribute_Hit: [2, 5],
                    Attribute_Crit: [1.2, 1.5],
                    Attribute_Wreck: [1, 1],
                    Attribute_Speed2: [2, 4]
                }
            },
            Quality_Purple: {
                "na": [{"k": 43, "v": 3}, {"k": 11, "v": 3}],
                "attr_l": [Attribute_Attack, Attribute_Hit, Attribute_Crit, Attribute_Wreck, Attribute_Speed2],
                "attr_v": {
                    Attribute_Attack: [24, 35],
                    Attribute_Hit: [2, 5],
                    Attribute_Crit: [1.2, 1.5],
                    Attribute_Wreck: [1, 1],
                    Attribute_Speed2: [2, 4]
                }
            },
            Quality_Red: {
                "na": [{"k": 11, "v": 2}, {"k": 45, "v": 3}],
                "attr_l": [Attribute_Hit, Attribute_Crit, Attribute_Wreck, Attribute_Speed2],
                "attr_v": {
                    Attribute_Attack: [27, 38],
                    Attribute_Hit: [2, 5],
                    Attribute_Crit: [1.2, 1.5],
                    Attribute_Wreck: [1, 1],
                    Attribute_Speed2: [2, 4]
                }
            },
            Quality_Gold: {
                "na": [{"k": 45, "v": 4}],
                "attr_l": [Attribute_Hit, Attribute_Crit, Attribute_Wreck, Attribute_Speed2],
                "attr_v": {
                    Attribute_Attack: [31, 46],
                    Attribute_Hit: [2, 5],
                    Attribute_Crit: [1.2, 1.5],
                    Attribute_Wreck: [1, 1],
                    Attribute_Speed2: [2, 4]
                }
            }
        }
    },
    5: {
        "part": Equip_Right_Weapon,
        "m_attr": Attribute_Speed1,
        "attr": {
            Quality_White: {
                "na": [{"k": 24, "v": 1}, {"k": 29, "v": 2}],
                "attr_l": [Attribute_Crit, Attribute_Wreck, Attribute_Hit],
                "attr_v": {
                    Attribute_Speed1: [3, 7],
                    Attribute_Crit: [1, 4],
                    Attribute_Wreck: [2, 5],
                    Attribute_Hit: [1.2, 1.5]
                }
            },
            Quality_Green: {
                "na": [{"k": 13, "v": 1}, {"k": 33, "v": 2}],
                "attr_l": [Attribute_Crit, Attribute_Wreck, Attribute_Hit],
                "attr_v": {
                    Attribute_Speed1: [6, 11],
                    Attribute_Crit: [1, 4],
                    Attribute_Wreck: [2, 5],
                    Attribute_Hit: [1.2, 1.5]
                }
            },
            Quality_Blue: {
                "na": [{"k": 29, "v": 2}],
                "attr_l": [Attribute_Crit, Attribute_Wreck, Attribute_Hit],
                "attr_v": {
                    Attribute_Speed1: [5, 13],
                    Attribute_Crit: [2, 5],
                    Attribute_Wreck: [2, 5],
                    Attribute_Hit: [1.2, 1.5]
                }
            },
            Quality_Purple: {
                "na": [{"k": 43, "v": 2}, {"k": 11, "v": 3}],
                "attr_l": [Attribute_Crit, Attribute_Wreck, Attribute_Hit],
                "attr_v": {
                    Attribute_Speed1: [7, 15],
                    Attribute_Crit: [2, 7],
                    Attribute_Wreck: [2, 5],
                    Attribute_Hit: [1.2, 1.5]
                }
            },
            Quality_Red: {
                "na": [{"k": 11, "v": 2}, {"k": 45, "v": 3}],
                "attr_l": [Attribute_Crit, Attribute_Wreck, Attribute_Hit],
                "attr_v": {
                    Attribute_Speed1: [7, 18],
                    Attribute_Crit: [4, 6],
                    Attribute_Wreck: [2, 5],
                    Attribute_Hit: [1.2, 1.5]
                }
            },
            Quality_Gold: {
                "na": [{"k": 45, "v": 3}],
                "attr_l": [Attribute_Crit, Attribute_Wreck, Attribute_Hit],
                "attr_v": {
                    Attribute_Speed1: [5, 26],
                    Attribute_Crit: [2, 9],
                    Attribute_Wreck: [2, 5],
                    Attribute_Hit: [1.2, 1.5]
                }
            }
        }
    },
    6: {
        "part": Equip_Left_Ring,
        "skill": {
            Quality_White: [{"k": 24, "v": {"id": 2, "lv": 1}}, {"k": 56, "v": None}],
            Quality_Green: [{"k": 24, "v": {"id": 2, "lv": 1}}, {"k": 29, "v": {"id": 2, "lv": 2}}],
            Quality_Blue: [{"k": 24, "v": {"id": 2, "lv": 2}}, {"k": 3, "v": {"id": 2, "lv": 3}}],
            Quality_Purple: [{"k": 24, "v": {"id": 2, "lv": 3}}, {"k": 29, "v": {"id": 2, "lv": 4}}],
            Quality_Red: [{"k": 24, "v": {"id": 2, "lv": 4}}, {"k": 4, "v": {"id": 2, "lv": 5}}],
            Quality_Gold: [{"k": 24, "v": {"id": 2, "lv": 5}}]
        },
        "attr": {
            Quality_White: {
                "na": [{"k": 24, "v": 2}, {"k": 29, "v": 3}],
                "attr_l": [Attribute_Hp, Attribute_Defense, Attribute_Hit, Attribute_Crit_Seal, Attribute_Parry],
                "attr_v": {
                    Attribute_Hp: [121, 141],
                    Attribute_Defense: [2, 5],
                    Attribute_Hit: [1.2, 1.5],
                    Attribute_Crit_Seal: [1, 1],
                    Attribute_Parry: [2, 4]
                }
            },
            Quality_Green: {
                "na": [{"k": 13, "v": 2}, {"k": 33, "v": 3}],
                "attr_l": [Attribute_Hp, Attribute_Defense, Attribute_Hit, Attribute_Crit_Seal, Attribute_Parry],
                "attr_v": {
                    Attribute_Hp: [121, 141],
                    Attribute_Defense: [2, 5],
                    Attribute_Hit: [1.2, 1.5],
                    Attribute_Crit_Seal: [1, 1],
                    Attribute_Parry: [2, 4]
                }
            },
            Quality_Blue: {
                "na": [{"k": 29, "v": 3}],
                "attr_l": [Attribute_Hp, Attribute_Defense, Attribute_Hit, Attribute_Crit_Seal, Attribute_Parry],
                "attr_v": {
                    Attribute_Hp: [121, 141],
                    Attribute_Defense: [2, 5],
                    Attribute_Hit: [1.2, 1.5],
                    Attribute_Crit_Seal: [1, 1],
                    Attribute_Parry: [2, 4]
                }
            },
            Quality_Purple: {
                "na": [{"k": 43, "v": 3}, {"k": 11, "v": 4}],
                "attr_l": [Attribute_Hp, Attribute_Defense, Attribute_Hit, Attribute_Crit_Seal, Attribute_Parry],
                "attr_v": {
                    Attribute_Hp: [121, 141],
                    Attribute_Defense: [2, 5],
                    Attribute_Hit: [1.2, 1.5],
                    Attribute_Crit_Seal: [1, 1],
                    Attribute_Parry: [2, 4]
                }
            },
            Quality_Red: {
                "na": [{"k": 11, "v": 3}, {"k": 45, "v": 4}],
                "attr_l": [Attribute_Hp, Attribute_Defense, Attribute_Hit, Attribute_Crit_Seal, Attribute_Parry],
                "attr_v": {
                    Attribute_Hp: [121, 141],
                    Attribute_Defense: [2, 5],
                    Attribute_Hit: [1.2, 1.5],
                    Attribute_Crit_Seal: [1, 1],
                    Attribute_Parry: [2, 4]
                }
            },
            Quality_Gold: {
                "na": [{"k": 45, "v": 5}],
                "attr_l": [Attribute_Hp, Attribute_Defense, Attribute_Hit, Attribute_Crit_Seal, Attribute_Parry],
                "attr_v": {
                    Attribute_Hp: [121, 141],
                    Attribute_Defense: [2, 5],
                    Attribute_Hit: [1.2, 1.5],
                    Attribute_Crit_Seal: [1, 1],
                    Attribute_Parry: [2, 4]
                }
            }
        }
    },
    7: {
        "part": Equip_Right_Ring,
        "skill": {
            Quality_White: [{"k": 24, "v": {"id": 3, "lv": 1}}, {"k": 56, "v": None}],
            Quality_Green: [{"k": 24, "v": {"id": 3, "lv": 1}}, {"k": 29, "v": {"id": 3, "lv": 2}}],
            Quality_Blue: [{"k": 24, "v": {"id": 3, "lv": 2}}, {"k": 3, "v": {"id": 3, "lv": 3}}],
            Quality_Purple: [{"k": 24, "v": {"id": 3, "lv": 3}}, {"k": 29, "v": {"id": 3, "lv": 4}}],
            Quality_Red: [{"k": 24, "v": {"id": 3, "lv": 4}}, {"k": 4, "v": {"id": 3, "lv": 5}}],
            Quality_Gold: [{"k": 24, "v": {"id": 3, "lv": 5}}]
        },
        "attr": {
            Quality_White: {
                "na": [{"k": 24, "v": 2}, {"k": 29, "v": 3}],
                "attr_l": [Attribute_Hp, Attribute_Defense, Attribute_Hit, Attribute_Crit_Seal, Attribute_Parry],
                "attr_v": {
                    Attribute_Hp: [121, 141],
                    Attribute_Defense: [2, 5],
                    Attribute_Hit: [1.2, 1.5],
                    Attribute_Crit_Seal: [1, 1],
                    Attribute_Parry: [2, 4]
                }
            },
            Quality_Green: {
                "na": [{"k": 13, "v": 2}, {"k": 33, "v": 3}],
                "attr_l": [Attribute_Hp, Attribute_Defense, Attribute_Hit, Attribute_Crit_Seal, Attribute_Parry],
                "attr_v": {
                    Attribute_Hp: [121, 141],
                    Attribute_Defense: [2, 5],
                    Attribute_Hit: [1.2, 1.5],
                    Attribute_Crit_Seal: [1, 1],
                    Attribute_Parry: [2, 4]
                }
            },
            Quality_Blue: {
                "na": [{"k": 29, "v": 3}],
                "attr_l": [Attribute_Hp, Attribute_Defense, Attribute_Hit, Attribute_Crit_Seal, Attribute_Parry],
                "attr_v": {
                    Attribute_Hp: [121, 141],
                    Attribute_Defense: [2, 5],
                    Attribute_Hit: [1.2, 1.5],
                    Attribute_Crit_Seal: [1, 1],
                    Attribute_Parry: [2, 4]
                }
            },
            Quality_Purple: {
                "na": [{"k": 43, "v": 3}, {"k": 11, "v": 4}],
                "attr_l": [Attribute_Hp, Attribute_Defense, Attribute_Hit, Attribute_Crit_Seal, Attribute_Parry],
                "attr_v": {
                    Attribute_Hp: [121, 141],
                    Attribute_Defense: [2, 5],
                    Attribute_Hit: [1.2, 1.5],
                    Attribute_Crit_Seal: [1, 1],
                    Attribute_Parry: [2, 4]
                }
            },
            Quality_Red: {
                "na": [{"k": 11, "v": 3}, {"k": 45, "v": 4}],
                "attr_l": [Attribute_Hp, Attribute_Defense, Attribute_Hit, Attribute_Crit_Seal, Attribute_Parry],
                "attr_v": {
                    Attribute_Hp: [121, 141],
                    Attribute_Defense: [2, 5],
                    Attribute_Hit: [1.2, 1.5],
                    Attribute_Crit_Seal: [1, 1],
                    Attribute_Parry: [2, 4]
                }
            },
            Quality_Gold: {
                "na": [{"k": 45, "v": 5}],
                "attr_l": [Attribute_Hp, Attribute_Defense, Attribute_Hit, Attribute_Crit_Seal, Attribute_Parry],
                "attr_v": {
                    Attribute_Hp: [121, 141],
                    Attribute_Defense: [2, 5],
                    Attribute_Hit: [1.2, 1.5],
                    Attribute_Crit_Seal: [1, 1],
                    Attribute_Parry: [2, 4]
                }
            }
        }
    },
    8: {
        "part": Equip_Gaiter,
        "skill": {
            Quality_White: [{"k": 24, "v": {"id": 4, "lv": 1}}, {"k": 56, "v": None}],
            Quality_Green: [{"k": 24, "v": {"id": 4, "lv": 1}}, {"k": 29, "v": {"id": 4, "lv": 2}}],
            Quality_Blue: [{"k": 24, "v": {"id": 4, "lv": 2}}, {"k": 3, "v": {"id": 4, "lv": 3}}],
            Quality_Purple: [{"k": 24, "v": {"id": 4, "lv": 3}}, {"k": 29, "v": {"id": 4, "lv": 4}}],
            Quality_Red: [{"k": 24, "v": {"id": 4, "lv": 4}}, {"k": 4, "v": {"id": 4, "lv": 5}}],
            Quality_Gold: [{"k": 24, "v": {"id": 4, "lv": 5}}]
        },
        "attr": {
            Quality_White: {
                "na": [{"k": 24, "v": 2}, {"k": 29, "v": 3}],
                "attr_l": [Attribute_Hp, Attribute_Defense, Attribute_Hit, Attribute_Crit_Seal, Attribute_Parry],
                "attr_v": {
                    Attribute_Hp: [121, 141],
                    Attribute_Defense: [2, 5],
                    Attribute_Hit: [1.2, 1.5],
                    Attribute_Crit_Seal: [1, 1],
                    Attribute_Parry: [2, 4]
                }
            },
            Quality_Green: {
                "na": [{"k": 13, "v": 2}, {"k": 33, "v": 3}],
                "attr_l": [Attribute_Hp, Attribute_Defense, Attribute_Hit, Attribute_Crit_Seal, Attribute_Parry],
                "attr_v": {
                    Attribute_Hp: [121, 141],
                    Attribute_Defense: [2, 5],
                    Attribute_Hit: [1.2, 1.5],
                    Attribute_Crit_Seal: [1, 1],
                    Attribute_Parry: [2, 4]
                }
            },
            Quality_Blue: {
                "na": [{"k": 29, "v": 3}],
                "attr_l": [Attribute_Hp, Attribute_Defense, Attribute_Hit, Attribute_Crit_Seal, Attribute_Parry],
                "attr_v": {
                    Attribute_Hp: [121, 141],
                    Attribute_Defense: [2, 5],
                    Attribute_Hit: [1.2, 1.5],
                    Attribute_Crit_Seal: [1, 1],
                    Attribute_Parry: [2, 4]
                }
            },
            Quality_Purple: {
                "na": [{"k": 43, "v": 3}, {"k": 11, "v": 4}],
                "attr_l": [Attribute_Hp, Attribute_Defense, Attribute_Hit, Attribute_Crit_Seal, Attribute_Parry],
                "attr_v": {
                    Attribute_Hp: [121, 141],
                    Attribute_Defense: [2, 5],
                    Attribute_Hit: [1.2, 1.5],
                    Attribute_Crit_Seal: [1, 1],
                    Attribute_Parry: [2, 4]
                }
            },
            Quality_Red: {
                "na": [{"k": 11, "v": 3}, {"k": 45, "v": 4}],
                "attr_l": [Attribute_Hp, Attribute_Defense, Attribute_Hit, Attribute_Crit_Seal, Attribute_Parry],
                "attr_v": {
                    Attribute_Hp: [121, 141],
                    Attribute_Defense: [2, 5],
                    Attribute_Hit: [1.2, 1.5],
                    Attribute_Crit_Seal: [1, 1],
                    Attribute_Parry: [2, 4]
                }
            },
            Quality_Gold: {
                "na": [{"k": 45, "v": 5}],
                "attr_l": [Attribute_Hp, Attribute_Defense, Attribute_Hit, Attribute_Crit_Seal, Attribute_Parry],
                "attr_v": {
                    Attribute_Hp: [121, 141],
                    Attribute_Defense: [2, 5],
                    Attribute_Hit: [1.2, 1.5],
                    Attribute_Crit_Seal: [1, 1],
                    Attribute_Parry: [2, 4]
                }
            }
        }
    },
    9: {
        "part": Equip_Shoes,
        "skill": {
            Quality_White: [{"k": 24, "v": {"id": 5, "lv": 1}}, {"k": 56, "v": None}],
            Quality_Green: [{"k": 24, "v": {"id": 5, "lv": 1}}, {"k": 29, "v": {"id": 5, "lv": 2}}, {"k": 35, "v": None}],
            Quality_Blue: [{"k": 24, "v": {"id": 5, "lv": 2}}, {"k": 3, "v": {"id": 5, "lv": 3}}, {"k": 42, "v": None}],
            Quality_Purple: [{"k": 24, "v": {"id": 5, "lv": 3}}, {"k": 29, "v": {"id": 5, "lv": 4}}, {"k": 34, "v": None}],
            Quality_Red: [{"k": 24, "v": {"id": 5, "lv": 4}}, {"k": 4, "v": {"id": 5, "lv": 5}}, {"k": 45, "v": None}],
            Quality_Gold: [{"k": 24, "v": {"id": 5, "lv": 5}}, {"k": 24, "v": None}]
        },
        "attr": {
            Quality_White: {
                "na": [{"k": 24, "v": 2}, {"k": 29, "v": 3}],
                "attr_l": [Attribute_Hp, Attribute_Defense, Attribute_Hit, Attribute_Crit_Seal, Attribute_Parry],
                "attr_v": {
                    Attribute_Hp: [121, 141],
                    Attribute_Defense: [2, 5],
                    Attribute_Hit: [1.2, 1.5],
                    Attribute_Crit_Seal: [1, 1],
                    Attribute_Parry: [2, 4]
                }
            },
            Quality_Green: {
                "na": [{"k": 13, "v": 2}, {"k": 33, "v": 3}],
                "attr_l": [Attribute_Hp, Attribute_Defense, Attribute_Hit, Attribute_Crit_Seal, Attribute_Parry],
                "attr_v": {
                    Attribute_Hp: [121, 141],
                    Attribute_Defense: [2, 5],
                    Attribute_Hit: [1.2, 1.5],
                    Attribute_Crit_Seal: [1, 1],
                    Attribute_Parry: [2, 4]
                }
            },
            Quality_Blue: {
                "na": [{"k": 29, "v": 3}],
                "attr_l": [Attribute_Hp, Attribute_Defense, Attribute_Hit, Attribute_Crit_Seal, Attribute_Parry],
                "attr_v": {
                    Attribute_Hp: [121, 141],
                    Attribute_Defense: [2, 5],
                    Attribute_Hit: [1.2, 1.5],
                    Attribute_Crit_Seal: [1, 1],
                    Attribute_Parry: [2, 4]
                }
            },
            Quality_Purple: {
                "na": [{"k": 43, "v": 3}, {"k": 11, "v": 4}],
                "attr_l": [Attribute_Hp, Attribute_Defense, Attribute_Hit, Attribute_Crit_Seal, Attribute_Parry],
                "attr_v": {
                    Attribute_Hp: [121, 141],
                    Attribute_Defense: [2, 5],
                    Attribute_Hit: [1.2, 1.5],
                    Attribute_Crit_Seal: [1, 1],
                    Attribute_Parry: [2, 4]
                }
            },
            Quality_Red: {
                "na": [{"k": 11, "v": 3}, {"k": 45, "v": 4}],
                "attr_l": [Attribute_Hp, Attribute_Defense, Attribute_Hit, Attribute_Crit_Seal, Attribute_Parry],
                "attr_v": {
                    Attribute_Hp: [121, 141],
                    Attribute_Defense: [2, 5],
                    Attribute_Hit: [1.2, 1.5],
                    Attribute_Crit_Seal: [1, 1],
                    Attribute_Parry: [2, 4]
                }
            },
            Quality_Gold: {
                "na": [{"k": 45, "v": 5}],
                "attr_l": [Attribute_Hp, Attribute_Defense, Attribute_Hit, Attribute_Crit_Seal, Attribute_Parry],
                "attr_v": {
                    Attribute_Hp: [121, 141],
                    Attribute_Defense: [2, 5],
                    Attribute_Hit: [1.2, 1.5],
                    Attribute_Crit_Seal: [1, 1],
                    Attribute_Parry: [2, 4]
                }
            }
        }
    },
    10: {
        "part": Equip_Talisman,
        "skill": {
            Quality_White: [{"k": 24, "v": {"id": 7, "lv": 1}}, {"k": 2, "v": {"id": 7, "lv": 2}}],
            Quality_Green: [{"k": 24, "v": {"id": 7, "lv": 1}}, {"k": 29, "v": {"id": 7, "lv": 2}}],
            Quality_Blue: [{"k": 24, "v": {"id": 8, "lv": 1}}, {"k": 3, "v": {"id": 8, "lv": 2}}],
            Quality_Purple: [{"k": 24, "v": {"id": 8, "lv": 1}}, {"k": 29, "v": {"id": 7, "lv": 2}}],
            Quality_Red: [{"k": 24, "v": {"id": 9, "lv": 1}}, {"k": 4, "v": {"id": 9, "lv": 2}}],
            Quality_Gold: [{"k": 24, "v": {"id": 7, "lv": 1}}, {"k": 29, "v": {"id": 7, "lv": 2}}]
        }
    },
    11: {
        "part": Equip_Belt,
        "skill": {
            Quality_White: [{"k": 24, "v": {"id": 6, "lv": 1}}, {"k": 135, "v": None}],
            Quality_Green: [{"k": 24, "v": {"id": 6, "lv": 1}}, {"k": 29, "v": {"id": 6, "lv": 2}}, {"k": 135, "v": None}],
            Quality_Blue: [{"k": 24, "v": {"id": 6, "lv": 2}}, {"k": 3, "v": {"id": 6, "lv": 3}}, {"k": 135, "v": None}],
            Quality_Purple: [{"k": 24, "v": {"id": 6, "lv": 3}}, {"k": 29, "v": {"id": 6, "lv": 4}}, {"k": 135, "v": None}],
            Quality_Red: [{"k": 24, "v": {"id": 6, "lv": 4}}, {"k": 4, "v": {"id": 6, "lv": 5}}, {"k": 135, "v": None}],
            Quality_Gold: [{"k": 24, "v": {"id": 6, "lv": 5}}]
        },
        "attr": {
            Quality_White: {
                "na": [{"k": 24, "v": 2}, {"k": 29, "v": 3}],
                "attr_l": [Attribute_Hp, Attribute_Defense, Attribute_Hit, Attribute_Crit_Seal, Attribute_Parry],
                "attr_v": {
                    Attribute_Hp: [121, 141],
                    Attribute_Defense: [2, 5],
                    Attribute_Hit: [1.2, 1.5],
                    Attribute_Crit_Seal: [1, 1],
                    Attribute_Parry: [2, 4]
                }
            },
            Quality_Green: {
                "na": [{"k": 13, "v": 2}, {"k": 33, "v": 3}],
                "attr_l": [Attribute_Hp, Attribute_Defense, Attribute_Hit, Attribute_Crit_Seal, Attribute_Parry],
                "attr_v": {
                    Attribute_Hp: [121, 141],
                    Attribute_Defense: [2, 5],
                    Attribute_Hit: [1.2, 1.5],
                    Attribute_Crit_Seal: [1, 1],
                    Attribute_Parry: [2, 4]
                }
            },
            Quality_Blue: {
                "na": [{"k": 29, "v": 3}],
                "attr_l": [Attribute_Hp, Attribute_Defense, Attribute_Hit, Attribute_Crit_Seal, Attribute_Parry],
                "attr_v": {
                    Attribute_Hp: [121, 141],
                    Attribute_Defense: [2, 5],
                    Attribute_Hit: [1.2, 1.5],
                    Attribute_Crit_Seal: [1, 1],
                    Attribute_Parry: [2, 4]
                }
            },
            Quality_Purple: {
                "na": [{"k": 43, "v": 3}, {"k": 11, "v": 4}],
                "attr_l": [Attribute_Hp, Attribute_Defense, Attribute_Hit, Attribute_Crit_Seal, Attribute_Parry],
                "attr_v": {
                    Attribute_Hp: [121, 141],
                    Attribute_Defense: [2, 5],
                    Attribute_Hit: [1.2, 1.5],
                    Attribute_Crit_Seal: [1, 1],
                    Attribute_Parry: [2, 4]
                }
            },
            Quality_Red: {
                "na": [{"k": 11, "v": 3}, {"k": 45, "v": 4}],
                "attr_l": [Attribute_Hp, Attribute_Defense, Attribute_Hit, Attribute_Crit_Seal, Attribute_Parry],
                "attr_v": {
                    Attribute_Hp: [121, 141],
                    Attribute_Defense: [2, 5],
                    Attribute_Hit: [1.2, 1.5],
                    Attribute_Crit_Seal: [1, 1],
                    Attribute_Parry: [2, 4]
                }
            },
            Quality_Gold: {
                "na": [{"k": 45, "v": 5}],
                "attr_l": [Attribute_Hp, Attribute_Defense, Attribute_Hit, Attribute_Crit_Seal, Attribute_Parry],
                "attr_v": {
                    Attribute_Hp: [121, 141],
                    Attribute_Defense: [2, 5],
                    Attribute_Hit: [1.2, 1.5],
                    Attribute_Crit_Seal: [1, 1],
                    Attribute_Parry: [2, 4]
                }
            }
        }
    }
}

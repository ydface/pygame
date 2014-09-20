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
    2: {
        "part": Equip_Clothes,
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
    5: {
        "part": Equip_Right_Weapon,
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
    6: {
        "part": Equip_Left_Ring,
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
    11: {
        "part": Equip_Belt,
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

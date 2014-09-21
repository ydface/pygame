#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

from util.macro import *

#装备掉落
EPART_1_1 = [
    {"key": 14, "val": 1},
    {"key": 14, "val": 2},
    {"key": 14, "val": 3},
    {"key": 14, "val": 4},
    {"key": 14, "val": 5},
    {"key": 14, "val": 6},
    {"key": 14, "val": 7},
    {"key": 14, "val": 8},
    {"key": 14, "val": 9},
    {"key": 14, "val": 10},
    {"key": 14, "val": 11},
]

EPART_1_2 = [
    {"key": 14, "val": 1},
    {"key": 14, "val": 2},
    {"key": 14, "val": 3},
    {"key": 14, "val": 4},
    {"key": 14, "val": 5},
    {"key": 14, "val": 6},
    {"key": 14, "val": 7},
    {"key": 14, "val": 8},
    {"key": 14, "val": 9},
    {"key": 14, "val": 10},
    {"key": 14, "val": 11},
]

EPART_1_3 = [
    {"key": 14, "val": 1},
    {"key": 14, "val": 2},
    {"key": 14, "val": 3},
    {"key": 14, "val": 4},
    {"key": 14, "val": 5},
    {"key": 14, "val": 6},
    {"key": 14, "val": 7},
    {"key": 14, "val": 8},
    {"key": 14, "val": 9},
    {"key": 14, "val": 10},
    {"key": 14, "val": 11},
]

#每关三类怪， 普通， 精英，首领
MC = {
    1: {
        "attr": [168, 168, 43, 12, 5.0, 3.0, 24, 7, 0, 9, 0, 13],
        "add": 0.6,
        "exp": 13,
        "equip": [{"key": 33, "val": Quality_White}, {"key": 11, "val": Quality_Green}, {"key": 6, "val": Quality_Blue}, {"key": 77, "val": None}],
        "part": EPART_1_1,
        "name": u"炼狱小妖",
        "level": [1, 5]
    },
    2: {
        "attr": [245, 245, 67, 23, 7.0, 6.0, 32, 11, 0, 14, 0, 21],
        "add": 0.9,
        "exp": 24,
        "equip": [{"key": 8, "val": Quality_Red}, {"key": 9, "val": Quality_Purple}, {"key": 13, "val": Quality_Blue}, {"key": 32, "val": Quality_Green}, {"key": 86, "val": None}],
        "part": EPART_1_2,
        "name": u"精英炼狱魔",
        "level": [2, 7]
    },
    3: {
        "attr": [324, 324, 97, 41, 10.0, 13.0, 47, 17, 0, 22, 0, 33],
        "add": 1.3,
        "exp": 33,
        "equip": [{"key": 24, "val": Quality_Purple}, {"key": 11, "val": Quality_Red}, {"key": 3, "val": Quality_Gold}, {"key": 33, "val": Quality_Blue}, {"key": 94, "val": None}],
        "part": EPART_1_2,
        "name": u"炼狱魔王",
        "level": [3, 9]
    },
    4: {
        "attr": [462, 462, 134, 63, 10.0, 13.0, 47, 17, 0, 22, 0, 33],
        "add": 1.6,
        "exp": 33,
        "equip": [{"key": 33, "val": Quality_White}, {"key": 11, "val": Quality_Green}, {"key": 6, "val": Quality_Blue}, {"key": 77, "val": None}],
        "part": EPART_1_2,
        "name": u"炼狱魔王",
        "level": [10, 18]
    }
}

MGROUP_1_1 = [
    {"key": 86, "val": [1, 1, 1]},
    {"key": 53, "val": [1, 1, 2]},
    {"key": 13, "val": [1, 2, 2]},
    {"key": 11, "val": [1, 2, 3]},
    {"key": 9, "val": [2, 2, 3]},
    {"key": 7, "val": [2, 3, 3]},
    {"key": 3, "val": [3, 3, 3]}
]

MGROUP_1_2 = [
    {"key": 6, "val": [1, 1, 1]},
    {"key": 9, "val": [1, 1, 2]},
    {"key": 94, "val": [1, 2, 2]},
    {"key": 43, "val": [1, 2, 3]},
    {"key": 7, "val": [2, 2, 3]},
    {"key": 5, "val": [2, 3, 3]},
    {"key": 3, "val": [3, 3, 3]}
]

MGROUP_1_3 = [
    {"key": 3, "val": [1, 1, 1]},
    {"key": 2, "val": [1, 1, 2]},
    {"key": 5, "val": [1, 2, 2]},
    {"key": 78, "val": [1, 2, 3]},
    {"key": 56, "val": [2, 2, 3]},
    {"key": 29, "val": [2, 3, 3]},
    {"key": 23, "val": [3, 3, 3]}
]

MN = [
    {"key": 145, "val": MGROUP_1_1},
    {"key": 18, "val": MGROUP_1_2},
    {"key": 5, "val": MGROUP_1_3},
]

LMN = {
    1: MN
}



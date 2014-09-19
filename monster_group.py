#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

from util.macro import *

#每关三类怪， 普通， 精英，首领
MC = {
    1: {
        "attr": [168, 168, 86, 23, 5.0, 3.0, 0, 0, 0, 0, 0, 0],
        "add": 0.6,
        "exp": 3,
        "equip": [{"key": 33, "val": Quality_White}, {"key": 11, "val": Quality_Green}, {"key": 3, "val": Quality_Blue}, {"key": 57, "val": None}],
        "name": u"炼狱小妖"
    },
    2: {
        "attr": [245, 245, 103, 15, 0.0, 0.0, 0, 0, 0, 0, 0, 0],
        "add": 0.9,
        "exp": 5,
        "equip": [{"key": 2, "val": Quality_Red}, {"key": 4, "val": Quality_Purple}, {"key": 13, "val": Quality_Blue}, {"key": 32, "val": Quality_Green}, {"key": 45, "val": None}],
        "name": u"精英炼狱魔"
    },
    3: {
        "attr": [324, 324, 150, 41, 0.0, 0.0, 0, 0, 0, 0, 0, 0],
        "add": 1.3,
        "exp": 8,
        "equip": [{"key": 24, "val": Quality_Purple}, {"key": 11, "val": Quality_Red}, {"key": 3, "val": Quality_Gold}, {"key": 33, "val": Quality_Blue}, {"key": 38, "val": None}],
        "name": u"炼狱魔王"
    }
}

MGROUP_1_1 = [
    {"key": 56, "val": [1, 1, 1]},
    {"key": 32, "val": [1, 1, 2]},
    {"key": 16, "val": [1, 2, 2]},
    {"key": 13, "val": [1, 2, 3]},
    {"key": 11, "val": [2, 2, 3]},
    {"key": 9, "val": [2, 3, 3]},
    {"key": 3, "val": [3, 3, 3]}
]

MGROUP_1_2 = [
    {"key": 6, "val": [1, 1, 1]},
    {"key": 9, "val": [1, 1, 2]},
    {"key": 35, "val": [1, 2, 2]},
    {"key": 43, "val": [1, 2, 3]},
    {"key": 11, "val": [2, 2, 3]},
    {"key": 13, "val": [2, 3, 3]},
    {"key": 12, "val": [3, 3, 3]}
]

MGROUP_1_3 = [
    {"key": 3, "val": [1, 1, 1]},
    {"key": 2, "val": [1, 1, 2]},
    {"key": 5, "val": [1, 2, 2]},
    {"key": 13, "val": [1, 2, 3]},
    {"key": 11, "val": [2, 2, 3]},
    {"key": 29, "val": [2, 3, 3]},
    {"key": 23, "val": [3, 3, 3]}
]

MN = [
    {"key": 60, "val": MGROUP_1_1},
    {"key": 30, "val": MGROUP_1_2},
    {"key": 10, "val": MGROUP_1_3},
]

LMN = {
    1: MN
}
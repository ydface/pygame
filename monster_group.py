#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

from util.macro import *

MC = {
    1: {
        "attr": [75, 75, 86, 23, 0.0, 0.0, 0, 0, 0, 0, 0, 0],
        "add": 0.6,
        "exp": 3,
        "equip": [{"key": 35, "val": Quality_White}, {"key": 5, "val": Quality_Green}, {"key": 3, "val": Quality_Blue}, {"key": 57, "val": None}]
    },
    2: {
        "attr": [43, 43, 103, 15, 0.0, 0.0, 0, 0, 0, 0, 0, 0],
        "add": 0.9,
        "exp": 5,
        "equip": [{"key": 35, "val": Quality_White}, {"key": 5, "val": Quality_Green}, {"key": 3, "val": Quality_Blue}, {"key": 57, "val": None}]
    },
    3: {
        "attr": [115, 115, 46, 41, 0.0, 0.0, 0, 0, 0, 0, 0, 0],
        "add": 1.3,
        "exp": 8,
        "equip": [{"key": 35, "val": Quality_White}, {"key": 5, "val": Quality_Green}, {"key": 3, "val": Quality_Blue}, {"key": 57, "val": None}]
    },
    4: {
        "attr": [42, 42, 38, 69, 0.0, 0.0, 0, 0, 0, 0, 0, 0],
        "add": 1.7,
        "exp": 9,
        "equip": [{"key": 35, "val": Quality_White}, {"key": 5, "val": Quality_Green}, {"key": 3, "val": Quality_Blue}, {"key": 57, "val": None}]
    },
    5: {
        "attr": [386, 386, 112, 95, 0.0, 0.0, 0, 0, 0, 0, 0, 0],
        "add": 2.4,
        "exp": 14,
        "equip": [{"key": 35, "val": Quality_White}, {"key": 5, "val": Quality_Green}, {"key": 3, "val": Quality_Blue}, {"key": 57, "val": None}]
    }
}

MGROUP_1_1 = [
    {"key": 21, "val": [1, 1, 2]},
    {"key": 19, "val": [2, 1, 2]},
    {"key": 16, "val": [3, 2, 2]},
    {"key": 13, "val": [1, 4, 2]},
    {"key": 11, "val": [4, 4, 3]},
    {"key": 9, "val": [3, 5, 2]},
    {"key": 3, "val": [5, 5, 2]}
]

MGROUP_1_2 = [
    {"key": 9, "val": [1, 1, 2]},
    {"key": 9, "val": [1, 1, 2]},
    {"key": 9, "val": [1, 1, 2]},
    {"key": 9, "val": [1, 1, 2]},
    {"key": 9, "val": [1, 1, 2]},
    {"key": 9, "val": [1, 1, 2]},
    {"key": 9, "val": [1, 1, 2]}
]

MGROUP_1_3 = [
    {"key": 9, "val": [1, 1, 2]},
    {"key": 9, "val": [1, 1, 2]},
    {"key": 9, "val": [1, 1, 2]},
    {"key": 9, "val": [1, 1, 2]},
    {"key": 9, "val": [1, 1, 2]},
    {"key": 9, "val": [1, 1, 2]},
    {"key": 9, "val": [1, 1, 2]}
]

MN = [
    {"key": 60, "val": MGROUP_1_1},
    {"key": 30, "val": MGROUP_1_2},
    { "key": 10, "val": MGROUP_1_3},
]

LMN = {
    1: MN
}
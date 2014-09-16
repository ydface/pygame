#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'


class Attribute(object):
    def __init__(self):
        super(Attribute, self).__init__()
        self.level = 1
        self.hp = 1
        self.max_hp = 1
        self.attack = 1
        self.defense = 0
        self.speed1 = 0
        self.speed2 = 0
        self.hit = 0
        self.dodge = 0
        self.crit = 0
        self.crit_seal = 0
        self.parry = 0
        self.wreck = 0
        self.anger = 0
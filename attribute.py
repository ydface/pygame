#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'


class Attribute(object):
    def __init__(self):
        super(Attribute, self).__init__()
        self.level = 1
        self.attack = 1
        self.defense = 50
        self.speed = 1
        self.hp = 1
        self.max_hp = 1
        self.crit = 0
        self.parry = 0

    def recover_hp(self, val):
        if self.hp + val > self.max_hp:
            self.hp = self.max_hp
        else:
            self.hp += val
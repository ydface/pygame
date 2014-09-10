#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import pygame, sys, pygame.mixer
from pygame.locals import *
import mypygame
import random
screen = mypygame.screen

class BattleUnit(object):
    def __init__(self, level):
        self.hp = 1000 + level * 100
        self.attack = 100 + level * 20

    def __add__(self, other):
        self.hp -= other.attack
        return self

class Battle(object):
    def __init__(self, level):
        num = random.randint(2, 5)

        self.monsters = []
        for i in range(0, num):
            self.monsters.append(BattleUnit(1))
        self.player = BattleUnit(2)

    def update(self):
        for unit in self.monsters:
            print unit
            unit = unit + self.player
            print unit.hp
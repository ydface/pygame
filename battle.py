#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import pygame, sys, pygame.mixer
from pygame.locals import *
import mypygame

screen = mypygame.screen

class BattleUnit(object):
    def __init__(self, level):
        self.hp = 1000 + level * 100
        self.attack = 100 + level * 20


class Battle(object):
    def __init__(self, level):
        pass

    def update(self):
        pass
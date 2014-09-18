#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import pygame
from pygame.locals import *
import mypygame
import util.node
from util.node import *
import button
import gamestate
import resource
import battle
import label
import game_ui.mission_map
import game_ui.attribute_ui
import game_ui.bag_ui
import game_ui.skill_ui

screen = mypygame.screen
screenwidth = mypygame.screenwidth
screenheight = mypygame.screenheight

class PlayerInfoButton(button.Button):
    def __init__(self, father):
        image = resource.getImage("player")
        pos = (screenwidth - 100 - 60 - 60, screenheight - 80)

        super(PlayerInfoButton, self).__init__(pos, image, None, father)
        self.attribute = None

    def click_up_effect(self):
        if not self.attribute:
            self.attribute = game_ui.attribute_ui.AttributeUI(layer=2)
            self.father.add(self.attribute)
        else:
            self.father.remove(self.attribute)
            self.attribute = None


class BagButton(button.Button):
    def __init__(self, father):
        image = resource.getImage("bag")
        pos = (screenwidth - 100 - 60, screenheight - 80)

        super(BagButton, self).__init__(pos, image, None, father)
        self.bag = None

    def click_up_effect(self):
        if not self.bag:
            self.bag = game_ui.bag_ui.BagUI(layer=2)
            self.father.add(self.bag)
        else:
            self.father.remove(self.bag)
            self.bag = None

class SkillButton(button.Button):
    def __init__(self, father):
        image = resource.getImage("bag")
        pos = (screenwidth - 100, screenheight - 80)

        super(SkillButton, self).__init__(pos, image, None, father)
        #self.skill = None

    def click_up_effect(self):
        if not self.father.has_ctype_child(game_ui.skill_ui.SkillUI):
            skill = game_ui.skill_ui.SkillUI(layer=2)
            self.father.add(skill)
        else:
            self.father.remove_ctype_child(game_ui.skill_ui.SkillUI)
            #self.skill = None


class UIGame(util.node.Node):
    def __init__(self):
        super(UIGame, self).__init__(event=Event_Type_Child)

        gamestate.SenceLevel = gamestate.LEVEL_0

        self.add(PlayerInfoButton(self))
        self.add(BagButton(self))
        self.add(SkillButton(self))

        self.mission_map = game_ui.mission_map.MissionMapUI(self, layer=3)
        self.add(self.mission_map)


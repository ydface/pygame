#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import pygame
from pygame.locals import *
import mypygame
import util.node
import button
import gamestate
import resource
import battle
import label
import game_ui.mission_map
import game_ui.attribute_ui
import game_ui.bag_ui

screen = mypygame.screen
screenwidth = mypygame.screenwidth
screenheight = mypygame.screenheight

LayerButton = gamestate.LayerButton
LayerLabel = gamestate.LayerLabel
LayerUI = gamestate.LayerUI

class PlayerInfoButton(button.Button):
    def __init__(self, father):
        image = resource.getImage("player")
        rect = Rect(screenwidth - 100 - 60, screenheight - 80, image.get_width(), image.get_height())

        button.Button.__init__(self, rect, image, None, father)
        self.ui_view = False

    def click_up_effect(self):
        if not self.ui_view:
            attribute = game_ui.attribute_ui.AttributeUI(2)
            self.father.layer_child[LayerUI]["attribute"] = attribute
            self.ui_view = True
            self.father.layer_child[LayerUI]["mission_map"].event_enable = False
        else:
            del self.father.layer_child[LayerUI]["attribute"]
            self.ui_view = False
            self.father.layer_child[LayerUI]["mission_map"].event_enable = True

class BagButton(button.Button):
    def __init__(self, father):
        image = resource.getImage("bag")
        rect = Rect(screenwidth - 100, screenheight - 80, image.get_width(), image.get_height())

        button.Button.__init__(self, rect, image, None, father)
        self.ui_view = False

    def click_up_effect(self):
        if not self.ui_view:
            bag = game_ui.bag_ui.BagUI(2)
            self.father.layer_child[LayerUI]["bag"] = bag
            self.ui_view = True
            self.father.layer_child[LayerUI]["mission_map"].event_enable = False
        else:
            del self.father.layer_child[LayerUI]["bag"]
            self.ui_view = False
            self.father.layer_child[LayerUI]["mission_map"].event_enable = True

class UIGame(util.node.Node):
    def __init__(self):
        util.node.Node.__init__(self)

        gamestate.SenceLevel = gamestate.LEVEL_0

        self.battle = None

        player_btn = PlayerInfoButton(self)
        self.layer_child[LayerButton]["user_info"] = player_btn

        bag_btn = BagButton(self)
        self.layer_child[LayerButton]["bag"] = bag_btn

        mission_map = game_ui.mission_map.MissionMapUI(self, 1)
        self.layer_child[LayerUI]["mission_map"] = mission_map


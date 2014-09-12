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

screen = mypygame.screen
screenwidth = mypygame.screenwidth
screenheight = mypygame.screenheight

LayerButton = gamestate.LayerButton
LayerLabel = gamestate.LayerLabel
LayerUI = gamestate.LayerUI

class PlayerInfoButton(button.Button):
    def __init__(self, rect, normal_image, select_image, father):
        button.Button.__init__(self, rect, normal_image, select_image, father)
        self.attribute_view = False

    def click_up_effect(self):
        if not self.attribute_view:
            attribute = game_ui.attribute_ui.AttributeUI(2)
            self.father.layer_child[LayerUI]["attribute"] = attribute
            self.attribute_view = True
            self.father.layer_child[LayerUI]["mission_map"].event_enable = False
        else:
            del self.father.layer_child[LayerUI]["attribute"]
            self.attribute_view = False
            self.father.layer_child[LayerUI]["mission_map"].event_enable = True

class UIGame(util.node.Node):
    def __init__(self):
        util.node.Node.__init__(self)

        gamestate.SenceLevel = gamestate.LEVEL_0

        self.battle = None

        player_image = resource.getImage("player")
        player_btn_rect = Rect(screenwidth - 100, screenheight - 80, player_image.get_width(), player_image.get_height())
        player_btn = PlayerInfoButton(player_btn_rect, player_image, None, self)
        self.layer_child[LayerButton]["user_info"] = player_btn

        mission_map = game_ui.mission_map.MissionMapUI(self, 1)
        self.layer_child[LayerUI]["mission_map"] = mission_map


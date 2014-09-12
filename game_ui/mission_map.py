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

screen = mypygame.screen
screenwidth = mypygame.screenwidth
screenheight = mypygame.screenheight

LayerButton = gamestate.LayerButton
LayerLabel = gamestate.LayerLabel
LayerUI = gamestate.LayerUI


class LevelButton1(button.Button):
    def __init__(self, father):
        image1 = resource.getImage("level_1_1")
        image1 = pygame.transform.scale(image1,(image1.get_width() / 2, image1.get_height() / 2))

        image0 = resource.getImage("level_1_0")
        image0 = pygame.transform.scale(image0,(image0.get_width() / 2, image0.get_height() / 2))

        rect = Rect(163, 111, image0.get_width(), image0.get_height())
        button.Button.__init__(self, rect, image1, image0, father)

    def click_up_effect(self):
        gamestate.SenceLevel = gamestate.LEVEL_1
        gamestate.current_ui = battle.Battle(3,None)

class LevelButton2(button.Button):
    def __init__(self, father):
        image1 = resource.getImage("level_2_1")
        image1 = pygame.transform.scale(image1,(image1.get_width() / 2, image1.get_height() / 2))

        image0 = resource.getImage("level_2_0")
        image0 = pygame.transform.scale(image0,(image0.get_width() / 2, image0.get_height() / 2))

        rect = Rect(100, 104, image0.get_width(), image0.get_height())

        button.Button.__init__(self, rect, image1, image0, father)

    def click_up_effect(self):
        gamestate.SenceLevel = gamestate.LEVEL_2
        gamestate.current_ui = battle.Battle(3,None)

class LevelButton3(button.Button):
    def __init__(self, father):
        image1 = resource.getImage("level_3_1")
        image1 = pygame.transform.scale(image1,(image1.get_width() / 2, image1.get_height() / 2))

        image0 = resource.getImage("level_3_0")
        image0 = pygame.transform.scale(image0,(image0.get_width() / 2, image0.get_height() / 2))

        rect = Rect(100, 160, image0.get_width(), image0.get_height())

        button.Button.__init__(self, rect, image1, image0, father)

    def click_up_effect(self):
        gamestate.SenceLevel = gamestate.LEVEL_3
        gamestate.current_ui = battle.Battle(3,None)

base_offest = 200

class MissionMapUI(util.node.Node):
    def __init__(self, father, zorder):
        util.node.Node.__init__(self, zorder)

        self.father = father

        self.offest = 0

        background = resource.getImage("big_map")
        self.background = pygame.transform.scale(background,(background.get_width() / 2, background.get_height() / 2))

        background_side = resource.getImage("map_key")
        self.background_side = pygame.transform.scale(background_side,(background_side.get_width() / 2, background_side.get_height() / 2))

        self.layer_child[LayerButton]["level_1"] = LevelButton1(self)
        self.layer_child[LayerButton]["level_2"] = LevelButton2(self)
        self.layer_child[LayerButton]["level_3"] = LevelButton3(self)

    def draw_self(self):
        if gamestate.SenceLevel == gamestate.LEVEL_0:
            screen.blit(self.background_side, (base_offest + self.background.get_width(), 10))
            screen.set_clip(base_offest + 3 + self.background.get_width() - self.offest, 20, self.offest, self.background.get_height())
            screen.blit(self.background, (base_offest + self.background.get_width() - self.offest, 20))

            for dc in self.layer_child:
                for c in self.layer_child[dc]:
                    self.layer_child[dc][c].draw_self()

            screen.set_clip((0, 0, mypygame.screenwidth, mypygame.screenwidth))

            screen.blit(self.background_side, (base_offest + 6 + self.background.get_width() - self.offest - self.background_side.get_width(), 10))

    def update(self):
        if gamestate.SenceLevel == gamestate.LEVEL_0:
            if self.offest < self.background.get_width() - 3:
                self.event_enable = False
                self.offest = self.offest + 3
                if self.offest > self.background.get_width():
                    self.offest = self.background.get_width() - 3
                if self.offest > 136 - self.layer_child[LayerButton]["level_1"].draw_image.get_width():
                    self.layer_child[LayerButton]["level_1"].rect[0] = base_offest + self.background.get_width() + 5 + 2*self.layer_child[LayerButton]["level_1"].draw_image.get_width()/3 - self.offest
                if self.offest > 290 - self.layer_child[LayerButton]["level_2"].draw_image.get_width():
                    self.layer_child[LayerButton]["level_2"].rect[0] = base_offest + 168 + self.background.get_width() + 5 + self.layer_child[LayerButton]["level_2"].draw_image.get_width() - self.offest
                if self.offest > 21 - self.layer_child[LayerButton]["level_3"].draw_image.get_width():
                    self.layer_child[LayerButton]["level_3"].rect[0] = base_offest - 75 + self.background.get_width() + 5 + self.layer_child[LayerButton]["level_3"].draw_image.get_width() - self.offest
            else:
                self.event_enable = True
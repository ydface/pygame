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
    def __init__(self, rect, normal_image, select_image, father):
        button.Button.__init__(self, rect, normal_image, select_image, father)

    def click_up_effect(self):
        gamestate.SenceLevel = gamestate.LEVEL_1
        gamestate.current_ui = battle.Battle(3,None)
        #del self.father.father.layer_child[LayerUI]["mission_map"]

class LevelButton2(button.Button):
    def __init__(self, rect, normal_image, select_image, father):
        button.Button.__init__(self, rect, normal_image, select_image, father)

    def click_up_effect(self):
        gamestate.SenceLevel = gamestate.LEVEL_2
        gamestate.current_ui = battle.Battle(3,None)
        #del self.father.father.layer_child[LayerUI]["mission_map"]

class LevelButton3(button.Button):
    def __init__(self, rect, normal_image, select_image, father):
        button.Button.__init__(self, rect, normal_image, select_image, father)

    def click_up_effect(self):
        gamestate.SenceLevel = gamestate.LEVEL_3
        gamestate.current_ui = battle.Battle(3,None)
        #del self.father.father.layer_child[LayerUI]["mission_map"]

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

        self.levelBtn1Rect = Rect(163,111,resource.getImage("level_1_0").get_width() / 2, resource.getImage("level_1_0").get_height() / 2)
        imageLevel11 = pygame.transform.scale(resource.getImage("level_1_1"),( resource.getImage("level_1_1").get_width() /2, resource.getImage("level_1_1").get_height() / 2))
        imageLevel10 = pygame.transform.scale(resource.getImage("level_1_0"),( resource.getImage("level_1_0").get_width() /2, resource.getImage("level_1_0").get_height() / 2))
        self.layer_child[LayerButton]["level_1"] = LevelButton1(self.levelBtn1Rect, imageLevel11, imageLevel10, self)

        self.levelBtn2Rect = Rect(100, 104,resource.getImage("level_2_0").get_width() / 2, resource.getImage("level_2_0").get_height() / 2)
        imageLevel21 = pygame.transform.scale(resource.getImage("level_2_1"),( resource.getImage("level_2_1").get_width() /2, resource.getImage("level_2_1").get_height() / 2))
        imageLevel20 = pygame.transform.scale(resource.getImage("level_2_0"),( resource.getImage("level_2_0").get_width() /2, resource.getImage("level_2_0").get_height() / 2))
        self.layer_child[LayerButton]["level_2"] = LevelButton2(self.levelBtn2Rect, imageLevel21, imageLevel20, self)

        self.levelBtn3Rect = Rect(100, 160,resource.getImage("level_3_0").get_width() / 2, resource.getImage("level_3_0").get_height() / 2)
        imageLevel31 = pygame.transform.scale(resource.getImage("level_3_1"),( resource.getImage("level_3_1").get_width() /2, resource.getImage("level_3_1").get_height() / 2))
        imageLevel30 = pygame.transform.scale(resource.getImage("level_3_0"),( resource.getImage("level_3_0").get_width() /2, resource.getImage("level_3_0").get_height() / 2))
        self.layer_child[LayerButton]["level_3"] = LevelButton3(self.levelBtn3Rect, imageLevel31, imageLevel30, self)

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
                self.offest = self.offest + 3
                if self.offest > self.background.get_width():
                    self.offest = self.background.get_width() - 3
                if self.offest > 136 - self.layer_child[LayerButton]["level_1"].draw_image.get_width():
                    self.layer_child[LayerButton]["level_1"].rect[0] = base_offest + self.background.get_width() + 5 + 2*self.layer_child[LayerButton]["level_1"].draw_image.get_width()/3 - self.offest
                if self.offest > 290 - self.layer_child[LayerButton]["level_2"].draw_image.get_width():
                    self.layer_child[LayerButton]["level_2"].rect[0] = base_offest + 168 + self.background.get_width() + 5 + self.layer_child[LayerButton]["level_2"].draw_image.get_width() - self.offest
                if self.offest > 21 - self.layer_child[LayerButton]["level_3"].draw_image.get_width():
                    self.layer_child[LayerButton]["level_3"].rect[0] = base_offest - 75 + self.background.get_width() + 5 + self.layer_child[LayerButton]["level_3"].draw_image.get_width() - self.offest
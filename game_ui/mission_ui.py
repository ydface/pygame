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

LayerButton = gamestate.LayerButton
LayerLabel = gamestate.LayerLabel
LayerUI = gamestate.LayerUI

class LevelButton1(button.Button):
    def __init__(self, rect, normal_image, select_image, father):
        button.Button.__init__(self, rect, normal_image, select_image, father)

    def clickUpEffect(self):
        gamestate.SenceLevel = gamestate.LEVEL_1

class LevelButton2(button.Button):
    def __init__(self, rect, normal_image, select_image, father):
        button.Button.__init__(self, rect, normal_image, select_image, father)

    def clickUpEffect(self):
        gamestate.SenceLevel = gamestate.LEVEL_2

class LevelButton3(button.Button):
    def __init__(self, rect, normal_image, select_image, father):
        button.Button.__init__(self, rect, normal_image, select_image, father)

    def clickUpEffect(self):
        gamestate.SenceLevel = gamestate.LEVEL_3

baseOffest = 200
class PlayerInfoButton(button.Button):
    def __init__(self, rect, normal_image, select_image, father):
        button.Button.__init__(self, rect, normal_image, select_image, father)

    def clickUpEffect(self):
        #screen.blit(resource.getImage("attribute"), (0, 0))
        gamestate.SenceLevel = gamestate.LEVEL_0
        self.father.battle = None
        self.father.labels.clear()

class UIGame(util.node.Node):
    def __init__(self):
        util.node.Node.__init__(self)

        self.battle = None

        playerBtnRect = Rect(mypygame.screenwidth - 100, mypygame.screenheight - 80, resource.getImage("player").get_width(), resource.getImage("player").get_height())
        #playerBtn = PlayerInfoButton(self.playerBtnRect, resource.getImage("player"), None, self)
        self.layer_child[LayerButton]["user_info"] = PlayerInfoButton(playerBtnRect, resource.getImage("player"), None, self)

        self.battleMap = resource.getImage("big_map")
        self.battleMap = pygame.transform.scale(self.battleMap,( self.battleMap.get_width() / 2, self.battleMap.get_height() / 2))

        self.mapKey = resource.getImage("map_key")
        self.mapKey = pygame.transform.scale(self.mapKey,( self.mapKey.get_width() /2, self.mapKey.get_height() / 2))
        self.mapOffest = 0

        self.levelBtn1Rect = Rect(163,111,resource.getImage("level_1_0").get_width() / 2, resource.getImage("level_1_0").get_height() / 2)
        imageLevel11 = pygame.transform.scale(resource.getImage("level_1_1"),( resource.getImage("level_1_1").get_width() /2, resource.getImage("level_1_1").get_height() / 2))
        imageLevel10 = pygame.transform.scale(resource.getImage("level_1_0"),( resource.getImage("level_1_0").get_width() /2, resource.getImage("level_1_0").get_height() / 2))
        self.levelBtn1 = LevelButton1(self.levelBtn1Rect, imageLevel11, imageLevel10, self)

        self.levelBtn2Rect = Rect(100, 104,resource.getImage("level_2_0").get_width() / 2, resource.getImage("level_2_0").get_height() / 2)
        imageLevel21 = pygame.transform.scale(resource.getImage("level_2_1"),( resource.getImage("level_2_1").get_width() /2, resource.getImage("level_2_1").get_height() / 2))
        imageLevel20 = pygame.transform.scale(resource.getImage("level_2_0"),( resource.getImage("level_2_0").get_width() /2, resource.getImage("level_2_0").get_height() / 2))
        self.levelBtn2 = LevelButton2(self.levelBtn2Rect, imageLevel21, imageLevel20, self)

        self.levelBtn3Rect = Rect(100, 160,resource.getImage("level_3_0").get_width() / 2, resource.getImage("level_3_0").get_height() / 2)
        imageLevel31 = pygame.transform.scale(resource.getImage("level_3_1"),( resource.getImage("level_3_1").get_width() /2, resource.getImage("level_3_1").get_height() / 2))
        imageLevel30 = pygame.transform.scale(resource.getImage("level_3_0"),( resource.getImage("level_3_0").get_width() /2, resource.getImage("level_3_0").get_height() / 2))
        self.levelBtn3 = LevelButton3(self.levelBtn3Rect, imageLevel31, imageLevel30, self)

        self.labels = dict()

    #def draw_self(self):
        #绘制内容
        #screen.blit(self.background[gamestate.SenceLevel], (0, 0))
        #if gamestate.SenceLevel == gamestate.LEVEL_0:
        #    screen.blit(self.mapKey, (baseOffest + self.battleMap.get_width(), 10))
        #    screen.set_clip(baseOffest + 3 + self.battleMap.get_width() - self.mapOffest, 20, self.mapOffest, self.battleMap.get_height())
        #    screen.blit(self.battleMap, (baseOffest + self.battleMap.get_width() - self.mapOffest, 20))

        #    self.levelBtn1.draw_self()
        #    self.levelBtn2.draw_self()
        #    self.levelBtn3.draw_self()

        #    screen.set_clip((0, 0, mypygame.screenwidth, mypygame.screenwidth))

        #    screen.blit(self.mapKey, (baseOffest + 6 + self.battleMap.get_width() - self.mapOffest - self.mapKey.get_width(), 10))

        #self.playerBtn.draw_self()

        #if self.battle:
        #    self.battle.draw_self()

        #for lb in self.labels.keys():
        #    if self.labels[lb].viewState.view == label.ViewTimer and not self.labels[lb].viewState.isView:
        #        del self.labels[lb]

        #for lb in self.labels:
        #    self.labels[lb].draw_self()

    #def handle_event(self, event):
        #self.playerBtn.handle_event(event)
        #self.levelBtn1.handle_event(event)
        #self.levelBtn2.handle_event(event)
        #self.levelBtn3.handle_event(event)

    def update(self):
        if gamestate.SenceLevel == gamestate.LEVEL_0:
            if self.mapOffest < self.battleMap.get_width() - 3:
                self.mapOffest = self.mapOffest + 3
                if self.mapOffest > self.battleMap.get_width():
                    self.mapOffest = self.battleMap.get_width() - 3
                if self.mapOffest > 136 - self.levelBtn1.drawImage.get_width():
                    self.levelBtn1.rect[0] = baseOffest + self.battleMap.get_width() + 5 + 2*self.levelBtn1.drawImage.get_width()/3 - self.mapOffest
                if self.mapOffest > 290 - self.levelBtn2.drawImage.get_width():
                    self.levelBtn2.rect[0] = baseOffest + 168 + self.battleMap.get_width() + 5 + self.levelBtn2.drawImage.get_width() - self.mapOffest
                if self.mapOffest > 21 - self.levelBtn3.drawImage.get_width():
                    self.levelBtn3.rect[0] = baseOffest - 75 + self.battleMap.get_width() + 5 + self.levelBtn3.drawImage.get_width() - self.mapOffest
                #self.drawSelf()
        if gamestate.SenceLevel != gamestate.LEVEL_0:
            if not self.battle:
                self.battle = battle.Battle(10, self)
            elif self.battle:
                self.battle.update()
        self.draw_self()

    def resetOffest(self):
        self.mapOffest = 0
        self.levelBtn2.rect[0] = 100
        gamestate.SenceLevel = gamestate.LEVEL_0


#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import pygame
from pygame.locals import *
import mypygame
import button
import gamestate
import resource

screen = mypygame.screen

class LevelButton1(button.Button):
    def __init__(self, rect, normal_image, select_image, father):
        button.Button.__init__(self, rect, normal_image, select_image, father)

    def clickUpEffect(self):
        gamestate.SenceLevel = gamestate.LEVEL_1

class PlayerInfoButton(button.Button):
    def __init__(self, rect, normal_image, select_image, father):
        button.Button.__init__(self, rect, normal_image, select_image, father)

    def clickUpEffect(self):
        gamestate.GameState = gamestate.MainUI

class UIGame(object):
    def __init__(self):
        self.background = []
        self.background.append(pygame.transform.scale(pygame.image.load("resource/background.jpg").convert_alpha(), screen.get_size()))
        self.background.append(pygame.transform.scale(pygame.image.load("resource/level_1_background.jpg").convert_alpha(), screen.get_size()))
        self.background.append(pygame.transform.scale(pygame.image.load("resource/level_2_background.jpg").convert_alpha(), screen.get_size()))

        self.playerBtnRect = Rect(mypygame.screenwidth - 100, mypygame.screenheight - 80, resource.getImage("player").get_width(), resource.getImage("player").get_height())
        self.playerBtn = PlayerInfoButton(self.playerBtnRect, resource.getImage("player"), None, self)

        self.battleMap = resource.getImage("big_map")
        self.battleMap = pygame.transform.scale(self.battleMap,( self.battleMap.get_width() /2, self.battleMap.get_height() / 2))

        self.mapKey = resource.getImage("map_key")
        self.mapKey = pygame.transform.scale(self.mapKey,( self.mapKey.get_width() /2, self.mapKey.get_height() / 2))
        self.mapOffest = 0

        self.levelBtn1Rect = Rect(163,111,resource.getImage("level_1_0").get_width() / 2, resource.getImage("level_1_0").get_height() / 2)
        imageLevel11 = pygame.transform.scale(resource.getImage("level_1_1"),( resource.getImage("level_1_1").get_width() /2, resource.getImage("level_1_1").get_height() / 2))
        imageLevel10 = pygame.transform.scale(resource.getImage("level_1_0"),( resource.getImage("level_1_0").get_width() /2, resource.getImage("level_1_0").get_height() / 2))
        self.levelBtn1 = LevelButton1(self.levelBtn1Rect, imageLevel11, imageLevel10, self)

    def drawSelf(self):
        #绘制内容
        screen.blit(self.background[gamestate.SenceLevel], (0, 0))
        if gamestate.SenceLevel == gamestate.LEVEL_0:
            screen.blit(self.mapKey, (100 + self.battleMap.get_width(), 10))
            screen.set_clip(103 + self.battleMap.get_width() - self.mapOffest, 20, self.mapOffest, self.battleMap.get_height())
            screen.blit(self.battleMap, (100 + self.battleMap.get_width() - self.mapOffest, 20))

            self.levelBtn1.drawSelf()

            screen.set_clip((0, 0, mypygame.screenwidth, mypygame.screenwidth))

            screen.blit(self.mapKey, (106 + self.battleMap.get_width() - self.mapOffest - self.mapKey.get_width(), 10))
        elif gamestate.SenceLevel == gamestate.LEVEL_1:
            screen.blit(resource.getImage("header_line"), (250, 250))
        self.playerBtn.drawSelf()

    def handleEvent(self, event):
        self.playerBtn.handleEvent(event)
        self.levelBtn1.handleEvent(event)

    def update(self):
        if gamestate.SenceLevel == gamestate.LEVEL_0:
            if self.mapOffest < self.battleMap.get_width() - 3:
                self.mapOffest = self.mapOffest + 3
                if self.mapOffest > self.battleMap.get_width():
                    self.mapOffest = self.battleMap.get_width() - 3
                if self.mapOffest > 136 - self.levelBtn1.drawImage.get_width():
                    self.levelBtn1.rect[0] = 100 + self.battleMap.get_width() + 5 + 2*self.levelBtn1.drawImage.get_width()/3 - self.mapOffest
                self.drawSelf()

    def resetOffest(self):
        self.mapOffest = 0
        gamestate.SenceLevel = gamestate.LEVEL_0


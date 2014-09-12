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

screen = mypygame.screen
screenwidth = mypygame.screenwidth
screenheight = mypygame.screenheight

LayerButton = gamestate.LayerButton
LayerLabel = gamestate.LayerLabel
LayerUI = gamestate.LayerUI

class PlayerInfoButton(button.Button):
    def __init__(self, rect, normal_image, select_image, father):
        button.Button.__init__(self, rect, normal_image, select_image, father)

    def click_up_effect(self):
        #screen.blit(resource.getImage("attribute"), (0, 0))
        gamestate.SenceLevel = gamestate.LEVEL_0
        self.father.battle = None

class UIGame(util.node.Node):
    def __init__(self):
        util.node.Node.__init__(self)

        self.battle = None

        player_image = resource.getImage("player")
        player_btn_rect = Rect(screenwidth - 100, screenheight - 80, player_image.get_width(), player_image.get_height())
        player_btn = PlayerInfoButton(player_btn_rect, player_image, None, self)
        self.layer_child[LayerButton]["user_info"] = player_btn

        misison_map = game_ui.mission_map.MissionMap()
        self.layer_child[LayerUI]["mission_map"] = misison_map

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
    '''
    def update(self):
        if gamestate.SenceLevel == gamestate.LEVEL_0:
            if self.mapOffest < self.battleMap.get_width() - 3:
                self.mapOffest = self.mapOffest + 3
                if self.mapOffest > self.battleMap.get_width():
                    self.mapOffest = self.battleMap.get_width() - 3
                if self.mapOffest > 136 - self.levelBtn1.draw_image.get_width():
                    self.levelBtn1.rect[0] = baseOffest + self.battleMap.get_width() + 5 + 2*self.levelBtn1.draw_image.get_width()/3 - self.mapOffest
                if self.mapOffest > 290 - self.levelBtn2.draw_image.get_width():
                    self.levelBtn2.rect[0] = baseOffest + 168 + self.battleMap.get_width() + 5 + self.levelBtn2.draw_image.get_width() - self.mapOffest
                if self.mapOffest > 21 - self.levelBtn3.draw_image.get_width():
                    self.levelBtn3.rect[0] = baseOffest - 75 + self.battleMap.get_width() + 5 + self.levelBtn3.draw_image.get_width() - self.mapOffest
                #self.drawSelf()
        if gamestate.SenceLevel != gamestate.LEVEL_0:
            if not self.battle:
                self.battle = battle.Battle(10, self)
            elif self.battle:
                self.battle.update()
        self.draw_self()'''

    def resetOffest(self):
        self.mapOffest = 0
        #self.levelBtn2.rect[0] = 100
        gamestate.SenceLevel = gamestate.LEVEL_0


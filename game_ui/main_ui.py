#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import pygame, sys, pygame.mixer
from pygame.locals import *
import mypygame
import util.node
import button
import gamestate
import resource
import label

screen = mypygame.screen

LayerButton = gamestate.LayerButton
LayerLabel = gamestate.LayerLabel
LayerUI = gamestate.LayerUI

#开始游戏按钮
class StartButton(button.Button):
    def __init__(self, rect, normal_image, select_image, father):
        button.Button.__init__(self, rect, normal_image, select_image, father)

    def MouseHoverEffect(self):
        if self.mouseStance:
            x, y = pygame.mouse.get_pos()
            rect = Rect(x + 30, y + 30, 100, 50)
            view = label.LabelViewState(label.ViewForver)
            text1 = label.FontLabel(rect, view, "resource/msyh.ttf", 16, u"点击开始游戏")
            self.father.layer_child[LayerLabel]["start_tips"] = text1
        elif not self.mouseStance and self.father.layer_child[LayerLabel].has_key("start_tips"):
            del self.father.layer_child[LayerLabel]["start_tips"]

    def clickUpEffect(self):
        gamestate.GameState = gamestate.GameUI

#退出游戏按钮
class ExitButton(button.Button):
    def __init__(self, rect, normal_image, select_image, father):
        button.Button.__init__(self, rect, normal_image, select_image, father)

    def MouseHoverEffect(self):
        if self.mouseStance:
            x, y = pygame.mouse.get_pos()
            rect = Rect(x + 30, y + 30, 100, 50)
            view = label.LabelViewState(label.ViewForver)
            text1 = label.FontLabel(rect, view, "resource/msyh.ttf", 16, u"点击此处退出")
            self.father.layer_child[LayerLabel]["exit_tips"] = text1
        elif not self.mouseStance and self.father.layer_child[LayerLabel].has_key("exit_tips"):
            del self.father.layer_child[LayerLabel]["exit_tips"]
        #self.text1.drawSelf()

    def clickUpEffect(self):
        mypygame.running = False

#主界面
class UIMain(util.node.Node):
    def __init__(self):
        util.node.Node.__init__(self)

        self.layer_child[LayerButton]["start"] = StartButton(Rect(350, 440, 100, 50), resource.getImage("start_normal"), resource.getImage("start_down"), self)
        self.layer_child[LayerButton]["exit"] = ExitButton(Rect(550, 440, 100, 50), resource.getImage("start_normal"), resource.getImage("start_down"), self)

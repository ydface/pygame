#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import pygame, sys, pygame.mixer
from pygame.locals import *
import mypygame
import util.node
import game_ui.mission_ui
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
    def __init__(self, father):
        rect = Rect(345, 420, 100, 50)
        image1 = resource.getImage("start_normal")
        image0 = resource.getImage("start_down")

        button.Button.__init__(self, rect, image1, image0, father)

    def mouse_hover_effect(self):
        if self.mouse_stance:
            x, y = pygame.mouse.get_pos()
            rect = Rect(x + 30, y + 30, 100, 50)
            view = label.LabelViewState(label.ViewForver)
            text1 = label.FontLabel(rect, view, 16, u"点击开始游戏")
            self.father.layer_child[LayerLabel]["start_tips"] = text1
        elif not self.mouse_stance and self.father.layer_child[LayerLabel].has_key("start_tips"):
            del self.father.layer_child[LayerLabel]["start_tips"]

    def click_up_effect(self):
        gamestate.current_ui = game_ui.mission_ui.UIGame()


#退出游戏按钮
class ExitButton(button.Button):
    def __init__(self, father):
        rect = Rect(345, 500, 100, 50)
        image1 = resource.getImage("start_normal")
        image0 = resource.getImage("start_down")

        button.Button.__init__(self, rect, image1, image0, father)

    def mouse_hover_effect(self):
        if self.mouse_stance:
            x, y = pygame.mouse.get_pos()
            rect = Rect(x + 30, y + 30, 100, 50)
            view = label.LabelViewState(label.ViewForver)
            text1 = label.FontLabel(rect, view, 16, u"点击此处退出")
            self.father.layer_child[LayerLabel]["exit_tips"] = text1
        elif not self.mouse_stance and self.father.layer_child[LayerLabel].has_key("exit_tips"):
            del self.father.layer_child[LayerLabel]["exit_tips"]

    def click_up_effect(self):
        mypygame.running = False


#主界面
class UIMain(util.node.Node):
    def __init__(self):
        util.node.Node.__init__(self)

        self.layer_child[LayerButton]["start"] = StartButton(self)
        self.layer_child[LayerButton]["exit"] = ExitButton(self)

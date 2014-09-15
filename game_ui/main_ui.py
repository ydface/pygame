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

#开始游戏按钮
class StartButton(button.Button):
    def __init__(self, father):
        rect = Rect(345, 420, 100, 50)
        image1 = resource.getImage("start_normal")
        image0 = resource.getImage("start_down")

        super(StartButton, self).__init__(rect, image1, image0, father)

    def click_up_effect(self):
        gamestate.current_ui = game_ui.mission_ui.UIGame()


#退出游戏按钮
class ExitButton(button.Button):
    def __init__(self, father):
        rect = Rect(345, 500, 100, 50)
        image1 = resource.getImage("start_normal")
        image0 = resource.getImage("start_down")

        super(ExitButton, self).__init__(rect, image1, image0, father)

    def click_up_effect(self):
        mypygame.running = False


#主界面
class UIMain(util.node.Node):
    def __init__(self):
        super(UIMain, self).__init__()

        self.add(StartButton(self))
        self.add(ExitButton(self))

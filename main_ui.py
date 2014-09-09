#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import pygame, sys, pygame.mixer
from pygame.locals import *
import mypygame
import button
import gamestate
import resource
import label

pygame = mypygame.pygame
screen = mypygame.screen

#开始游戏按钮
class StartButton(button.Button):
    def __init__(self, rect, normal_image, select_image):
        button.Button.__init__(self, rect, normal_image, select_image)

    def clickUpEffect(self):
        gamestate.GameState = gamestate.GameUI

#退出游戏按钮
class ExitButton(button.Button):
    def __init__(self, rect, normal_image, select_image):
        button.Button.__init__(self, rect, normal_image, select_image)

    def MouseHoverEffect(self):
        self.text1 = label.FontLabel(Rect(100 + 5, 100, 100, 50), label.LabelViewState(label.ViewInterval,50,[0,0]), "宋体", 64, u"测 试")
        self.text1.drawSelf()

    def clickUpEffect(self):
        raise SystemExit

#主界面
class UIMain(object):
    def __init__(self):
        #背景
        self.background = pygame.image.load("resource/background.jpg").convert_alpha()
        self.background = pygame.transform.scale(self.background, screen.get_size())

        #按钮
        self.btn = []
        self.btn.append(StartButton(Rect(350, 440, 100, 50), resource.getImage("start_normal"), resource.getImage("start_down")))
        self.btn.append(ExitButton(Rect(550, 440, 100, 50), resource.getImage("start_normal"), resource.getImage("start_down")))

        #self.text1 = label.FontLabel(Rect(250, 440, 100, 50), label.LabelViewState(label.ViewTimer,50,[0,0]), "宋体", 64, u"测 试")
    def drawSelf(self):
        #绘制内容
        screen.blit(self.background, (0, 0))
        for btn in self.btn:
            btn.drawSelf()
        #self.text1.drawSelf()
    def handleEvent(self, event):
        for btn in self.btn:
            btn.handleEvent(event)
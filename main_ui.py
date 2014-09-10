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
    def __init__(self, rect, normal_image, select_image, father):
        button.Button.__init__(self, rect, normal_image, select_image, father)

    def MouseHoverEffect(self):
        if self.mouseStance:
            x, y = pygame.mouse.get_pos()
            rect = Rect(x + 30, y + 30, 100, 50)
            view = label.LabelViewState(label.ViewForver)
            text1 = label.FontLabel(rect, view, "resource/msyh.ttf", 16, u"点击开始游戏")
            self.father.label["start_tips"] = text1
        elif not self.mouseStance and self.father.label.has_key("start_tips"):
            del self.father.label["start_tips"]

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
            self.father.label["exit_tips"] = text1
        elif not self.mouseStance and self.father.label.has_key("exit_tips"):
            del self.father.label["exit_tips"]
        #self.text1.drawSelf()

    def clickUpEffect(self):
        mypygame.running = False

#主界面
class UIMain(object):
    def __init__(self):
        #背景
        self.background = pygame.image.load("resource/background.jpg").convert_alpha()
        self.background = pygame.transform.scale(self.background, screen.get_size())

        #按钮
        self.btn = []
        self.btn.append(StartButton(Rect(350, 440, 100, 50), resource.getImage("start_normal"), resource.getImage("start_down"), self))
        self.btn.append(ExitButton(Rect(550, 440, 100, 50), resource.getImage("start_normal"), resource.getImage("start_down"), self))

        self.label = dict()
        #self.text1 = label.FontLabel(Rect(250, 440, 100, 50), label.LabelViewState(label.ViewTimer,50,[0,0]), "宋体", 64, u"测 试")
    def drawSelf(self):
        #绘制内容
        screen.blit(self.background, (0, 0))
        for btn in self.btn:
            btn.drawSelf()

        for lb in self.label:
            self.label[lb].drawSelf()
        #self.text1.drawSelf()
    def handleEvent(self, event):
        for btn in self.btn:
            btn.handleEvent(event)
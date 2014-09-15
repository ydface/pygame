#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import pygame, sys, pygame.mixer
from pygame.locals import *
import mypygame
import util.node

screen = mypygame.screen

#永久显示
ViewForver = 1

#定时显示
ViewTimer = 2

#间隔显示
ViewInterval = 3


COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 128, 0)
COLOR_WHITE = (255, 255, 255)


#[0][0] 第一位表示上下方向位移,第二位表示左右方向位移
class LabelViewState(object):
    def __init__(self, view, last_time=1, move=[0, 0]):
        super(LabelViewState, self).__init__()
        self.view = view
        self.move = move
        self.last_time = last_time
        self.isView = True


class FontLabel(util.node.Node):
    def __init__(self, rect, view_state, font_size, **kwargs):
        super(FontLabel, self).__init__(**kwargs)

        self.rect = rect
        self.viewState = view_state
        self.font = "resource/msyh.ttf"
        self.fontSize = font_size
        self.text = kwargs['text']
        self.father = kwargs.get('father', None)

        color = kwargs.get('color', COLOR_WHITE)

        self.my_font = pygame.font.Font(self.font, self.fontSize)
        self.name_surface = self.my_font.render(self.text, True, color)

    def update(self, **kwargs):
        self.rect[0] = self.rect[0] + self.viewState.move[0]
        self.rect[1] = self.rect[1] + self.viewState.move[1]
        if self.viewState.view == ViewTimer:
            time = kwargs['time']
            self.viewState.last_time -= time
            if self.viewState.last_time <= 0:
                self.viewState.isView = False
                self.father.remove(self)
        elif self.viewState.view == ViewInterval:
            self.viewState.curFrame += + 1
            if self.viewState.viewFrame == self.viewState.curFrame:
                self.viewState.isView = not self.viewState.isView
                self.viewState.curFrame = 0

    def draw(self):
        if self.viewState.isView:
            screen.blit(self.name_surface, (self.rect[0], self.rect[1]))
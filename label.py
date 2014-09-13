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
    def __init__(self, view, view_frame=0, move=[0, 0]):
        super(LabelViewState, self).__init__()
        self.view = view
        self.viewFrame = view_frame
        self.move = move
        self.curFrame = 0
        self.isView = True


class FontLabel(util.node.Node):
    def __init__(self, rect, view_state, font_size, text="TEXT", color=COLOR_WHITE):
        super(FontLabel, self).__init__()

        self.rect = rect
        self.viewState = view_state
        self.font = "resource/msyh.ttf"
        self.fontSize = font_size
        self.text = text

        self.my_font = pygame.font.Font(self.font, self.fontSize)
        self.name_surface = self.my_font.render(self.text, True, color)

    def update(self):
        self.rect[0] = self.rect[0] + self.viewState.move[0]
        self.rect[1] = self.rect[1] + self.viewState.move[1]
        if self.viewState.view == ViewTimer:
            if self.viewState.viewFrame > 0:
                self.viewState.viewFrame -= 1
                if self.viewState.viewFrame <= 0:
                    self.viewState.isView = False
        elif self.viewState.view == ViewInterval:
            self.viewState.curFrame += + 1
            if self.viewState.viewFrame == self.viewState.curFrame:
                self.viewState.isView = not self.viewState.isView
                self.viewState.curFrame = 0

    def draw_self(self):
        self.update()
        if self.viewState.isView:
            screen.blit(self.name_surface, (self.rect[0], self.rect[1]))
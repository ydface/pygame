#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import pygame
import sys
import pygame.mixer
from pygame.locals import *
import mypygame
import util.node

screen = mypygame.screen


class Button(util.node.Node):
    def __init__(self, pos, image0, image1, father, **kwargs):
        super(Button, self).__init__(**kwargs)

        self.father = father
        # 正常状态下图片
        self.image0 = image0

        #鼠标点击下图片
        self.image1 = image1
        self.image = self.image0

        self.rect = self.image.get_rect()
        self.rect.topleft = (pos[0], pos[1])

        #鼠标悬停
        self.mouse_stance = False

    def draw(self):
        screen.blit(self.image, (self.rect[0], self.rect[1]))

    def event(self, event):
        #点击事件检测与处理
        if event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            position = pygame.mouse.get_pos()
            if self.rect.collidepoint(position):
                self.click_down()
        elif event.type == MOUSEMOTION:
            position = pygame.mouse.get_pos()
            if self.rect.collidepoint(position):
                self.mouse_stance = True
            else:
                self.mouse_stance = False
            self.mouse_hover_effect()

        elif event.type == MOUSEBUTTONUP:
            self.click_up()
            position = pygame.mouse.get_pos()
            if self.rect.collidepoint(position):
                #点中影响
                self.click_up_effect()

    def mouse_hover_effect(self):
        pass

    def click_down_effect(self):
        pass

    #点击效果，默认无效果
    def click_up_effect(self):
        pass

    def click_down(self):
        #如果有点中效果变化，则变化
        if self.image1:
            self.image = self.image1
        self.click_down_effect()

    def click_up(self):
        self.image = self.image0
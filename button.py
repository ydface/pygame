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
    def __init__(self, rect, normal_image, select_image, father, zorder = 1):
        util.node.Node.__init__(self, zorder)
        #矩形 (x,y,w,h)
        self.rect = rect

        self.father = father
        # 正常状态下图片
        self.image_normal = normal_image

        #鼠标点击下图片
        self.image_selected = select_image
        self.draw_image = self.image_normal

        #鼠标悬停
        self.mouse_stance = False

    def draw_self(self):
        screen.blit(self.draw_image, (self.rect[0], self.rect[1]))

    def handle_event(self, event):
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
        if self.image_selected:
            self.draw_image = self.image_selected
        self.click_down_effect()

    def click_up(self):
        self.draw_image = self.image_normal
#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import pygame, sys, pygame.mixer
from pygame.locals import *
import mypygame

screen = mypygame.screen

class Button(object):
    def __init__(self, rect, normal_image, select_image, father):
        #矩形 (x,y,w,h)
        self.rect = rect
        
        self.father = father
        # 正常状态下图片
        self.imageNormal = normal_image

        #鼠标点击下图片
        self.imageSelected = select_image
        self.drawImage = self.imageNormal

        self.moveAble = False

    def drawSelf(self):
        screen.blit(self.drawImage, (self.rect[0], self.rect[1]))

    def handleEvent(self, event):
        #点击事件检测与处理
        if event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            position = pygame.mouse.get_pos()
            if self.rect.collidepoint(position):
                self.clickDown()
        if event.type == MOUSEMOTION:
            position = pygame.mouse.get_pos()
            if self.rect.collidepoint(position):
                self.mouseStance = True
            else:
                self.mouseStance = False
            self.MouseHoverEffect()

        elif event.type == MOUSEBUTTONUP:
            self.clickUp()
            position = pygame.mouse.get_pos()
            if self.rect.collidepoint(position):
                #点中影响
                self.clickUpEffect()

    def MouseHoverEffect(self):
        pass

    def clickDownEffect(self):
        pass

    #点击效果，默认无效果
    def clickUpEffect(self):
        pass

    def clickDown(self):
        #如果有点中效果变化，则变化
        if self.imageSelected:
            self.drawImage = self.imageSelected
            self.drawSelf()
        self.clickDownEffect()

    def clickUp(self):
        self.drawImage = self.imageNormal
        self.drawSelf()
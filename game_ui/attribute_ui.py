#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import pygame
from pygame.locals import *
import mypygame
import util.node
import button
import gamestate
import resource
import battle
import label

screen = mypygame.screen

class AttributeUI(util.node.Node):
    def __init__(self, zorder):
        util.node.Node.__init__(self, zorder)

        self.image = resource.getImage("attribute")
        self.move_able = False
        self.rect = Rect(100, 300, self.image.get_width(), self.image.get_height())

    def draw_self(self):
        screen.blit(self.image, (self.rect[0], self.rect[1]))

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            position = pygame.mouse.get_pos()
            if self.rect.collidepoint(position):
                self.move_able = True
        elif event.type == MOUSEMOTION:
            position = pygame.mouse.get_pos()
            if self.rect.collidepoint(position):
                rel = pygame.mouse.get_rel()
                if self.move_able:
                    self.rect[0] += rel[0]
                    self.rect[1] += rel[1]

        elif event.type == MOUSEBUTTONUP:
            self.move_able = False
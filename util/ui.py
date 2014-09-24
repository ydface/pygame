#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import pygame
from pygame.locals import *
import mypygame
import util.node

screen = mypygame.screen
screenwidth = mypygame.screenwidth
screenheight = mypygame.screenheight


class BaseUI(util.node.Node):
    def __init__(self):
        super(BaseUI, self).__init__()

        self.move_able = False

    def self_event(self, event):
        if event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            position = event.pos
            if self.rect.collidepoint(position):
                self.move_able = True
                self.top()
                return True
            return False
        elif event.type == MOUSEMOTION:
            position = event.pos
            if self.rect.collidepoint(position):
                rel = pygame.mouse.get_rel()
                if self.move_able:
                    self.rect[0] += rel[0]
                    self.rect[1] += rel[1]
                    for child in self.child:
                        child.rect[0] += rel[0]
                        child.rect[1] += rel[1]
                return True
            return False
        elif event.type == MOUSEBUTTONUP:
            if self.move_able:
                self.move_able = False
                return True
            return False
        else:
            return False
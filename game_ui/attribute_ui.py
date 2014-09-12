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

    def draw_self(self):
        screen.blit(self.image, (400, 300))
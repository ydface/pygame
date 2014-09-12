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

class Item(util.node.Node):
    def __init__(self, father, item_id, pos):
        util.node.Node.__init__(self)

        self.item_id = item_id
        self.image = resource.getImage("item_" + str(self.item_id))
        x = pos % 6
        y = pos / 6

        self.pos = [father.pos[0] + 37.5 * x + 5 + 6 * (x + 1), father.pos[1] + 37.5 * y + 15 + 15 * y]

    def draw_self(self):
        screen.blit(self.image, self.pos)


class BagUI(util.node.Node):
    def __init__(self, zorder):
        util.node.Node.__init__(self, zorder)

        image = resource.getImage("bag_background")
        self.image = pygame.transform.scale(image, (image.get_width() * 2 / 3, image.get_height() * 2))

        self.pos = (280, 300)

        self.items = dict()
        for i in range(0, 30):
            self.items[str(i)] = Item( self, i + 1, i)

    def draw_self(self):
        screen.blit(self.image, self.pos)
        for i in self.items:
            self.items[i].draw_self()
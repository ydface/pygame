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


class ItemCell(util.node.Node):
    def __init__(self, father, item_id, pos):
        super(ItemCell, self).__init__()

        self.father = father
        self.item_id = item_id
        self.image = resource.getImage("item_" + str(self.item_id))
        self.index = pos

        self.x = pos % 6
        self.y = pos / 6

    def draw_self(self):
        pos = (self.father.rect[0] + 37.5 * self.x + 5 + 6 * (self.x + 1), self.father.rect[1] + 37.5 * self.y + 15 + 15 * self.y)
        screen.blit(self.image, pos)


class BagUI(util.node.Node):
    def __init__(self, **kwargs):
        super(BagUI, self).__init__(**kwargs)

        image = resource.getImage("bag_background")
        self.image = pygame.transform.scale(image, (image.get_width() * 2 / 3, image.get_height() * 2))

        self.move_able = False
        self.rect = Rect(280, 300, self.image.get_width(), self.image.get_height())

        self.items = dict()
        for i in range(0, 30):
            self.items[str(i)] = ItemCell( self, i + 1, i)

    def draw(self):
        screen.blit(self.image, (self.rect[0], self.rect[1]))
        for i in self.items:
            self.items[i].draw_self()

    def event(self, event):
        if event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            position = pygame.mouse.get_pos()
            if self.rect.collidepoint(position):
                self.move_able = True
                self.top_layer()
        elif event.type == MOUSEMOTION:
            position = pygame.mouse.get_pos()
            if self.rect.collidepoint(position):
                rel = pygame.mouse.get_rel()
                if self.move_able:
                    self.rect[0] += rel[0]
                    self.rect[1] += rel[1]

        elif event.type == MOUSEBUTTONUP:
            self.move_able = False
            self.back_layer()
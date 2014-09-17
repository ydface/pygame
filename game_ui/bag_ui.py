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
import game_ui.attribute_ui
from equipment import *

screen = mypygame.screen

item_background = [(255, 255, 255), (0, 255, 0), (65, 105, 225), (160, 32, 240), (255, 0, 0), (255, 255, 0)]


class ItemCell(util.node.Node):
    def __init__(self, father, equip, idx):
        super(ItemCell, self).__init__()

        self.father = father
        self.equip = equip
        self.image = resource.getImage("item_" + str(self.equip.template))
        self.index = idx
        self.clicked = False

        self.x = idx % 6
        self.y = idx / 6

        self.rect = self.image.get_rect()
        pos = (self.father.rect[0] + 37.5 * self.x + 5 + 6 * (self.x + 1), self.father.rect[1] + 37.5 * self.y + 15 + 15 * self.y)
        self.rect.topleft = (pos[0], pos[1])

    def draw(self):
        pos = (self.father.rect[0] + 37.5 * self.x + 5 + 6 * (self.x + 1), self.father.rect[1] + 37.5 * self.y + 15 + 15 * self.y)
        self.rect.topleft = (pos[0], pos[1])
        pygame.draw.rect(screen, item_background[self.equip.quality], (pos[0] -2, pos[1] - 2, self.image.get_width() + 4, self.image.get_height() + 4))
        screen.blit(self.image, pos)

        label.FontLabel.draw_label(10, Equip_Name[self.equip.part], label.COLOR_WHITE, (pos[0] + 12, pos[1] + 38))

    def event(self, event):
        if event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            position = pygame.mouse.get_pos()
            if self.rect.collidepoint(position):
                self.clicked = True
        elif event.type == MOUSEMOTION:
            position = pygame.mouse.get_pos()
            if not self.rect.collidepoint(position):
                self.clicked = False
        elif event.type == MOUSEBUTTONUP:
            if self.clicked:
                gamestate.player.put_on_equipment(self.index)
                self.clicked = False
                self.father.rebuild()
                attr_ui = self.father.father.has_ui(game_ui.attribute_ui.AttributeUI)
                if attr_ui is not None:
                    attr_ui.rebuild()

class BagUI(util.node.Node):
    def __init__(self, **kwargs):
        super(BagUI, self).__init__(**kwargs)

        image = resource.getImage("bag_background")
        self.image = pygame.transform.scale(image, (image.get_width() * 2 / 3, image.get_height() * 2))

        self.move_able = False
        self.rect = Rect(280, 300, self.image.get_width(), self.image.get_height())

        self.items = dict()
        self.rebuild()

    def draw(self):
        screen.set_clip(self.rect[0], self.rect[1], self.image.get_width(), self.image.get_height())
        screen.blit(self.image, (self.rect[0], self.rect[1]))
        for child in self.child:
            child.draw()

        screen.set_clip((0, 0, mypygame.screenwidth, mypygame.screenwidth))

    def rebuild(self):
        self.child = []
        equips = gamestate.player.equips
        for i in range(len(equips)):
            if equips[i] is not None:
                self.add(ItemCell( self, equips[i], i))

        #for i in self.items:
            #self.items[i].draw()
    '''
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
    '''
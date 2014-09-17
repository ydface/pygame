#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import pygame
from pygame.locals import *
import mypygame
import util.node
from util.node import *
import util.ui
import button
import gamestate
import resource
import battle
import label
import game_ui.attribute_ui
from equipment import *
from util.color import *
screen = mypygame.screen

#道具品质颜色
IBC = [COLOR_WHITE, COLOR_GREEN, COLOR_BLUE, COLOR_Purple, COLOR_RED, COLOR_GOLD]

IEW = 2


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
        pos = self.rect.topleft
        e_rect = (pos[0] - IEW, pos[1] - IEW, self.rect[2] + IEW * 2, self.rect[3] + IEW * 2)
        pygame.draw.rect(screen, IBC[self.equip.quality], e_rect)
        screen.blit(self.image, pos)

        label.FontLabel.draw_label(10, Equip_Name[self.equip.part], label.COLOR_WHITE, (pos[0] + 12, pos[1] + 38))

    def event(self, event):
        if event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            position = pygame.mouse.get_pos()
            if self.rect.collidepoint(position):
                self.clicked = True
                return True
            return False
        elif event.type == MOUSEMOTION:
            position = pygame.mouse.get_pos()
            if not self.rect.collidepoint(position):
                self.clicked = False
        elif event.type == MOUSEBUTTONUP:
            if self.clicked:
                gamestate.player.put_on_equipment(self.index)
                self.clicked = False
                self.father.rebuild()
                attr_ui = self.father.father.has_ctype_child(game_ui.attribute_ui.AttributeUI)
                if attr_ui is not None:
                    attr_ui.rebuild()
                return True
            return False
        return False


class BagUI(util.ui.BaseUI):
    def __init__(self, **kwargs):
        super(BagUI, self).__init__()

        self.event_type = Event_Type_Child

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
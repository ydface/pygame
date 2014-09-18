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
IBC = [COLOR_WHITE, COLOR_GREEN, COLOR_BLUE, COLOR_PURPLE, COLOR_RED, COLOR_GOLD]

IEW = 2


class ItemDetail(util.node.Node):
    def __init__(self, father, item_cell, target):
        super(ItemDetail, self).__init__(father=father)

        self.item = item_cell

        #对比装备
        self.target = target
        image = resource.getImage("bag_background")
        self.image = pygame.transform.scale(image, (image.get_width() * 2 / 5, image.get_height() * 2))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.item.rect[0] + self.item.rect[2] + 5, self.item.rect[1])
        self.target_rect = self.image.get_rect()
        self.target_rect.topleft = (self.item.rect[0] - self.item.rect[2] - 85, self.item.rect[1])

    def draw(self):
        #当前装备
        screen.blit(self.image, self.rect.topleft)
        screen.blit(self.item.image, (self.rect[0] + 14, self.rect[1] + 11))
        text = u"等级:   " + str(self.item.equip.level)
        label.FontLabel.draw_label(10, text, COLOR_WHITE, (self.rect[0] + 15, self.rect[1] + 42))
        text = u"品质:   " + QName[self.item.equip.quality]
        label.FontLabel.draw_label(10, text, IBC[self.item.equip.quality], (self.rect[0] + 15, self.rect[1] + 58))
        for attr in range(Attribute_Hp, Attribute_None):
            text = self.item.equip.attribute_value_str(attr)
            label.FontLabel.draw_label(10, text, COLOR_WHITE, (self.rect[0] + 15, self.rect[1] + 56 + 20 + 20 * attr))

        #已装备装备
        if not self.target:
            return
        screen.blit(self.image, self.target_rect)
        screen.blit(self.target.image, (self.target_rect[0] + 14, self.target_rect[1] + 11))
        text = u"等级:   " + str(self.target.level)
        label.FontLabel.draw_label(10, text, COLOR_WHITE, (self.target_rect[0] + 15, self.target_rect[1] + 42))
        text = u"品质:   " + QName[self.target.quality]
        label.FontLabel.draw_label(10, text, IBC[self.target.quality], (self.target_rect[0] + 15, self.target_rect[1] + 58))
        for attr in range(Attribute_Hp, Attribute_None):
            text = self.target.attribute_value_str(attr)
            label.FontLabel.draw_label(10, text, COLOR_WHITE, (self.target_rect[0] + 15, self.target_rect[1] + 56 + 20 + 20 * attr))
        #pygame.draw.rect(screen, COLOR_RED, self.close_rect)
        #label.FontLabel.draw_label(14, u'关闭', COLOR_WHITE, (self.close_rect[0] + 8, self.close_rect[1] + 2))


class ItemCell(util.node.Node):
    def __init__(self, father, equip, idx, pos):
        super(ItemCell, self).__init__()

        self.father = father
        self.equip = equip
        self.image = resource.getImage("item_" + str(self.equip.template))
        self.index = idx
        self.clicked = False

        self.x = pos % 6
        self.y = pos / 6

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
                i_detail = self.father.has_ctype_child(ItemDetail)
                if i_detail and i_detail.item == self:
                    self.father.remove_ctype_child(ItemDetail)
                return False
            else:
                if not self.father.has_ctype_child(ItemDetail):
                    self.father.add(ItemDetail(self, self, gamestate.player.part_equipment(self.equip.part)))
                    return True
            return False
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

        self.up_btl_rect = Rect(self.rect[0] + self.rect[1] + 3, self.rect[1] + 40, 20, 20)
        self.down_btl_rect = Rect(self.rect[0] + self.rect[1] + 3, self.rect[1] + 70, 20, 20)

        self.items = dict()
        self.line = 0
        self.max_line = 0
        self.rebuild()

    def draw(self):
        #screen.set_clip(self.rect[0], self.rect[1], self.image.get_width(), self.image.get_height())
        screen.blit(self.image, (self.rect[0], self.rect[1]))
        for child in self.child:
            child.draw()

        #screen.set_clip((0, 0, mypygame.screenwidth, mypygame.screenwidth))

        label.FontLabel.draw_label(20, "+", label.COLOR_WHITE, self.up_btl_rect.topleft)
        label.FontLabel.draw_label(20, "-", label.COLOR_WHITE, self.down_btl_rect.topleft)

    def rebuild(self):
        self.child = []
        equips = gamestate.player.equips
        self.max_line = len(equips) / 6 + 1
        for i in range(self.line * 6, self.line * 6 + 6 * 5):
            if equips[i] is not None:
                self.add(ItemCell(self, equips[i], i, i - self.line * 6))

    def self_event(self, event):
        if event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            position = pygame.mouse.get_pos()
            if self.rect.collidepoint(position):
                self.move_able = True
                self.top()
                return True
            if self.up_btl_rect.collidepoint(position):
                self.line += 1
                self.line = min([self.max_line, self.line])
                self.rebuild()
            elif self.down_btl_rect.collidepoint(position):
                self.line -= 1
                self.line = max([0, self.line])
                self.rebuild()
            return False
        elif event.type == MOUSEMOTION:
            position = pygame.mouse.get_pos()
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
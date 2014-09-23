#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import mypygame
import gameresource
import util.node
from util.node import *
import util.ui
import label
import game_ui.attribute_ui
from equipment import *
from util.color import *
screen = mypygame.screen

#道具品质颜色
IBC = [COLOR_WHITE, COLOR_GREEN, COLOR_BLUE, COLOR_PURPLE, COLOR_RED, COLOR_GOLD]

IEW = 2

#背包一栏可显示道具数
ALEN = 6

#背包一列可显示道具数
HLEN = 5


class ItemDetail(util.node.Node):
    def __init__(self, father, item_cell, target):
        super(ItemDetail, self).__init__(father=father)

        self.item = item_cell

        #对比装备
        self.target = target
        self.image = gameresource.getUIImage("idetail", 0.56, 2.2, u"装备详情")
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.item.rect[0] + self.item.rect[2] + 5, self.item.rect[1])
        self.target_rect = self.image.get_rect()
        self.target_rect.topleft = (self.item.rect[0] - self.item.rect[2] - 85, self.item.rect[1])

    def draw(self):
        #当前装备
        screen.blit(self.image, self.rect.topleft)
        screen.blit(self.item.equip.image, (self.rect[0] + 14, self.rect[1] + 20 + 11))
        text = u"等级:   " + str(self.item.equip.level)
        label.FontLabel.draw_label(10, text, COLOR_WHITE, (self.rect[0] + 15, self.rect[1] + 62))
        text = u"品质:   " + QName[self.item.equip.quality]
        label.FontLabel.draw_label(10, text, IBC[self.item.equip.quality], (self.rect[0] + 15, self.rect[1] + 78))
        text = u"部位:   " + Equip_Name[self.item.equip.part]
        label.FontLabel.draw_label(10, text, COLOR_WHITE, (self.rect[0] + 15, self.rect[1] + 98))

        text = u"秘技:   无"
        if self.item.equip.skill is not None:
            text = text = u"秘技:   " + self.item.equip.skill.name + " " + str(self.item.equip.skill.level) + u"级"
        label.FontLabel.draw_label(10, text, COLOR_WHITE, (self.rect[0] + 15, self.rect[1] + 118))

        i = 0
        for attr in range(Attribute_Hp, Attribute_None):
            if not self.item.equip.attribute_value(attr):
                if not self.target or not self.target.attribute_value(attr):
                    continue
            text = self.item.equip.attribute_value_str(attr)
            if self.target:
                text += "   (" + str((self.item.equip.attribute_value(attr) - self.target.attribute_value(attr))) + ")"
            label.FontLabel.draw_label(10, text, COLOR_WHITE, (self.rect[0] + 15, self.rect[1] + 76 + 60 + 20 * i))
            i += 1

        #已装备装备
        if not self.target:
            return
        screen.blit(self.image, self.target_rect)
        screen.blit(self.target.image, (self.target_rect[0] + 14, self.target_rect[1] + 20 + 11))
        text = u"当前装备"
        label.FontLabel.draw_label(10, text, COLOR_RED, (self.target_rect[0] + 15, self.target_rect[1] + 62))

        text = u"等级:   " + str(self.target.level)
        label.FontLabel.draw_label(10, text, COLOR_WHITE, (self.target_rect[0] + 15, self.target_rect[1] + 72))
        text = u"品质:   " + QName[self.target.quality]
        label.FontLabel.draw_label(10, text, IBC[self.target.quality], (self.target_rect[0] + 15, self.target_rect[1] + 88))

        text = u"部位:   " + Equip_Name[self.target.part]
        label.FontLabel.draw_label(10, text, COLOR_WHITE, (self.target_rect[0] + 15, self.target_rect[1] + 108))

        text = u"秘技:   无"
        if self.target.skill is not None:
            text = text = u"秘技:   " + self.target.skill.name + " " + str(self.target.skill.level) + u"级"
        label.FontLabel.draw_label(10, text, COLOR_WHITE, (self.target_rect[0] + 15, self.target_rect[1] + 128))

        i = 0
        for attr in range(Attribute_Hp, Attribute_None):
            if not self.target.attribute_value(attr) and not self.item.equip.attribute_value(attr):
                continue
            text = self.target.attribute_value_str(attr)
            label.FontLabel.draw_label(10, text, COLOR_WHITE, (self.target_rect[0] + 15, self.target_rect[1] + 76 + 70 + 20 * i))
            i += 1



class ItemCell(util.node.Node):
    def __init__(self, father, equip, idx, pos):
        super(ItemCell, self).__init__()

        self.father = father
        self.equip = equip
        if self.equip:
            if self.equip.part in RNAME:
                self.image = gameresource.get_image(RNAME[self.equip.part] + str(self.equip.quality))
                self.image = pygame.transform.scale(self.image, (37, 37))
            else:
                self.image = gameresource.get_image("item_" + str(self.equip.template))
        else:
            self.image = gameresource.get_image("ecell")
            self.image = pygame.transform.scale(self.image, (37, 37))

        self.index = idx
        self.clicked = False

        self.x = pos % ALEN
        self.y = pos / ALEN

        self.rect = self.image.get_rect()
        pos = (self.father.rect[0] + 37.5 * self.x + 3 + 7 * (self.x + 1), self.father.rect[1] + 37 + 37.5 * self.y + 15 + 15 * self.y)
        self.rect.topleft = (pos[0], pos[1])

    def draw(self):
        pos = self.rect.topleft
        e_rect = (pos[0] - IEW, pos[1] - IEW, self.rect[2] + IEW * 2, self.rect[3] + IEW * 2)
        if self.equip:
            label.FontLabel.draw_rect_line((pos[0] - IEW, pos[1] - IEW), (self.rect[2] + IEW * 2, self.rect[3] + IEW * 2), IBC[self.equip.quality])
        screen.blit(self.image, pos)

    def event(self, event):
        if event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            position = pygame.mouse.get_pos()
            if self.rect.collidepoint(position):
                self.clicked = True
                return True
            return False
        if event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[2]:
            position = pygame.mouse.get_pos()
            if self.rect.collidepoint(position):
                gamestate.player.destory_equipment(self.equip)
                self.father.remove(self)
                self.father.remove_ctype_child(ItemDetail)
                self.father.rebuild()
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
                if not self.father.has_ctype_child(ItemDetail) and self.equip:
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

        self.image = gameresource.getUIImage("bag_ui", 1.17, 2.2, u"背包", 20)

        self.move_able = False
        self.rect = Rect(280, 300, self.image.get_width(), self.image.get_height())

        self.up_btl_rect = Rect(self.rect[0] + self.rect[1] + 3, self.rect[1] + 40, 60, 20)
        self.down_btl_rect = Rect(self.rect[0] + self.rect[1] + 3, self.rect[1] + 70, 60, 20)

        self.items = dict()
        self.line = 0
        self.max_line = 0
        self.rebuild()

    def draw(self):
        screen.blit(self.image, (self.rect[0], self.rect[1]))
        for child in self.child:
            child.draw()

        label.FontLabel.draw_label(20, u"向下翻", label.COLOR_WHITE, self.up_btl_rect.topleft)
        label.FontLabel.draw_label(20, u"向上翻", label.COLOR_WHITE, self.down_btl_rect.topleft)

    def rebuild(self):
        self.child = []
        equips = gamestate.player.equips
        self.max_line = len(equips) / ALEN
        bidx = self.line * ALEN
        for i in range(bidx, bidx + ALEN * HLEN):
            if i >= len(equips):
                break
            #if equips[i] is not None:
            self.add(ItemCell(self, equips[i], i, i - bidx))

    def self_event(self, event):
        if event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            position = pygame.mouse.get_pos()
            if self.rect.collidepoint(position):
                self.move_able = True
                self.top()
                return True
            if self.up_btl_rect.collidepoint(position):
                self.line += 1
                self.line = min([self.max_line - HLEN, self.line])
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
                    self.up_btl_rect[0] += rel[0]
                    self.up_btl_rect[1] += rel[1]
                    self.down_btl_rect[0] += rel[0]
                    self.down_btl_rect[1] += rel[1]
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

#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import mypygame
import util.node
import util.ui
from attribute import *
from bag_ui import *
from equipment import *
screen = mypygame.screen

#装备栏各装备格的偏移
ECO = [
            [100, 10],
    [20, 60],
            [100, 110],
    [20, 160],      [180, 160],
    [20, 210],      [180, 210],
            [100, 260],
            [100, 310],
            [180, 60]
]

#道具品质边框宽
IEW = 2


class EquipCell(util.node.Node):
    def __init__(self, father, equip):
        super(EquipCell, self).__init__()

        self.father = father
        self.equip = equip
        self.image = resource.getImage("item_" + str(self.equip.template))
        self.clicked = False

        self.rect = self.image.get_rect()
        pos = (self.father.rect[0] + ECO[self.equip.part][0], self.father.rect[1] + ECO[self.equip.part][1])
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
                    self.father.add(ItemDetail(self, self, None))
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


class AttributeLabel(util.node.Node):
    def __init__(self, father):
        super(AttributeLabel, self).__init__(father=father)

        image = resource.getImage("bag_background")
        self.image = pygame.transform.scale(image, (image.get_width() * 2 / 7, image.get_height() * 5 / 2))

        self.rect = self.image.get_rect()
        self.rect.topleft = self.father.rect.topleft
        self.rect[0] = self.father.rect[0] + self.father.rect[2]

    def draw(self):
        screen.blit(self.image, self.rect.topleft)
        text = u"等       级:   " + str(gamestate.player.level)
        label.FontLabel.draw_label(10, text, label.COLOR_WHITE, (self.rect[0] + 15, self.rect[1] + 36))

        text = u"经       验:   " + str(gamestate.player.exp) + " / " + str(gamestate.player.n_exp)
        label.FontLabel.draw_label(10, text, label.COLOR_WHITE, (self.rect[0] + 15, self.rect[1] + 56))

        for attr in range(Attribute_Hp, Attribute_None):
            text = gamestate.player.attribute_value_str(attr)
            label.FontLabel.draw_label(10, text, label.COLOR_WHITE, (self.rect[0] + 15, self.rect[1] + 56 + 20 + 20 * attr))


class AttributeUI(util.ui.BaseUI):
    def __init__(self, **kwargs):
        super(AttributeUI, self).__init__()

        self.event_type = Event_Type_Child

        image = resource.getImage("bag_background")
        self.image = pygame.transform.scale(image, (image.get_width() * 4 / 7, image.get_height() * 5 / 2))

        self.move_able = False
        self.rect = self.image.get_rect()
        self.rect.topleft = (100, 300)

        #self.add(AttributeLabel(self))
        self.rebuild()

    def draw(self):
        screen.blit(self.image, self.rect.topleft)
        for child in self.child:
            child.draw()

    def rebuild(self):
        self.child = []
        self.add(AttributeLabel(self))
        equips = gamestate.player.e_equips
        for i in range(len(equips)):
            if equips[i] is not None:
                self.add(EquipCell(self, equips[i]))
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

Equip_Cell_Offest = [
            [100, 10],
    [20, 60],
            [100, 110],
    [20, 160],      [180, 160],
    [20, 210],      [180, 210],
            [100, 260],
            [100, 310],
            [180, 60]
]


class EquipCell(util.node.Node):
    def __init__(self, father, equip):
        super(EquipCell, self).__init__()

        self.father = father
        self.equip = equip
        self.image = resource.getImage("item_" + str(self.equip.template))
        self.clicked = False

        self.rect = self.image.get_rect()
        pos = (self.father.rect[0] + Equip_Cell_Offest[self.equip.part][0], self.father.rect[1] + Equip_Cell_Offest[self.equip.part][1])
        self.rect.topleft = (pos[0], pos[1])

    def draw(self):
        pos = self.rect.topleft
        pygame.draw.rect(screen, item_background[self.equip.quality], (pos[0] - 2, pos[1] - 2, self.image.get_width() + 4, self.image.get_height() + 4))
        screen.blit(self.image, pos)

        label.FontLabel.draw_label(10, Equip_Name[self.equip.part], label.COLOR_WHITE, (pos[0] + 12, pos[1] + 38))


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
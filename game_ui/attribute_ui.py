#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import mypygame
import util.node
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
        pos = (self.father.rect1[0] + Equip_Cell_Offest[self.equip.part][0], self.father.rect1[1] + Equip_Cell_Offest[self.equip.part][1])
        self.rect.topleft = (pos[0], pos[1])

        print self.equip.part
    def draw(self):
        pos = (self.father.rect1[0] + Equip_Cell_Offest[self.equip.part][0], self.father.rect1[1] + Equip_Cell_Offest[self.equip.part][1])
        self.rect.topleft = (pos[0], pos[1])
        pygame.draw.rect(screen, item_background[self.equip.quality], (pos[0] - 2, pos[1] - 2, self.image.get_width() + 4, self.image.get_height() + 4))
        screen.blit(self.image, pos)

        my_font = pygame.font.Font("resource/msyh.ttf", 10)
        tx_level = Equip_Name[self.equip.part]
        level_surface = my_font.render(tx_level, True, (255, 255, 255))
        screen.blit(level_surface, (pos[0] + 12, pos[1] + 38))


class AttributeUI(util.node.Node):
    def __init__(self, **kwargs):
        super(AttributeUI, self).__init__(**kwargs)

        image = resource.getImage("bag_background")
        self.image1 = pygame.transform.scale(image, (image.get_width() * 4 / 7, image.get_height() * 5 / 2))
        self.image2 = pygame.transform.scale(image, (image.get_width() * 2 / 7, image.get_height() * 5 / 2))

        self.move_able = False
        self.rect1 = self.image1.get_rect()
        self.rect1.topleft = (100, 300)

        self.rect2 = self.image2.get_rect()
        self.rect2.topleft = self.rect1.topleft
        self.rect2[0] = self.rect1[0] + self.rect1[2]

        self.rebuild()

    def draw(self):
        screen.blit(self.image1, self.rect1.topleft)
        screen.blit(self.image2, self.rect2.topleft)

        my_font = pygame.font.Font("resource/msyh.ttf", 10)
        tx_level = u"等       级:   " + str(gamestate.player.level)
        level_surface = my_font.render(tx_level, True, (255, 255, 255))
        screen.blit(level_surface, (self.rect2[0] + 15, self.rect2[1] + 36))

        tx_exp = u"经       验:   " + str(gamestate.player.exp) + " / " + str(gamestate.player.n_exp)
        exp_surface = my_font.render(tx_exp, True, (255, 255, 255))
        screen.blit(exp_surface, (self.rect2[0] + 15, self.rect2[1] + 56))

        for attr in range(Attribute_Hp, Attribute_None):
            tx1 = gamestate.player.attribute_value_str(attr)
            tx1_surface = my_font.render(tx1, True, (255, 255, 255))
            screen.blit(tx1_surface, (self.rect2[0] + 15, self.rect2[1] + 56 + 20 + 20 * attr))

        for child in self.child:
            child.draw()

    def rebuild(self):
        self.child = []
        equips = gamestate.player.e_equips
        for i in range(len(equips)):
            if equips[i] is not None:
                self.add(EquipCell(self, equips[i]))

    def event(self, event):
        if event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            position = pygame.mouse.get_pos()
            if self.rect1.collidepoint(position):
                self.move_able = True
                self.top_layer()
        elif event.type == MOUSEMOTION:
            position = pygame.mouse.get_pos()
            if self.rect1.collidepoint(position):
                rel = pygame.mouse.get_rel()
                if self.move_able:
                    self.rect1[0] += rel[0]
                    self.rect1[1] += rel[1]
                    self.rect2[0] += rel[0]
                    self.rect2[1] += rel[1]
        elif event.type == MOUSEBUTTONUP:
            self.move_able = False
            self.back_layer()
#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import pygame
from pygame.locals import *
import mypygame
import util.node
import util.ui
import button
import gamestate
import resource
import battle
import label
import skill
from skill import *
screen = mypygame.screen


class SkillCell(util.node.Node):
    def __init__(self, father, pos, skill):
        super(SkillCell, self).__init__()

        self.father = father
        self.skill = skill
        self.image = resource.getImage("skill_" + str(self.skill.skill_id))
        self.index = pos
        self.rect = self.image.get_rect()
        x = pos % 6
        y = pos / 6
        self.rect.topleft = (self.father.rect[0] + 37.5 * x + 6 * (x + 1), self.father.rect[1] + 20 + 37.5 * y + 15 * (y + 1))

    def draw(self):
        pos = (self.rect[0], self.rect[1])
        screen.blit(self.image, pos)

        text = SC[self.skill.skill_id]["name"] + u" 等级: " + str(self.skill.level)
        label.FontLabel.draw_label(10, text, label.COLOR_WHITE, (pos[0], pos[1] + 24.5))

        text = "CD: " + str(round(self.skill.cool_down, 1))
        label.FontLabel.draw_label(10, text, label.COLOR_WHITE, (pos[0], pos[1] + 35.5))

    '''
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
    '''


class SkillUI(util.ui.BaseUI):
    def __init__(self, **kwargs):
        super(SkillUI, self).__init__()

        self.image = resource.getUIImage("skill_ui", 0.93, 2, u"技能")

        self.move_able = False
        self.rect = self.image.get_rect()
        self.rect.topleft = (580, 300)

        self.build()

    def draw(self):
        screen.blit(self.image, (self.rect[0], self.rect[1]))
        for child in self.child:
            child.draw()

    def build(self):
        skills = gamestate.player.skills
        for i in range(len(skills)):
             self.add(SkillCell(self, i, skills[i]))
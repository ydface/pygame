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
        self.rect.topleft = (self.father.rect[0] + 37.5 * x + 6 * (x + 1), self.father.rect[1] + 37.5 * y + 15 * (y + 1))

    def draw(self):
        pos = (self.rect[0], self.rect[1])
        screen.blit(self.image, pos)

        text = SC[self.skill.skill_id]["name"] + u" 等级: " + str(self.skill.level)
        label.FontLabel.draw_label(10, text, label.COLOR_WHITE, (pos[0], pos[1] + 24.5))

        text = "CD: " + str(round(self.skill.cool_down, 1))
        label.FontLabel.draw_label(10, text, label.COLOR_WHITE, (pos[0], pos[1] + 35.5))


class SkillUI(util.ui.BaseUI):
    def __init__(self, **kwargs):
        super(SkillUI, self).__init__()

        image = resource.getImage("bag_background")
        self.image = pygame.transform.scale(image, (image.get_width() * 2 / 3, image.get_height() * 2))

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
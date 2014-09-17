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

screen = mypygame.screen


class SkillCell(util.node.Node):
    def __init__(self, father, skill_id, pos, level):
        super(SkillCell, self).__init__()

        self.father = father
        self.skill_id = skill_id
        self.image = resource.getImage("skill_" + str(self.skill_id))
        self.index = pos
        self.level = level

        self.x = pos % 6
        self.y = pos / 6

    def draw(self):
        pos = (self.father.rect[0] + 37.5 * self.x + 5 + 6 * (self.x + 1), self.father.rect[1] + 37.5 * self.y + 15 + 15 * self.y)
        screen.blit(self.image, pos)

        text = skill.skill_config[str(self.skill_id)]["name"] + u" 等级: " + str(self.level)
        label.FontLabel.draw_label(10, text, label.COLOR_WHITE, (pos[0], pos[1] + 24.5))


class SkillUI(util.ui.BaseUI):
    def __init__(self, **kwargs):
        super(SkillUI, self).__init__()

        image = resource.getImage("bag_background")
        self.image = pygame.transform.scale(image, (image.get_width() * 2 / 3, image.get_height() * 2))

        self.move_able = False
        self.rect = self.image.get_rect()
        self.rect.topleft = (580, 300)

        self.skills = dict()

    def draw(self):
        self.skills.clear()
        screen.blit(self.image, (self.rect[0], self.rect[1]))
        for i in range(len(gamestate.player.skills)):
            skill_id = gamestate.player.skills[i].skill_id
            level = gamestate.player.skills[i].level
            self.skills[str(skill_id)] = SkillCell(self, skill_id, i, level)
        for cell in self.skills:
            self.skills[cell].draw()
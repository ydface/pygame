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

        my_font = pygame.font.Font("resource/msyh.ttf", 10)
        tx_level = str(self.level)
        level_surface = my_font.render(tx_level, True, (255, 255, 255))
        screen.blit(level_surface, (pos[0] + 28, pos[1] + 24.5))


class SkillUI(util.node.Node):
    def __init__(self, **kwargs):
        super(SkillUI, self).__init__(**kwargs)

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
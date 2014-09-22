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
import skill
from skill import *
screen = mypygame.screen


'''
class SkillDetail(util.node.Node):
    def __init__(self, skill_cell):
        super(SkillDetail, self).__init__()

        self.skill = skill_cell

        self.background = resource.getUIImage("sdetail", 0.8, 1, u"技能详情")
        self.rect = self.background.get_rect()
        self.rect.topleft = (self.skill.rect[0] + self.skill.rect[2] + 5, self.skill.rect[1])

    def draw(self):
        screen.blit(self.background, self.rect.topleft)
        screen.blit(self.skill.skill.image, (self.rect[0] + 5, self.rect[1] + 25))

        pos = [self.rect[0] + 5, self.rect[1] + 25]

        text = self.skill.skill.name
        label.FontLabel.draw_label(12, text, label.COLOR_WHITE, (pos[0], pos[1] + 36.5))
        text = u"等级: " + str(self.skill.skill.level)
        label.FontLabel.draw_label(12, text, label.COLOR_WHITE, (pos[0], pos[1] + 48.5))
        text = "CD: " + str(round(self.skill.skill.cool_down, 1))
        label.FontLabel.draw_label(12, text, label.COLOR_WHITE, (pos[0], pos[1] + 60.5))

        text = u"释放: " + str(self.skill.skill.max_release_time)
        label.FontLabel.draw_label(12, text, label.COLOR_WHITE, (pos[0], pos[1] + 72.5))

        lw = int(self.rect[2] / 12.0)
        text = u"详情: " + SC[self.skill.skill.skill_id]["content"]
        tl = len(text) / lw + 1

        for i in range(0, tl):
            tx = text[i * lw: lw * (i + 1)]
            label.FontLabel.draw_label(12, tx, label.COLOR_WHITE, (pos[0], pos[1] + 88.5 + i * 12))
'''


class SkillCell(util.node.Node):
    def __init__(self, father, pos, skill, **kwargs):
        super(SkillCell, self).__init__()

        self.father = father
        self.skill = skill
        #self.image = resource.getImage("skill_" + str(self.skill.res))
        self.index = pos
        self.rect = self.skill.image.get_rect()
        y_offest = kwargs.get("offest", 20)
        self.rect.topleft = (self.father.rect[0] + 5, self.father.rect[1] + y_offest + 45.5 * pos + 15)

    def draw(self):
        pos = (self.rect[0], self.rect[1])
        screen.blit(self.skill.image, pos)

        text = SC[self.skill.skill_id]["name"]
        label.FontLabel.draw_label(10, text, label.COLOR_WHITE, (pos[0] + 35, pos[1] + 0.5))
        text = u"等级: " + str(self.skill.level)
        label.FontLabel.draw_label(10, text, label.COLOR_WHITE, (pos[0] + 35, pos[1] + 10.5))
        text = "CD: " + str(round(self.skill.cool_down, 1)) + "s"
        label.FontLabel.draw_label(10, text, label.COLOR_WHITE, (pos[0] + 35, pos[1] + 20.5))

        text = u"释放: " + str(self.skill.max_release_time) + "s"
        label.FontLabel.draw_label(10, text, label.COLOR_WHITE, (pos[0] + 35 + 50, pos[1] + 20.5))

        text = u"详情: " + SC[self.skill.skill_id]["content"]
        label.FontLabel.draw_label(10, text, label.COLOR_WHITE, (pos[0], pos[1] + 30.5))

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
                i_detail = self.father.has_ctype_child(SkillDetail)
                if i_detail and i_detail.skill == self:
                    self.father.remove_ctype_child(SkillDetail)
                return False
            else:
                if not self.father.has_ctype_child(SkillDetail):
                    self.father.add(SkillDetail(self))
                    return True
            return False
        return False
    '''


class SkillUI(util.ui.BaseUI):
    def __init__(self, **kwargs):
        super(SkillUI, self).__init__()

        self.event_type = Event_Type_Child

        self.image = resource.getUIImage("skill_ui", 1.57, 2.1, u"技能")

        self.move_able = False
        self.rect = self.image.get_rect()
        self.rect.topleft = (430, 210)

        self.build()

    def draw(self):
        screen.blit(self.image, (self.rect[0], self.rect[1]))
        for child in self.child:
            child.draw()

    def build(self):
        skills = gamestate.player.skills
        for i in range(len(skills)):
             self.add(SkillCell(self, i, skills[i]))
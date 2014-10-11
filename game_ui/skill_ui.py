#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import pygame
import util.node
import mypygame
import gameresource
from util.node import *
import util.ui
import gamestate
import skill
import label


screen = mypygame.screen


class SkillCell(util.node.Node):
    def __init__(self, father, pos, skill, **kwargs):
        super(SkillCell, self).__init__()

        self.father = father
        self.skill = skill
        #self.image = resource.get_image("skill_" + str(self.skill.gameresource))
        self.index = pos
        self.rect = self.skill.image.get_rect()
        y_offest = kwargs.get("offest", 20)
        self.rect.topleft = (self.father.rect[0] + 5, self.father.rect[1] + y_offest + 45.5 * pos + 15)

        self.up_btn_rect = Rect(self.rect[0] + 200, self.rect[1], 60, 20)

    def draw(self):
        pos = (self.rect[0], self.rect[1])
        screen.blit(self.skill.image, pos)

        text = skill.SC[self.skill.skill_id]["name"]
        label.FontLabel.draw_label(10, text, label.COLOR_WHITE, (pos[0] + 35, pos[1] + 0.5))
        text = u"等级: " + str(self.skill.level)
        label.FontLabel.draw_label(10, text, label.COLOR_WHITE, (pos[0] + 35, pos[1] + 10.5))
        text = "CD: " + str(round(self.skill.cool_down, 1)) + "s"
        label.FontLabel.draw_label(10, text, label.COLOR_WHITE, (pos[0] + 35, pos[1] + 20.5))

        text = u"释放: " + str(self.skill.max_release_time) + "s"
        label.FontLabel.draw_label(10, text, label.COLOR_WHITE, (pos[0] + 35 + 50, pos[1] + 20.5))

        text = u"详情: " + skill.SC[self.skill.skill_id]["content"]
        label.FontLabel.draw_label(10, text, label.COLOR_WHITE, (pos[0], pos[1] + 30.5))

        label.FontLabel.draw_label(20, u"向上移", label.COLOR_WHITE, self.up_btn_rect.topleft)

    def self_event(self, event):
        if event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            position = pygame.mouse.get_pos()
            if self.up_btn_rect.collidepoint(position):
                if gamestate.player.skill_up(self.skill):
                    self.father.build()
                return True
        return False



class SkillUI(util.ui.BaseUI):
    def __init__(self, **kwargs):
        super(SkillUI, self).__init__()

        self.event_type = Event_Type_Child

        self.image = gameresource.getUIImage("skill_ui", 1.57, 2.6, u"技能")

        self.move_able = False
        self.rect = self.image.get_rect()
        self.rect.topleft = (430, 210)

        self.build()

    def draw(self):
        screen.blit(self.image, (self.rect[0], self.rect[1]))
        for child in self.child:
            child.draw()

    def build(self):
        self.child = []
        skills = gamestate.player.skills
        for i in range(len(skills)):
             self.add(SkillCell(self, i, skills[i]))
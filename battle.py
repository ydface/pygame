#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import pygame
import pygame.mixer
from pygame.locals import *
import mypygame
import game_ui.mission_ui
import random
import resource
import label
import util.node
import gamestate
import button
import skill
import monster
import player
from attribute import *

screen = mypygame.screen

class ExitButton(button.Button):
    def __init__(self, father):
        pos = [345, 500]
        image1 = resource.getImage("start_normal")
        image0 = resource.getImage("start_down")

        super(ExitButton, self).__init__(pos, image1, image0, father)

    def click_up_effect(self):
        gamestate.current_ui = game_ui.mission_ui.UIGame()


class BattleUnit(button.Button):
    def __init__(self, unit, image, pos, father, target, **kwargs):
        super(BattleUnit, self).__init__(pos, image, resource.getImage("header_line"), father)
        self.unit = unit
        self.dead = False
        self.father = father
        self.target = target
        self.skills = kwargs.get('skill', [skill.Skill(101, 1, self.unit), skill.Skill(102, 1, self.unit)])
        self.next_skill = self.skills[0]
        self.recover_time = 0.1
        self.anger = 0

    def draw(self):
        screen.blit(self.image, (self.rect[0], self.rect[1]))

        my_font = pygame.font.Font("resource/msyh.ttf", 10)
        #绘制等级
        tx_lv = str(self.unit.level)
        lv_surface = my_font.render(tx_lv, True, (255, 255, 255))
        screen.blit(lv_surface, (self.rect[0] + 60, self.rect[1] + 6))
        #绘制血条
        hp_label = int(float(self.unit.attribute_value(Attribute_Hp)) / self.unit.attribute_value(Attribute_Max_Hp) * 100)
        if hp_label:
            pygame.draw.rect(screen, (255, 0, 0), (self.rect[0] + 69, self.rect[1] + 24, hp_label, 8))
        my_font = pygame.font.Font("resource/msyh.ttf", 8)
        tx_hp = self.unit.attribute_value_str(Attribute_Hp) + " / " + self.unit.attribute_value_str(Attribute_Max_Hp)
        hp_surface = my_font.render(tx_hp, True, (255, 255, 255))
        screen.blit(hp_surface, (self.rect[0] + 71, self.rect[1] + 23))

        ##绘制怒气条
        anger_label = int(float(self.anger) / 100 * 100)
        if anger_label:
            pygame.draw.rect(screen, (0, 0, 255), (self.rect[0] + 69, self.rect[1] + 34, anger_label, 8))
        #my_font = pygame.font.Font("resource/msyh.ttf", 8)
        tx_anger = str(self.anger) + " / " + str(100)
        anger_surface = my_font.render(tx_anger, True, (255, 255, 255))
        screen.blit(anger_surface, (self.rect[0] + 83, self.rect[1] + 33))

        if not self.dead:
            self.next_skill.draw_process(self)
        else:
            if isinstance(self.unit, player.Player):
                pass
        for child in self.child:
            child.draw()

    def click_up_effect(self):
        if self in self.father.monsters and not self.dead:
            self.target.target = self

    def update(self, **kwargs):
        time = kwargs['time']

        if not self.dead and not self.father.end:
            for s in self.skills:
                s.cd_update(**kwargs)
            self.next_skill.release_update(**kwargs)
        if self.father.end:
            self.recover(time)

        for child in self.child:
            child.update(**kwargs)

    def recover(self, time):
        self.recover_time -= time
        if self.recover_time <= 0:
            self.recover_time = 0.1
            hpr = self.unit.attribute_value(Attribute_Max_Hp) / 30
            if self.unit.hp_inc(hpr):
                self.dead = False
                self.target = None

                for s in self.skills:
                    s.go_cd()
                self.father.new_battle()

    def damaged(self, damage):
        self.unit.hp_dec(damage)

    def anger_change(self, val):
        self.anger -= val
        self.anger = min([max([self.anger, 0]), 100])

    def recover_hp(self, val):
        self.unit.hp_inc(val)

    def active(self):
        if self.dead:
            return
        if not self.target or self.target.dead:
            for m in self.father.monsters:
                if not m.dead:
                    self.target = m

        if self.next_skill.available:
            effect = skill.SkillEffect(self.next_skill, self, self.target)
            effect.effect_active()
            self.skill_available()

        if self.target.unit.attribute_value(Attribute_Hp) == 0:
            self.target.dead = True
            if isinstance(self.target.unit, monster.Monster):
                gamestate.player.add_exp(self.target.unit.exp)
                gamestate.player.get_equipment(self.target.unit.equip)

                view = label.LabelViewState(label.ViewTimer, 0.6, [0, -0.4])
                rect = [self.rect[0] + 13, self.rect[1] - 3]
                lb = label.FontLabel(rect, view, 12, text="exp " + str(self.target.unit.exp), color=label.COLOR_GREEN, father=self)
                self.add(lb)

    def add_hp_change_label(self, text, font_size, color):
        view = label.LabelViewState(label.ViewTimer, 0.6, [0, -0.4])
        rect = [self.rect[0] + 200, self.rect[1] + 30]
        lb = label.FontLabel(rect, view, font_size, text=text, color=color, father=self)
        self.add(lb)

    def skill_available(self):
        self.next_skill = self.skills[0]
        for s in self.skills:
            if self.anger < s.anger:
                continue
            if s.cool_down <= 0:
                self.next_skill = s
            elif s.cool_down < self.next_skill.cool_down:
                self.next_skill = s


class Battle(util.node.Node):
    def __init__(self, level):
        super(Battle, self).__init__()

        self.end = True
        self.player = BattleUnit(gamestate.player, resource.getImage("header_line"), [100, 360], self, None, skill=gamestate.player.skills)
        self.player.dead = True
        self.add(self.player)
        self.monsters = []

        self.next_delay = random.randint(3, 5)
        self.add(ExitButton(self))

    def update(self, **kwargs):
        time = kwargs['time']
        self.player.update(**kwargs)
        if not self.end:
            self.player.active()

            if not self.check_end():
                for monster in self.monsters:
                    if monster.dead:
                        continue
                    monster.update(**kwargs)
                    monster.active()
                    if self.check_end():
                        break
            for child in self.child:
                child.update(**kwargs)

    def new_battle(self):
        self.end = False
        self.player.dead = False
        num = random.randint(1, 6)
        for i in range(0, num):
            level = random.randint(max([1, gamestate.player.level - 3]), gamestate.player.level)
            mid = random.randint(1, 5)
            m = BattleUnit(monster.Monster(mid, level), resource.getImage("header_line"), [400, 20 + 80 * i], self, self.player)
            self.monsters.append(m)
            self.add(m)

    def check_end(self):
        if self.end:
            return self.end

        if self.player.unit.attribute_value(Attribute_Hp) == 0:
            self.end = True
            for m in self.monsters:
                self.remove(m)
            self.monsters = []
        else:
            for m in self.monsters:
                if not m.dead:
                    return False
            self.end = True

            for m in self.monsters:
                self.remove(m)
            self.monsters = []
        return self.end


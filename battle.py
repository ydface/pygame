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
import attribute
import skill

screen = mypygame.screen

class ExitButton(button.Button):
    def __init__(self, father):
        rect = Rect(345, 500, 100, 50)
        image1 = resource.getImage("start_normal")
        image0 = resource.getImage("start_down")

        super(ExitButton, self).__init__(rect, image1, image0, father)

    def click_up_effect(self):
        gamestate.current_ui = game_ui.mission_ui.UIGame()


class BattleUnit(button.Button, attribute.Attribute):
    def __init__(self, level, image, rect, father, target, **kwargs):
        super(BattleUnit, self).__init__(rect, image, resource.getImage("header_line"), father)
        attribute.Attribute.__init__(self)
        self.hp = 1000 + level * 100
        self.max_hp = self.hp
        self.attack = 100 + level * 20
        self.dead = False
        self.father = father
        self.speed = random.randint(30, 90)
        self.target = target
        self.skills = kwargs.get('skill', [skill.Skill(1, 1)])
        self.exp = random.randint(10, 100)
        self.next_skill = self.skills[0]
        self.anger = 0

    def draw(self):
        screen.blit(self.image, (self.rect[0], self.rect[1]))
         #绘制血条
        hp_label = int(float(self.hp) / self.max_hp * 100)
        if hp_label:
            pygame.draw.rect(screen, (255, 0, 0), (self.rect[0] + 69, self.rect[1] + 24, hp_label, 8))
        my_font = pygame.font.Font("resource/msyh.ttf", 8)
        tx_hp = str(self.hp) + " / " + str(self.max_hp)
        hp_surface = my_font.render(tx_hp, True, (255, 255, 255))
        screen.blit(hp_surface, (self.rect[0] + 79, self.rect[1] + 23))

        ##绘制怒气条
        anger_label = int(float(self.anger) / 100 * 100)
        if anger_label:
            pygame.draw.rect(screen, (0, 0, 255), (self.rect[0] + 69, self.rect[1] + 34, anger_label, 8))
        my_font = pygame.font.Font("resource/msyh.ttf", 8)
        tx_anger = str(self.anger) + " / " + str(100)
        anger_surface = my_font.render(tx_anger, True, (255, 255, 255))
        screen.blit(anger_surface, (self.rect[0] + 83, self.rect[1] + 33))

        if self.dead:
            self.child = []
            return

        #绘制技能释放进度条
        self.next_skill.draw_process(self)

        for child in self.child:
            child.draw()

    def click_up_effect(self):
        if self in self.father.monsters and not self.dead:
            self.target.target = self

    def update(self, **kwargs):
        time = kwargs['time']

        if not self.dead:
            for s in self.skills:
                s.cd_update(**kwargs)
            self.next_skill.release_update(**kwargs)

        for child in self.child:
            child.update(**kwargs)

    def recover(self):
        self.hp = self.max_hp
        self.dead = True
        self.target = None

        for s in self.skills:
            s.go_cd()

    def damaged(self, damage):
        if self.hp <= damage:
            self.hp = 0
        else:
            self.hp -= damage

    def anger_change(self, val):
        self.anger -= val
        if self.anger > 100:
            self.anger = 100
        elif self.anger < 0:
            self.anger = 0

    def active(self):
        if self.dead:
            return
        if not self.target or self.target.dead:
            for monster in self.father.monsters:
                if not monster.dead:
                    self.target = monster

        if self.next_skill.available:
            effect = skill.SkillEffect(self.next_skill, self, self.target)
            effect.effect_active()
            self.skill_available()

        if self.target.hp <= 0:
            self.target.hp = 0
            self.target.dead = True
            if self in self.father.monsters:
                gamestate.player.add_exp(self.target.exp)

    def add_hp_change_label(self, text, font_size, color):
        view = label.LabelViewState(label.ViewTimer, 0.8, [0, -0.3])
        rect = Rect(self.rect[0] + 200, self.rect[1] + 30, 100, 50)
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
        self.player = BattleUnit(gamestate.player.level, resource.getImage("header_line"), Rect(100, 360, 100, 50), self, None, skill=gamestate.player.skills)
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
        else:
            self.next_delay -= time
            if self.next_delay <= 0:
                self.new_battle()
                self.next_delay = random.randint(3, 6)

    def new_battle(self):
        self.end = False
        self.player.dead = False
        num = random.randint(1, 6)
        for i in range(0, num):
            level = random.randint(1, gamestate.player.level)
            monster = BattleUnit(level, resource.getImage("header_line"), Rect(400, 20 + 80 * i, 100, 50), self, self.player)
            self.monsters.append(monster)
            self.add(monster)

    def check_end(self):
        if self.end:
            return self.end

        if self.player.hp <= 0:
            self.end = True
            self.player.recover()
            for monster in self.monsters:
                self.remove(monster)
            self.monsters = []
        else:
            for monster in self.monsters:
                if not monster.dead:
                    return False
            self.end = True
            self.player.recover()

            for monster in self.monsters:
                self.remove(monster)
            self.monsters = []

            gamestate.player.add_exp(1)

        return self.end


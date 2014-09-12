#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import pygame, sys, pygame.mixer
from pygame.locals import *
import mypygame
import game_ui.mission_ui
import random
import resource
import label
import util.node
import gamestate
import button

screen = mypygame.screen

LayerButton = gamestate.LayerButton
LayerLabel = gamestate.LayerLabel
LayerUI = gamestate.LayerUI

count = 0
class BattleUnit(button.Button):
    def __init__(self, level, image, rect, father):
        button.Button.__init__(self, rect, image, resource.getImage("attribute"), father)
        self.hp = 1000 + level * 100
        self.maxHp = self.hp
        self.attack = 100 + level * 20
        self.image = image
        self.rect = rect
        self.dead = False
        self.father = father
        self.speed = random.randint(30, 90)
        self.activeProcess = 0
        self.deadDraw = False
        self.attack_enable = False

    def draw_self(self):
        global count
        screen.blit(self.image, (self.rect[0], self.rect[1]))

        #绘制技能释放进度条
        if not self.dead and not self.father.end:
            pygame.draw.rect(screen, (255, 255, 0), (self.rect[0] + 69, self.rect[1] + 54, 100, 4))
            w = float(self.activeProcess) / self.speed * 100
            pygame.draw.rect(screen, (255, 0, 0), (self.rect[0] + 69, self.rect[1] + 54, w, 4))

            count += 1
            rect = Rect(self.rect[0] + 69 + 35, self.rect[1] + 48, 100, 4)
            view = label.LabelViewState(label.ViewTimer, 2)
            text = str(round(float(self.activeProcess) / self.speed, 2))
            text1 = label.FontLabel(rect, view, 12, text)
            self.father.layer_child[LayerLabel][str(count)] = text1

        #绘制血条
        w = int(float(self.hp) / self.maxHp * 100)
        if w:
            pygame.draw.rect(screen, (255, 0, 0), (self.rect[0] + 69, self.rect[1] + 24, w, 8))

        if self.dead and not self.deadDraw:
            rect = Rect(self.rect[0] + 77, self.rect[1] + 3, 100, 50)
            view = label.LabelViewState(label.ViewForver)
            text1 = label.FontLabel(rect, view, 16, "Dead")
            self.father.layer_child[LayerLabel][str(count)] = text1
            self.deadDraw = True

    def update(self):
        self.activeProcess += 1
        if self.activeProcess > self.speed:
            self.activeProcess = 0
            self.attack_enable = True

    def attack_target(self, other):
            self.attack_enable = False

            global count
            count += 1
            other.hp -= self.attack
            if other.hp <= 0:
                other.hp = 0
            rect = Rect(other.rect[0] + 200, other.rect[1] + 30, 100, 50)
            view = label.LabelViewState(label.ViewTimer, 120, [0, -0.3])
            text = str(-self.attack)
            text1 = label.FontLabel(rect, view, 16, text)
            self.father.layer_child[LayerLabel][str(count)] = text1

            if other.hp <= 0:
                other.dead = True

class Battle(util.node.Node):
    def __init__(self, level, father):
        util.node.Node.__init__(self)
        num = random.randint(2, 5)

        self.end = False
        self.playerWin = False
        for i in range(0, num):
            self.layer_child[LayerButton][str(i)] = BattleUnit(1, resource.getImage("header_line"), Rect(400, 20 + 80 * i, 100, 50), self)
        self.layer_child[LayerButton]["player"] = BattleUnit(5, resource.getImage("header_line"), Rect(100, 360, 100, 50), self)

        self.next_delay = 0

    def update(self):
        targetIdx = random.randint(0, len(self.layer_child[LayerButton]) - 2)
        target = self.layer_child[LayerButton][str(targetIdx)]
        player = self.layer_child[LayerButton]["player"]
        player.update()
        if not target.dead and not player.dead and player.attack_enable:
            player.attack_target(target)
            self.check_end()

        if not self.end:
            for unit in self.layer_child[LayerButton]:
                monster = self.layer_child[LayerButton][unit]
                monster.update()
                if not monster.dead and monster.attack_enable and unit != "player":
                    monster.attack_target(player)
                    self.check_end()
                    if self.end:
                        break
        if self.end:
            self.next_delay += 1

            rect = Rect(200, 30, 100, 50)
            view = label.LabelViewState(label.ViewForver)
            text = str(60 - self.next_delay) + u"帧后返回"
            text1 = label.FontLabel(rect, view, 16, text)
            self.layer_child[LayerLabel]["return"] = text1

        if self.next_delay > 60:
            if self.playerWin:
                gamestate.current_ui = Battle(3,None)
            else:
                gamestate.current_ui = game_ui.mission_ui.UIGame()

        for key in self.layer_child[LayerLabel].keys():
            view_state = self.layer_child[LayerLabel][key]
            if view_state.viewState.view == label.ViewTimer and not view_state.viewState.isView:
                del self.layer_child[LayerLabel][key]


    def check_end(self):
        player = self.layer_child[LayerButton]["player"]
        if player.hp <= 0:
            self.end = True

            rect = Rect(40, 30, 100, 50)
            view = label.LabelViewState(label.ViewForver)
            text1 = label.FontLabel(rect, view, 16, "You Dead")
            self.layer_child[LayerLabel]["result"] = text1

        else:
            for unit in self.layer_child[LayerButton]:
                monster = self.layer_child[LayerButton][unit]
                if not monster.dead and unit != "player":
                    return
            self.end = True
            self.playerWin = True

            rect = Rect(40, 30, 100, 50)
            view = label.LabelViewState(label.ViewForver)
            text1 = label.FontLabel(rect, view, 16, "You Win")
            self.layer_child[LayerLabel]["result"] = text1


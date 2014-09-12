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

    def draw_self(self):
        global count
        screen.blit(self.image, (self.rect[0], self.rect[1]))
        w = int(float(self.hp) / self.maxHp * 100)
        if w:
            pygame.draw.rect(screen, (255, 0, 0), (self.rect[0] + 69, self.rect[1] + 24, w, 8))
        if self.dead and not self.deadDraw:
            rect = Rect(self.rect[0] + 77, self.rect[1] + 3, 100, 50)
            view = label.LabelViewState(label.ViewForver)
            text1 = label.FontLabel(rect, view, "resource/msyh.ttf", 16, "Dead")
            self.father.layer_child[LayerLabel][str(count)] = text1
            self.deadDraw = True

    def attackTarget(self, other):
        self.activeProcess += 1
        if self.activeProcess > self.speed:
            self.activeProcess = 0
            global count
            count += 1
            other.hp -= self.attack
            if other.hp <= 0:
                other.hp = 0
            rect = Rect(other.rect[0] + 200, other.rect[1] + 30, 100, 50)
            view = label.LabelViewState(label.ViewTimer, 120, [0, -0.3])
            text = str(-self.attack)
            text1 = label.FontLabel(rect, view, "resource/msyh.ttf", 16, text)
            self.father.layer_child[LayerLabel][str(count)] = text1

            if other.hp <= 0:
                other.dead = True

class Battle(util.node.Node):
    def __init__(self, level, father):
        util.node.Node.__init__(self)
        num = random.randint(2, 5)

        self.end = False
        self.playerWin = False
        self.monsters = []
        for i in range(0, num):
            self.layer_child[LayerButton][str(i)] = BattleUnit(1, resource.getImage("header_line"), Rect(400, 20 + 80 * i, 100, 50), self)
        self.layer_child[LayerButton]["player"] = BattleUnit(30, resource.getImage("header_line"), Rect(100, 360, 100, 50), self)

        self.next_delay = 0

    def update(self):
        targetIdx = random.randint(0, len(self.layer_child[LayerButton]) - 2)
        target = self.layer_child[LayerButton][str(targetIdx)]
        player = self.layer_child[LayerButton]["player"]
        if not target.dead and not player.dead:
            player.attackTarget(target)
            self.checkEnd()

        if not self.end:
            for unit in self.layer_child[LayerButton]:
                monster = self.layer_child[LayerButton][unit]
                if not monster.dead and unit != "player":
                    monster.attackTarget(player)
                    self.checkEnd()
                    if self.end:
                        break
        if self.end:
            self.next_delay += 1

            rect = Rect(200, 30, 100, 50)
            view = label.LabelViewState(label.ViewForver)
            text = str(60 - self.next_delay) + u"帧后返回"
            text1 = label.FontLabel(rect, view, "resource/msyh.ttf", 16, text)
            self.layer_child[LayerLabel]["return"] = text1

        if self.next_delay > 60:
            gamestate.current_ui = game_ui.mission_ui.UIGame()

    def checkEnd(self):
        player = self.layer_child[LayerButton]["player"]
        if player.hp <= 0:
            self.end = True

            rect = Rect(40, 30, 100, 50)
            view = label.LabelViewState(label.ViewForver)
            text1 = label.FontLabel(rect, view, "resource/msyh.ttf", 16, "You Dead")
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
            text1 = label.FontLabel(rect, view, "resource/msyh.ttf", 16, "You Win")
            self.layer_child[LayerLabel]["result"] = text1


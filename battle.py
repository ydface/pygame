#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import pygame, sys, pygame.mixer
from pygame.locals import *
import mypygame
import random
import resource
import label

screen = mypygame.screen

count = 0
class BattleUnit(object):
    def __init__(self, level, image, rect, father):
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

    def drawSelf(self):
        global count
        screen.blit(self.image, (self.rect[0], self.rect[1]))
        w = int(float(self.hp) / self.maxHp * 100)
        if w:
            pygame.draw.rect(screen, (255, 0, 0), (self.rect[0] + 69, self.rect[1] + 24, w, 8))
        if self.dead and not self.deadDraw:
            rect = Rect(self.rect[0] + 77, self.rect[1] + 3, 100, 50)
            view = label.LabelViewState(label.ViewForver)
            text1 = label.FontLabel(rect, view, "resource/msyh.ttf", 16, "Dead")
            self.father.labels[str(count)] = text1
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
            self.father.labels[str(count)] = text1

            if other.hp <= 0:
                other.dead = True

class Battle(object):
    def __init__(self, level, father):
        num = random.randint(2, 5)

        self.end = False
        self.playerWin = False
        self.father = father
        self.monsters = []
        for i in range(0, num):
            self.monsters.append(BattleUnit(1, resource.getImage("header_line"), Rect(400, 20 + 80 * i, 100, 50), self.father))
        self.player = BattleUnit(30, resource.getImage("header_line"), Rect(100, 360, 100, 50), self.father)

    def update(self):
        targetIdx = random.randint(0,len(self.monsters) - 1)
        target = self.monsters[targetIdx]
        if not target.dead and not self.player.dead:
            self.player.attackTarget(target)
            self.checkEnd()
        if not self.end:
            for unit in self.monsters:
                if not unit.dead:
                    unit.attackTarget(self.player)
                    self.checkEnd()
                    if self.end:
                        break

    def drawSelf(self):
        self.player.drawSelf()
        for unit in self.monsters:
            unit.drawSelf()

    def checkEnd(self):
        if self.player.hp <= 0:
            self.end = True

            rect = Rect(40, 30, 100, 50)
            view = label.LabelViewState(label.ViewForver)
            text1 = label.FontLabel(rect, view, "resource/msyh.ttf", 16, "You Dead")
            self.father.labels["result"] = text1

        else:
            for unit in self.monsters:
                if not unit.dead:
                    return
            self.end = True
            self.playerWin = True

            rect = Rect(40, 30, 100, 50)
            view = label.LabelViewState(label.ViewForver)
            text1 = label.FontLabel(rect, view, "resource/msyh.ttf", 16, "You Win")
            self.father.labels["result"] = text1


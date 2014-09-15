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

screen = mypygame.screen
screenwidth = mypygame.screenwidth
screenheight = mypygame.screenheight

class LevelButton1(button.Button):
    def __init__(self, father):
        image1 = resource.getImage("level_1_1")
        image1 = pygame.transform.scale(image1,(image1.get_width() / 2, image1.get_height() / 2))

        image0 = resource.getImage("level_1_0")
        image0 = pygame.transform.scale(image0,(image0.get_width() / 2, image0.get_height() / 2))

        rect = Rect(163, 111, image0.get_width(), image0.get_height())
        super(LevelButton1, self).__init__(rect, image0, image1, father)

    def click_up_effect(self):
        gamestate.SenceLevel = gamestate.LEVEL_1
        gamestate.current_ui = battle.Battle(3)


class LevelButton2(button.Button):
    def __init__(self, father):
        image1 = resource.getImage("level_2_1")
        image1 = pygame.transform.scale(image1,(image1.get_width() / 2, image1.get_height() / 2))

        image0 = resource.getImage("level_2_0")
        image0 = pygame.transform.scale(image0,(image0.get_width() / 2, image0.get_height() / 2))

        rect = Rect(100, 104, image0.get_width(), image0.get_height())

        super(LevelButton2, self).__init__(rect, image0, image1, father)

    def click_up_effect(self):
        gamestate.SenceLevel = gamestate.LEVEL_2
        gamestate.current_ui = battle.Battle(3)


class LevelButton3(button.Button):
    def __init__(self, father):
        image1 = resource.getImage("level_3_1")
        image1 = pygame.transform.scale(image1,(image1.get_width() / 2, image1.get_height() / 2))

        image0 = resource.getImage("level_3_0")
        image0 = pygame.transform.scale(image0,(image0.get_width() / 2, image0.get_height() / 2))

        rect = Rect(100, 160, image0.get_width(), image0.get_height())

        super(LevelButton3, self).__init__(rect, image0, image1, father)

    def click_up_effect(self):
        gamestate.SenceLevel = gamestate.LEVEL_3
        gamestate.current_ui = battle.Battle(3)

base_offest = 200


class MissionMapUI(util.node.Node):
    def __init__(self, father, **kwargs):
        super(MissionMapUI, self).__init__(**kwargs)

        self.father = father

        self.offest = 0

        background = resource.getImage("big_map")
        self.background = pygame.transform.scale(background,(background.get_width() / 2, background.get_height() / 2))

        background_side = resource.getImage("map_key")
        self.background_side = pygame.transform.scale(background_side,(background_side.get_width() / 2, background_side.get_height() / 2))

        self.level1 = LevelButton1(self)
        self.level2 = LevelButton2(self)
        self.level3 = LevelButton3(self)

        self.add(self.level1)
        self.add(self.level2)
        self.add(self.level3)

    def draw(self):
        if gamestate.SenceLevel == gamestate.LEVEL_0:
            screen.blit(self.background_side, (base_offest + self.background.get_width(), 10))
            screen.set_clip(base_offest + 3 + self.background.get_width() - self.offest, 20, self.offest, self.background.get_height())
            screen.blit(self.background, (base_offest + self.background.get_width() - self.offest, 20))

            for child in self.child:
                child.draw()

            screen.set_clip((0, 0, mypygame.screenwidth, mypygame.screenwidth))

            screen.blit(self.background_side, (base_offest + 6 + self.background.get_width() - self.offest - self.background_side.get_width(), 10))

    def update(self, **kwargs):
        if gamestate.SenceLevel == gamestate.LEVEL_0:
            if self.offest < self.background.get_width() - 3:
                self.event_enable = False
                self.offest = self.offest + 3
                if self.offest >= self.background.get_width() - 3:
                    self.event_enable = True
                if self.offest > self.background.get_width():
                    self.offest = self.background.get_width() - 3
                if self.offest > 136 - self.level1.image.get_width():
                    self.level1.rect[0] = base_offest + self.background.get_width() + 5 + 2*self.level1.image.get_width()/3 - self.offest
                if self.offest > 290 - self.level2.image.get_width():
                    self.level2.rect[0] = base_offest + 168 + self.background.get_width() + 5 + self.level2.image.get_width() - self.offest
                if self.offest > 21 - self.level3.image.get_width():
                    self.level3.rect[0] = base_offest - 75 + self.background.get_width() + 5 + self.level3.image.get_width() - self.offest

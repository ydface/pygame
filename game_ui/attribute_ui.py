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
from attribute import *

screen = mypygame.screen


class AttributeUI(util.node.Node):
    def __init__(self, **kwargs):
        super(AttributeUI, self).__init__(**kwargs)

        self.image = resource.getImage("attribute")
        self.move_able = False
        self.rect = Rect(100, 300, self.image.get_width(), self.image.get_height())

    def draw(self):
        screen.blit(self.image, (self.rect[0], self.rect[1]))

        my_font = pygame.font.Font("resource/msyh.ttf", 8)
        tx_level = str(gamestate.player.level)
        level_surface = my_font.render(tx_level, True, (255, 255, 255))
        screen.blit(level_surface, (self.rect[0] + 75, self.rect[1] + 96))

        tx_exp = str(gamestate.player.exp) + " / " + str(gamestate.player.n_exp)
        exp_surface = my_font.render(tx_exp, True, (255, 255, 255))
        screen.blit(exp_surface, (self.rect[0] + 165, self.rect[1] + 96))

        for attr in range(Attribute_Hp, Attribute_None):
            x_idx = attr % 2
            y_idx = attr // 2
            tx1 = gamestate.player.attribute_value_str(attr)
            tx1_surface = my_font.render(tx1, True, (255, 255, 255))
            screen.blit(tx1_surface, (self.rect[0] + 75 + 96 * x_idx, self.rect[1] + 114 + 18 * y_idx))

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
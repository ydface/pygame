#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import pygame
try:
    import pygame.mixer as mixer
except ImportError:
    import android.mixer as mixer
import mypygame
import util.node
from util.color import *
import traceback
screen = mypygame.screen

#永久显示
ViewForver = 1

#定时显示
ViewTimer = 2

#间隔显示
ViewInterval = 3

#[0][0] 第一位表示上下方向位移,第二位表示左右方向位移
class LabelViewState(object):
    def __init__(self, view, last_time=1, move=[0, 0]):
        super(LabelViewState, self).__init__()
        self.view = view
        self.move = move
        self.last_time = last_time
        self.isView = True


class FontLabel(util.node.Node):
    TTF_Font = "resource/msyh.ttf"
    try:
        D_Font = {
            8: pygame.font.Font(TTF_Font, 8),
            9: pygame.font.Font(TTF_Font, 9),
            10: pygame.font.Font(TTF_Font, 10),
            12: pygame.font.Font(TTF_Font, 12),
            14: pygame.font.Font(TTF_Font, 14),
            16: pygame.font.Font(TTF_Font, 16),
            20: pygame.font.Font(TTF_Font, 20)
        }
    except:
        log = open("log.txt", 'a')
        traceback.print_exc(file=log)
        log.write("\n")
        log.flush()
        log.close()

    def __init__(self, pos, view_state, font_size, **kwargs):
        super(FontLabel, self).__init__(**kwargs)

        self.pos = pos
        self.viewState = view_state
        self.father = kwargs.get('father', None)

        text = kwargs['text']
        color = kwargs.get('color', COLOR_WHITE)

        self.text_surface = FontLabel.D_Font[font_size].render(text, True, color)

    def update(self, **kwargs):
        self.pos[0] = self.pos[0] + self.viewState.move[0]
        self.pos[1] = self.pos[1] + self.viewState.move[1]
        if self.viewState.view == ViewTimer:
            time = kwargs['time']
            self.viewState.last_time -= time
            if self.viewState.last_time <= 0:
                self.viewState.isView = False
                self.father.remove(self)
        elif self.viewState.view == ViewInterval:
            self.viewState.curFrame += + 1
            if self.viewState.viewFrame == self.viewState.curFrame:
                self.viewState.isView = not self.viewState.isView
                self.viewState.curFrame = 0

    def draw(self):
        if self.viewState.isView:
            screen.blit(self.text_surface, (self.pos[0], self.pos[1]))

    @staticmethod
    def draw_label(font_size, text, color, pos):
        surface = FontLabel.D_Font[font_size].render(text, True, color)
        screen.blit(surface, pos)

    @staticmethod
    def draw_rect_line(pos, wh, color):
        pygame.draw.line(screen, color, (pos[0], pos[1]), (pos[0], pos[1] + wh[1]), 2)
        pygame.draw.line(screen, color, (pos[0], pos[1]), (pos[0] + wh[0], pos[1]), 2)
        pygame.draw.line(screen, color, (pos[0] + wh[0], pos[1]), (pos[0] + wh[0], pos[1] + wh[1]), 2)
        pygame.draw.line(screen, color, (pos[0], pos[1] + wh [1]), (pos[0] + wh[0], pos[1] + wh[1]), 2)
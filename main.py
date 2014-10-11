#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys

#导入pygame模块，第8行的作用是简化你的输入，如不用在event前再加上pygame模块名
import pygame
from pygame.locals import *
#from game_ui import main_ui
import mypygame
import gameresource
import gamestate
import label
import save_data
import traceback

screen = mypygame.screen
clock = mypygame.clock


def draw_mouse():
    pos = pygame.mouse.get_pos()
    screen.blit(gameresource.get_image("mouse1"), (pos[0], pos[1]))


def update():
    while mypygame.running:
        screen.blit(gameresource.background[gamestate.SenceLevel], (0, 0))
        for event in pygame.event.get():
            #接收到窗口关闭事件
            if event.type == QUIT:
                mypygame.running = False
            else:
                gamestate.current_ui.event(event)

        frame = clock.tick(60) / 1000.0
        gamestate.current_ui.update(time=frame)
        gamestate.current_ui.draw()

        text = "FPS : " + str(int(1 / frame))
        label.FontLabel.draw_label(16, text, label.COLOR_WHITE, (10, 600))

        #先绘制场景界面，再绘制鼠标，鼠标在最上层
        #if mypygame.android is None:
        draw_mouse()

        #将Surface对象绘制在屏幕上
        pygame.display.update()

    if not mypygame.running:
        gamestate.current_ui = None
        save_data.Save.save()
        pygame.quit()


def start():
    update()

if __name__ == "__main__":
    start()

    

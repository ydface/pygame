#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys

#导入pygame模块，第8行的作用是简化你的输入，如不用在event前再加上pygame模块名
import pygame
from pygame.locals import *
from game_ui import main_ui
import mypygame
import gamestate
import resource
import label
import save_data

screen = mypygame.screen
clock = mypygame.clock


def draw_mouse():
    pos = pygame.mouse.get_pos()
    screen.blit(resource.getImage("mouse"), (pos[0], pos[1]))


def hello_world():
    resource.init()

    gamestate.current_ui = main_ui.UIMain()

    #循环，直到接收到窗口关闭事件
    while mypygame.running:
         #处理事件
        screen.blit(resource.background[gamestate.SenceLevel], (0, 0))
        for event in pygame.event.get():
            #接收到窗口关闭事件
            if event.type == QUIT:
                mypygame.running = False
            else:
                gamestate.current_ui.event(event)

        frame = clock.tick(60) / 1000.0
        gamestate.current_ui.update(time=frame)
        gamestate.current_ui.draw()

        text = "FPS : " + str(1 / frame)
        view = label.LabelViewState(label.ViewForver)
        fps_label = label.FontLabel(Rect(10, 600, 10, 10), view, 16, text=text, father=None)
        fps_label.draw()

        #先绘制场景界面，再绘制鼠标，鼠标在最上层
        draw_mouse()

        #将Surface对象绘制在屏幕上
        pygame.display.update()

    gamestate.current_ui = None

    save_data.Save.save()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    hello_world()
    

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
                gamestate.current_ui.handle_event(event)
        gamestate.current_ui.update()
        gamestate.current_ui.draw_self()

        frame = clock.tick(60)
        text = "FPS : " + str(1000.0 / frame)
        view = label.LabelViewState(label.ViewForver)
        fps_label = label.FontLabel(Rect(10, 600, 10, 10), view, 16, text)
        fps_label.draw_self()

        #先绘制场景界面，再绘制鼠标，鼠标在最上层
        draw_mouse()

        #将Surface对象绘制在屏幕上
        pygame.display.update()

    gamestate.current_ui = None

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    hello_world()
    

#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys

#导入pygame模块，第8行的作用是简化你的输入，如不用在event前再加上pygame模块名
import pygame
from pygame.locals import *
from game_ui import main_ui
from game_ui import mission_ui

import mypygame
import gamestate
import resource
import label

pygame = mypygame.pygame
screen = mypygame.screen
clock = mypygame.clock

def draw_mouse():
    pos = pygame.mouse.get_pos()
    screen.blit(resource.getImage("mouse"), (pos[0], pos[1]))

def hello_world():
    resource.init()

    main = main_ui.UIMain()
    game = mission_ui.UIGame()

    #循环，直到接收到窗口关闭事件
    while mypygame.running:
         #处理事件
        screen.blit(resource.background[gamestate.SenceLevel], (0, 0))
        for event in pygame.event.get():
            #接收到窗口关闭事件
            if event.type == QUIT:
                mypygame.running = False
            else:
                if gamestate.GameState == gamestate.MainUI:
                    main.handle_event(event)
                elif gamestate.GameState == gamestate.GameUI:
                    game.handle_event(event)
        #绘制界面
        if gamestate.GameState == gamestate.MainUI:
            main.draw_self()
            game.resetOffest()
        elif gamestate.GameState == gamestate.GameUI:
            game.update()
            #game.drawSelf()

        text = "FPS : " + str(1000.0 / clock.tick(60))
        view = label.LabelViewState(label.ViewForver)
        fps_label = label.FontLabel(Rect(10, 600, 10, 10), view, "resource/msyh.ttf", 16, text)
        fps_label.draw_self()
        del fps_label

        #先绘制场景界面，再绘制鼠标，鼠标在最上层
        draw_mouse()

        #将Surface对象绘制在屏幕上
        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    hello_world()
    

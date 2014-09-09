#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys

#导入pygame模块，第8行的作用是简化你的输入，如不用在event前再加上pygame模块名
import pygame
from pygame.locals import *
import mypygame
import main_ui
import button
import gamestate
import game_ui
import resource
import label

pygame = mypygame.pygame
screen = mypygame.screen
clock = mypygame.clock

def drawMouse():
    pos = pygame.mouse.get_pos()
    screen.blit(resource.getImage("mouse"), (pos[0], pos[1]))

    #由于鼠标变化较频繁，所以更新鼠标位子后，刷新屏幕绘制内容
    #pygame.display.update()

def hello_world():
    resource.init()

    main = main_ui.UIMain()
    game = game_ui.UIGame()


    #循环，直到接收到窗口关闭事件
    while True:

         #处理事件
        for event in pygame.event.get():
            #接收到窗口关闭事件
            if event.type == QUIT:
                #退出
                pygame.quit()
                sys.exit()
            else:
                if gamestate.GameState == gamestate.MainUI:
                    main.handleEvent(event)
                elif gamestate.GameState == gamestate.GameUI:
                    game.handleEvent(event)

        #绘制界面
        if gamestate.GameState == gamestate.MainUI:
            main.drawSelf()
            game.resetOffest()
        elif gamestate.GameState == gamestate.GameUI:
            game.update()
            game.drawSelf()

        frame = clock.tick(60)
        #先绘制场景界面，再绘制鼠标，鼠标在最上层
        drawMouse()

        #将Surface对象绘制在屏幕上
        pygame.display.update()

if __name__ == "__main__":
    hello_world()
    

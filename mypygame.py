#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'


import pygame
try:
    import pygame.mixer as mixer
except ImportError:
    import android.mixer as mixer

#pygame 初始化
pygame.init()

ScreenSize = (800, 640)
clock = pygame.time.Clock()

#设置窗口模式及大小
screen = pygame.display.set_mode(ScreenSize)

#鼠标可用
pygame.mouse.set_visible(False)
mixer.set_num_channels(32)

#设置窗口标题
pygame.display.set_caption("放置传奇")

screenwidth = screen.get_width()
screenheight = screen.get_height()

running = True

explosions=0

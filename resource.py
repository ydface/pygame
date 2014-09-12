#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import pygame, sys, pygame.mixer
from pygame.locals import *
import mypygame
import button
import gamestate

pygame = mypygame.pygame
screen = mypygame.screen

game_sources = dict()
background = []

def getImage(key):
    global game_sources
    return game_sources[key]

def loadImage(path):
    try:
       image = pygame.image.load(path).convert_alpha()
    except pygame.error:
        print "can't load the image from", path
        raise SystemExit
    return image

def loadBtnImage():
    global game_sources
    image = loadImage("resource/item1.jpg")

    max_width = int(image.get_width() / 37.5)
    max_height = int(image.get_height() / 37.5)
    for i in range(max_width):
        for j in range(max_height):
            itemName = "item_" + str( max_width * i + (j + 1))
            game_sources[itemName] = image.subsurface((37.5 * i, 37.5 * j), (37.5, 37.5))

def loadMainUIImage():
    global game_sources
    image = loadImage("resource/mainUI.png")
    game_sources["player"] = image.subsurface((75, 100), (40, 60))

    image = loadImage("resource/2.png")
    game_sources["mouse"] = image.subsurface((528, 32), (38, 38))

    image = loadImage(("resource/2.jpg"))
    game_sources["play_btn"] = image.subsurface((20, 160), (130, 200))

def loadBattleMapImage():
    global game_sources
    image1 = loadImage("resource/worldmapUI/map_background1.pvr.ccz.png")
    image2 = loadImage("resource/worldmapUI/worldmapui.pvr.ccz.png")

    game_sources["big_map"] = image1.subsurface((0, 0), (850, 570))
    game_sources["map_key"] = image1.subsurface((890, 2), (40, 620))

    game_sources["level_1_0"] = image1.subsurface((0, 575), (185, 100))
    game_sources["level_1_1"] = image1.subsurface((185, 575), (185, 100))
    game_sources["level_1_1"] = image1.subsurface((185, 575), (185, 100))
    game_sources["level_1_1"] = image1.subsurface((185, 575), (185, 100))

    game_sources["level_2_0"] = image2.subsurface((2, 180), (240, 150))
    game_sources["level_2_1"] = image2.subsurface((245, 180), (240, 150))

    game_sources["level_3_1"] = image2.subsurface((240, 475), (185, 150))
    game_sources["level_3_0"] = image2.subsurface((556, 537), (185, 150))

def loadHeaderImage():
    global game_sources
    image = loadImage("resource/header1.png")

    hImage = image.subsurface((365, 95), (175, 63))
    hImage = pygame.transform.scale(hImage, (hImage.get_width(), hImage.get_height()))
    game_sources["header_line"] = hImage

    game_sources["attribute"] = loadImage("resource/attributeUI.jpg")

def init():
    global background
    loadMainUIImage()
    loadBtnImage()
    loadBattleMapImage()
    loadHeaderImage()
    game_sources["start_normal"] = loadImage("resource/start_normal.jpg")
    game_sources["start_down"] = loadImage("resource/start_down.jpg")

    background.append(pygame.transform.scale(pygame.image.load("resource/background.jpg").convert_alpha(), screen.get_size()))
    background.append(pygame.transform.scale(pygame.image.load("resource/level_1_background.jpg").convert_alpha(), screen.get_size()))
    background.append(pygame.transform.scale(pygame.image.load("resource/level_2_background.jpg").convert_alpha(), screen.get_size()))
    background.append(pygame.transform.scale(pygame.image.load("resource/level_3_background.jpg").convert_alpha(), screen.get_size()))
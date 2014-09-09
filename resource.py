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

def loadBattleMapImage():
    global game_sources
    image = loadImage("resource/worldmapUI/map_background1.pvr.ccz.png")

    game_sources["big_map"] = image.subsurface((0, 0), (850, 570))
    game_sources["map_key"] = image.subsurface((890, 2), (40, 620))

    game_sources["level_1_0"] = image.subsurface((0, 575), (185, 100))
    game_sources["level_1_1"] = image.subsurface((185, 575), (185, 100))


def loadHeaderImage():
    global game_sources
    image = loadImage("resource/header.png")

    hImage = image.subsurface((0, 0), (450, 160))
    hImage = pygame.transform.scale(hImage, (hImage.get_width() / 2, hImage.get_height() / 2))
    game_sources["header_line"] = hImage

def init():
    loadMainUIImage()
    loadBtnImage()
    loadBattleMapImage()
    loadHeaderImage()
    game_sources["start_normal"] = loadImage("resource/start_normal.jpg")
    game_sources["start_down"] = loadImage("resource/start_down.jpg")
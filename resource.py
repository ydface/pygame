#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import pygame
import sys
import pygame.mixer
from pygame.locals import *
import mypygame
import button
import gamestate
import label
from util.color import *
import cPickle
import traceback

screen = mypygame.screen

game_sources = dict()
background = []


def getImage(key):
    global game_sources
    return game_sources[key]


def getUIImage(key, wr, hr, text=u'界面', size=16):
    global game_sources
    if game_sources.has_key(key):
        return game_sources[key]
    else:
        image1 = getImage("ui1")
        image1 = pygame.transform.scale(image1, (int(image1.get_width() * wr), image1.get_height()))
        image2 = getImage("ui2")
        image2 = pygame.transform.scale(image2, (int(image2.get_width() * wr), int(image2.get_height() * hr)))

        w = image1.get_rect()[2]
        h1 = image1.get_rect()[3]
        h2 = image2.get_rect()[3]
        image = pygame.surface.Surface((w, h1 + h2), flags=SRCALPHA, depth=32)
        image.blit(image1, (0, 0))
        image.blit(image2, (0, h1))

        tlen = len(text) * size
        tlen = (w - tlen) / 2
        hlen = (h1 - size) // 2
        surface = label.FontLabel.D_Font[size].render(text, True, COLOR_WHITE)
        image.blit(surface, (tlen, hlen))
        game_sources[key] = image
        return image

def loadImage(path):
    try:
       image = pygame.image.load(path).convert_alpha()
    except:
        file = open("log.txt", "a")
        traceback.print_exc(file=file)
        file.write("\n")
        file.flush()
        file.close()
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

    image = loadImage("resource/skills.png")
    max_width = int(image.get_width() / 75)
    max_height = int(image.get_height() / 75)
    for i in range(0,5):
        for j in range(0, 7):
            itemName = "skill_" + str(max_width * i + (j + 1))
            himage = image.subsurface((64 * i, 64 * j), (64, 64))
            himage = pygame.transform.scale(himage, (32, 32))
            game_sources[itemName] = himage

def loadMainUIImage():
    global game_sources
    #image = loadImage("resource/test.png")
    #game_sources["player_btn"] = image.subsurface((0, 0), (39, 59))
    #game_sources["bag_btn"] = image.subsurface((39, 0), (40, 60))

    #image = loadImage("resource/2.png")
    #game_sources["mouse"] = image.subsurface((528, 32), (38, 38))


    #game_sources["ui_label"] = image.subsurface((26, 285), (646, 37))
    #game_sources["ui_main"] = image.subsurface((26, 322), (646, 133))
    #image = loadImage(("resource/2.jpg"))
    #game_sources["play_btn"] = image.subsurface((20, 160), (130, 200))

    #image = loadImage("resource/bag.png")
    #game_sources["bag_background"] = image.subsurface((6, 455), (412, 135))


def loadBattleMapImage():
    global game_sources
    image1 = loadImage("resource/mb1.png")
    image2 = loadImage("resource/mb2.png")

    game_sources["big_map"] = image1.subsurface((0, 0), (850, 570))
    game_sources["map_key"] = image1.subsurface((890, 2), (40, 620))

    game_sources["level_1_0"] = image1.subsurface((185, 575), (185, 100))
    game_sources["level_1_1"] = image1.subsurface((0, 575), (185, 100))

    game_sources["level_2_0"] = image2.subsurface((245, 180), (240, 150))
    game_sources["level_2_1"] = image2.subsurface((2, 180), (240, 150))

    game_sources["level_3_0"] = image2.subsurface((240, 475), (185, 150))
    game_sources["level_3_1"] = image2.subsurface((556, 537), (185, 150))


def loadHeaderImage():
    global game_sources
    #image = loadImage("resource/header1.png")

    #hImage = image.subsurface((365, 95), (175, 63))
    #hImage = pygame.transform.scale(hImage, (hImage.get_width(), hImage.get_height()))
    #game_sources["header_line"] = hImage

    #game_sources["attribute"] = loadImage("resource/attributeUI.jpg")


def load_ini(path):
    global game_sources
    file = open("resource/" + path + ".ini")
    cp = cPickle.load(file)
    file.close()
    image = loadImage("resource/" + path + ".png")

    for f in cp:
        key = f["key"]
        pos = (max([f["x"], 0]), f["y"])
        wh = (f["w"], f["h"])
        t_image = image.subsurface(pos, wh)
        #t_image = pygame.transform.scale(t_image, (32, 32))
        game_sources[key] = t_image
        #print game_sources.has_key("btn2")

def init():
    global background
    loadMainUIImage()
    loadBtnImage()
    loadBattleMapImage()
    loadHeaderImage()
    game_sources["start_normal"] = loadImage("resource/start_normal.jpg")
    game_sources["start_down"] = loadImage("resource/start_down.jpg")

    p_image = loadImage("resource/role1.png")
    p_image = pygame.transform.scale(p_image, (int(p_image.get_width() * 1.8), int(p_image.get_height() * 1.8)))
    game_sources["player"] = p_image

    background.append(pygame.transform.scale(pygame.image.load("resource/background.jpg").convert_alpha(), screen.get_size()))
    background.append(pygame.transform.scale(pygame.image.load("resource/level_1_background.jpg").convert_alpha(), screen.get_size()))
    background.append(pygame.transform.scale(pygame.image.load("resource/level_2_background.jpg").convert_alpha(), screen.get_size()))
    background.append(pygame.transform.scale(pygame.image.load("resource/level_3_background.jpg").convert_alpha(), screen.get_size()))

    load_ini("ui")
    load_ini("good")

init()
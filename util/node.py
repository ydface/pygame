#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import gamestate

class Node(object):
    def __init__(self):

        self.layer_child = dict()

        #初始化 三层UI
        ui_dict = dict()
        self.layer_child[gamestate.LayerUI] = ui_dict

        button_dict = dict()
        self.layer_child[gamestate.LayerButton] = button_dict

        label_dict = dict()
        self.layer_child[gamestate.LayerLabel] = label_dict

    def handle_event(self, event):
        for dc in self.layer_child:
            for c in self.layer_child[dc]:
                self.layer_child[dc][c].handle_event(event)

    def draw_self(self):
        for dc in self.layer_child:
            for c in self.layer_child[dc]:
                self.layer_child[dc][c].draw_self()

    def update(self):
        pass
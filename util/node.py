#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import gamestate

class Node(object):
    def __init__(self, zorder = 1):

        self.layer_child = dict()

        #初始化 三层UI
        ui_dict = dict()
        self.layer_child[gamestate.LayerUI] = ui_dict

        button_dict = dict()
        self.layer_child[gamestate.LayerButton] = button_dict

        label_dict = dict()
        self.layer_child[gamestate.LayerLabel] = label_dict

        self.event_enable = True

        self.zorder = zorder

    def __lt__(self, other):
        if self.zorder < other.zorder:
            return True
        return False

    def handle_event(self, event):
        if self.event_enable:
            for dc in self.layer_child.keys():
                for c in self.layer_child[dc].keys():
                    self.layer_child[dc][c].handle_event(event)

    def draw_self(self):
        #每次重新排序后绘制
        for dc in self.layer_child:
            result = sorted(self.layer_child[dc].items(), key=lambda d: d[1])
            for s in result:
                s[1].draw_self()

    def update(self):
        for dc in self.layer_child.keys():
            for c in self.layer_child[dc].keys():
                self.layer_child[dc][c].update()
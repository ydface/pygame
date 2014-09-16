#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import pygame
import pygame.mixer
from pygame.locals import *

class Node(object):
    def __init__(self, **kwargs):
        super(Node, self).__init__()

        self.father = None
        self._zorder = kwargs.get('layer', 1)
        self._old_zorder = self._zorder

        self.child = []

        self.event_enable = True

    def __lt__(self, other):
        if self._zorder < other._zorder:
            return True
        return False

    def add(self, sprite):
        sprite.father = self
        self.child.append(sprite)
        #self.child = sorted(self.child)

    def has_child(self, sprite):
        if sprite in self.child:
            return True
        return False

    def remove(self, sprite):
        self.child.remove(sprite)

    def event(self, event):
        if self.event_enable:
            self.child = sorted(self.child)
            for child in self.child:
                child.event(event)

    def draw(self):
        self.child.sort(reverse=True)
        for child in self.child:
            child.draw()

    def update(self, **kwargs):
        for child in self.child:
            child.update(**kwargs)

    def top_layer(self):
        self._zorder = 0

    def back_layer(self):
        self._zorder = self._old_zorder
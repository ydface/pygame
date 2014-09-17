#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

from pygame import *

Event_Type_Child = 1
Event_Type_Self = 2
Event_Type_All = 3


class Node(object):
    def __init__(self, **kwargs):
        super(Node, self).__init__()

        self.father = kwargs.get('father', None)
        self._zorder = kwargs.get('layer', 1)

        self.child = []

        self.event_type = kwargs.get('event', Event_Type_Self)

        self.event_enable = True

    def __lt__(self, other):
        if self._zorder < other._zorder:
            return True
        return False

    def add(self, sprite):
        sprite.father = self
        self.child.append(sprite)
        sprite.top()

    def has_child(self, sprite):
        if sprite in self.child:
            return True
        return False

    def remove(self, sprite):
        self.child.remove(sprite)

    def event(self, event):
        event_end = False
        if self.event_enable:
            clen = len(self.child) - 1
            if self.event_type == Event_Type_Self:
                if self.self_event(event):
                    return True
                while clen >= 0:
                    self.child[clen].event(event)
                    clen -= 1
            elif self.event_type == Event_Type_Child:
                while clen >= 0:
                    event_end = self.child[clen].event(event)
                    if not event_end:
                        clen -= 1
                        continue
                    else:
                        return event_end
                self.self_event(event)
            elif self.event_type == Event_Type_All:
                self.self_event(event)
                while clen >= 0:
                    self.child[clen].event(event)
                return False

    def draw(self):
        for child in self.child:
            child.draw()

    def update(self, **kwargs):
        for child in self.child:
            child.update(**kwargs)

    def has_child(self, ctype):
        for child in self.child:
            if isinstance(child, ctype):
                return child
        return None

    def self_event(self, event):
        pass

    def top(self):
        self._zorder = 99
        count = 2
        for child in self.father.child:
            if child != self:
                child._zorder = count
                count += 1
        self.father.child.sort()
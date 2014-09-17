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

    #插入子节点到所有子节点的最上层
    def add(self, sprite):
        sprite.father = self
        self.child.append(sprite)
        sprite.top()

    #是否有某个具体子节点
    def has_child(self, sprite):
        if sprite in self.child:
            return True
        return False

    #是否有某Class的实例子节点，返回该子节点
    def has_ctype_child(self, ctype):
        for child in self.child:
            if isinstance(child, ctype):
                return child
        return None

    #移除子节点
    def remove(self, sprite):
        self.child.remove(sprite)

    #删除由某class实例的子节点 all_remove表示是否全部删除
    def remove_ctype_child(self, ctype, all_remove=False):
        if all_remove:
            self.child = [child for child in self.child if not isinstance(child, ctype)]
        else:
            child = self.has_ctype_child(ctype)
            if child:
                self.remove(child)

    #事件处理
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

    #绘制
    def draw(self):
        for child in self.child:
            child.draw()

    #update
    def update(self, **kwargs):
        for child in self.child:
            child.update(**kwargs)

    #自身事件处理
    def self_event(self, event):
        pass

    #自身置为最上层
    def top(self):
        self._zorder = 99
        count = 2
        for child in self.father.child:
            if child != self:
                child._zorder = count
                count += 1
        self.father.child.sort()
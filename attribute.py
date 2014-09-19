#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

from util.macro import *


class Attribute(object):
    def __init__(self):
        super(Attribute, self).__init__()
        self.level = 1
        self.attribute = [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def attribute_value(self, attribute):
        return int(self.attribute[attribute])

    def attribute_value_str(self, attribute):
        return Attribute_Name[attribute] + ":   " + str(int(self.attribute_value(attribute)))

    def attribute_inc(self, attribute, val):
        self.attribute[attribute] += val
        return self.attribute_value(attribute)

    def hp_inc(self, val):
        self.attribute[Attribute_Hp] += val
        self.attribute[Attribute_Hp] = min([self.attribute_value(Attribute_Hp), self.attribute_value(Attribute_Max_Hp)])
        return self.attribute_value(Attribute_Hp) == self.attribute_value(Attribute_Max_Hp)

    def hp_dec(self, val):
        self.attribute[Attribute_Hp] -= val
        self.attribute[Attribute_Hp] = max([self.attribute_value(Attribute_Hp), 0])
        return self.attribute_value(Attribute_Hp) == 0
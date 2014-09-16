#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'


Attribute_Hp = 0
Attribute_Max_Hp = 1
Attribute_Attack = 2
Attribute_Defense = 3
Attribute_Speed1 = 4
Attribute_Speed2 = 5
Attribute_Hit = 6
Attribute_Dodge = 7
Attribute_Crit = 8
Attribute_Crit_Seal = 9
Attribute_Wreck = 10
Attribute_Parry = 11
Attribute_None = 12

class Attribute(object):
    def __init__(self):
        super(Attribute, self).__init__()
        self.level = 1
        self.attribute = [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def attribute_value(self, attribute):
        if attribute in [Attribute_Hp, Attribute_Max_Hp]:
            return int(self.attribute[attribute])
        return self.attribute[attribute]

    def attribute_value_str(self, attribute):
        return str(self.attribute_value(attribute))

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
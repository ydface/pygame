#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'


Attribute_Hp = 0
Attribute_Max_Hp = Attribute_Hp + 1
Attribute_Attack = Attribute_Max_Hp + 1
Attribute_Defense = Attribute_Attack + 1
Attribute_Speed1 = Attribute_Defense + 1
Attribute_Speed2 = Attribute_Speed1 + 1
Attribute_Hit = Attribute_Speed2 + 1
Attribute_Dodge = Attribute_Hit + 1
Attribute_Crit = Attribute_Dodge + 1
Attribute_Crit_Seal = Attribute_Crit + 1
Attribute_Wreck = Attribute_Crit_Seal + 1
Attribute_Parry = Attribute_Wreck + 1
Attribute_None = Attribute_Parry + 1

Attribute_Name = [u"血量", u"最大血量", u"攻击", u"防御", u"冷却加速", u"施法加速", u"命中", u"闪避", u"暴击",
                  u"抗暴", u"破击", u"格挡"]


class Attribute(object):
    def __init__(self):
        super(Attribute, self).__init__()
        self.level = 1
        self.attribute = [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def attribute_value(self, attribute):
        return self.attribute[attribute]

    def attribute_value_str(self, attribute):
        return Attribute_Name[attribute] + ": " + str(int(self.attribute_value(attribute)))

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
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

Attribute_Name = [u"血       量", u"最大血量", u"攻       击", u"防       御", u"冷却加速", u"施法加速", u"命      中",
                  u"闪      避", u"暴      击", u"抗      暴", u"破      击", u"格      挡"]


Quality_White = 0
Quality_Green = Quality_White + 1
Quality_Blue = Quality_Green + 1
Quality_Purple = Quality_Blue + 1
Quality_Red = Quality_Purple + 1
Quality_Gold = Quality_Red + 1

Equip_Hat = 0
Equip_Necklace = Equip_Hat + 1
Equip_Clothes = Equip_Necklace + 1
Equip_Left_Weapon = Equip_Clothes + 1
Equip_Right_Weapon = Equip_Left_Weapon + 1
Equip_Left_Ring = Equip_Right_Weapon + 1
Equip_Right_Ring = Equip_Left_Ring + 1
Equip_Belt = Equip_Right_Ring + 1
Equip_Gaiter = Equip_Belt + 1
Equip_Shoes = Equip_Gaiter + 1
Equip_Talisman = Equip_Shoes + 1

Equip_Name = [u"头盔", u"项链", u"护甲", u"主手", u"副手", u"左手戒指", u"右手戒指", u"腰带", u"护腿", u"鞋子", u"护符"]
QName = [u"粗糙", u"精致", u"无暇", u"完美", u"神器", u"传奇"]

BTY_YUNXUAN = 1
BTY_SHANGHAI_INC = 2
BTY_SHANGHAI_DEC = 3
BTY_BAOJI_SEAL = 4
BTY_BAOJI_INC = 5
BTY_DOT = 6
BTY_HOT = 7
BTY_MINGZHONG_DEC = 8
BTY_ZUZHOU = 9
BTY_ABSORB_BLOOD = 10

RNAME = {
    Equip_Clothes: "clothes",
    Equip_Left_Weapon: "weapon",
    Equip_Hat: "hat"
}
#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import gamestate
import cPickle

save_obj = None


class Save(object):
    def __init__(self):
        super(Save, self).__init__()

    @staticmethod
    def save():
        sav_obj = dict()
        sav_obj["user"] = dict()
        sav_obj["bag"] = dict()
        sav_obj["skill"] = []

        player = gamestate.player

        sav_obj["user"] = player.user_serialize_save()
        sav_obj["skill"] = player.skill_serialize_save()

        cPickle.dump(sav_obj, open("save.sav", "wb"), 1)

    @staticmethod
    def init_save():
        global save_obj
        save_obj = dict()
        save_obj["user"] = dict()
        save_obj["bag"] = dict()
        save_obj["skill"] = []

        user_obj = save_obj["user"]
        user_obj["level"] = 1
        user_obj["exp"] = 1

        skill_obj = save_obj["skill"]
        skill_obj.append({"skill_id": 1, "level": 1})
        skill_obj.append({"skill_id": 2, "level": 1})

    @staticmethod
    def load(module):
        global save_obj
        if not save_obj:
            try:
                save_obj = cPickle.load(open("save.sav"))
            except IOError, e:
                Save.init_save()
        return save_obj[module]


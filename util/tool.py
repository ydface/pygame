#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import random


class RandSeed(object):
    def __init__(self, key, val):
        super(RandSeed, self).__init__()

        self.key = key
        self.val = val


class RandUtil(object):

    @staticmethod
    def random(para):
        for i in range(len(para)):
            if i > 0:
                para[i].key += para[i - 1].key

        ra = random.randint(0, para[len(para) - 1].key)

        for i in range(len(para)):
            if i == 0:
                if ra <= para[i].key:
                    return para[i].val
                else:
                    continue
            else:
                if para[i-1].key < ra and para[i].key >= ra:
                    print para[i-1].key, ra, para[i].key
                    return para[i].val
                else:
                    continue
            return None


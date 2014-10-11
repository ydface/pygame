#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import json
import os
import socket
import sys

PORT = "6888"
HOST = "localhost"


class Session(object):
    def __init__(self, address=None):
        if address is None:
            address = "127.0.0.1", "6888"
        try:
            self.conn = socket.create_connection(address)
            self.client = self.conn.makefile()
        except:
            self.conn = None

    def _rpc(self, method, result, *args):
        if not self.conn:
            return None

        data = {'method': method,
                'params': args}
        request = json.dumps(data)
        self.client.write(request + '\n')
        self.client.flush()
        if result:
            response = self.client.readline()
            response = json.loads(response)
            if response['error'] is not None:
                print(response['error'])
                return None
            return response["result"]
        return None

    def __getattr__(self, name):
        def rpc_call(result, *args):
            return self._rpc(name, result,*args)
        return rpc_call


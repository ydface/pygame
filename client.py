#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import sys
from twisted.internet.protocol import ClientFactory
from twisted.internet.protocol import Protocol
from twisted.protocols.basic import protocol
from twisted.python import log
from twisted.internet import reactor
from twisted.internet.protocol import ReconnectingClientFactory
import main

connection = None


class SyncDataProtocol(Protocol):
    def dataReceived(self, data):
        log.msg("Receiver respond msg: %s" % data)

    def write(self, data):
        self.transport.write(data + "\n")


class Client(ReconnectingClientFactory):
    #protocol = Protocol()

    def startedConnecting(self, connector):
        log.msg("Start connect %s" % connector.host)

    def buildProtocol(self, addr):
        self.resetDelay()

        global connection
        if connection:
            del connection
        connection = SyncDataProtocol()
        return connection

    def clientConnectionLost(self, connector, reason):
        ReconnectingClientFactory.clientConnectionLost(self, connector, reason)

    def clientConnectionFailed(self, connector, reason):
        ReconnectingClientFactory.clientConnectionFailed(self, connector, reason)


def run():
    if main.update():
        reactor.callLater(0.016, run)
    else:
        reactor.stop()


def start():
    log.startLogging(sys.stdout)

    reactor.connectTCP("127.0.0.1", 6888, Client())
    reactor.callFromThread(run)
    reactor.run()
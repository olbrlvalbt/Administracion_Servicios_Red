from Procesamiento import Ejecutar
import os, time
import threading
from pysnmp.hlapi import *
from getSNMP import consultaSNMP

class Monitor(threading.Thread):
    def __init__(self, agent):
        super(Monitor, self).__init__()
        self.agent = agent
        self.stopRequest = threading.Event()

    def run(self):
        while not self.stopRequest.isSet():
	   	   Ejecutar( self.agent['comunity'] , self.agent['hostname'] , self.agent['port'] , self.agent['idAgent'] , self.agent['time'] )        

    def join(self, timeout = None):
        self.stopRequest.set()
        #super(Monitor, self).join(timeout)

    def getAgentInfo(self, oid):
        return consultaSNMP(self.agent['comunity'], self.agent['hostname'], self.agent['port'], oid)

from Procesamiento import Ejecutar
from LineaBase import EjecutarLb
import os, time
import threading
from pysnmp.hlapi import *
from getSNMP import consultaSNMP

class Monitor(threading.Thread):
    def __init__(self, agent):
        super(Monitor, self).__init__()
        self.agent = agent
        self.ramRsg = (agent['ramReady'], agent['ramSet'], agent['ramGo'])
        self.cpuRsg = (agent['cpuReady'], agent['cpuSet'], agent['cpuGo'])
        self.hddRsg = (agent['hddReady'], agent['hddSet'], agent['hddGo'])
        self.ramOverflow = False
        self.cpuOverflow = []
        self.hddOverflow = False
        self.stopRequest = threading.Event()

    def run(self):
        while not self.stopRequest.isSet():
            try:
                Ejecutar( self.agent['comunity'] , self.agent['hostname'] , self.agent['port'] , self.agent['idAgent'] , self.agent['time'] )    
                EjecutarLb( self , self.agent['comunity'] , self.agent['hostname'] , self.agent['port'] , self.agent['idAgent'] , self.agent['time'] )   
            except Exception as e:
                print(e.message)
                time.sleep(10)
                continue

    def join(self, timeout = None):
        self.stopRequest.set()
        #super(Monitor, self).join(timeout)

    def getAgentInfo(self, oid):
        return consultaSNMP(self.agent['comunity'], self.agent['hostname'], self.agent['port'], oid)

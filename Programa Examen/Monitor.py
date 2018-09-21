import os, time
import threading
from pysnmp.hlapi import *

class Monitor(threading.Thread):
    def __init__(self, idAgent, agent):
        super(Monitor, self).__init__()
        self.idAgent = idAgent
        self.agent = agent
        self.stopRequest = threading.Event()

    def run(self):
        while not self.stopRequest.isSet():
		var = 1
            	#self.getAgentInfo()

    def join(self, timeout = None):
        self.stopRequest.set()
        super(Monitor, self).join(timeout)

    def getIdAgent(self):
        return self.idAgent

    def getAgentInfo(self):
        errorIndication, errorStatus, errorIndex, varBinds = next(
            getCmd(SnmpEngine(),
                   CommunityData(self.agent['comunity'], mpModel=0),
                   UdpTransportTarget((self.agent['hostname'], self.agent['port'])),
                   ContextData(),
                   ObjectType(ObjectIdentity('1.3.6.1.2.1.1.3.0')))
        )

        if errorIndication:
            print(errorIndication)
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        else:
            for varBind in varBinds:
                print(' = '.join([x.prettyPrint() for x in varBind]))

        time.sleep(2)

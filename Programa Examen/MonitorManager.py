import json
import threading, time
import os.path
from pysnmp.hlapi import *
from Monitor import Monitor

class MonitorManager():
	def __init__(self):
		self.data = {}
		self.data['agents'] = [] 
		self.pool = list()

		if os.path.exists('agents.json'):
			with open('agents.json', 'r') as f:
				self.data = json.load(f)
				pool = [Monitor(idAgent = agent['idAgent'], agent = agent) for agent in self.data['agents']]
			for t in pool:
				t.start()

	def addAgent(self, idAgent, hostname, version, port, comunity):
		for agent in self.data['agents']:
			if agent['idAgent'] == idAgent:
				return False

		newAgent = {  
		    'idAgent': idAgent,
		    'hostname': hostname,
		    'version': version,
		    'port': port,
		    'comunity': comunity
		}

		t = Monitor(idAgent = idAgent, agent = newAgent)
		self.pool.append(t)
		t.start()

		self.data['agents'].append(newAgent)
		with open('agents.json', 'w') as f:  
		    json.dump(self.data, f)

		return True
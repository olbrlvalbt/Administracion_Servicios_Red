import json
import threading, time
import os.path
from Procesamiento import crearBases
from pysnmp.hlapi import *
from Monitor import Monitor

class MonitorManager():
	def __init__(self):
		self.data = {}
		self.data['agents'] = [] 
		self.pool = {}

		if os.path.exists('agents.json'):
			with open('agents.json', 'r') as f:
				self.data = json.load(f)
			for agent in self.data['agents']:
				t = Monitor(agent)
				self.pool.update({agent['idAgent']: t})
				t.start()

	def addAgent(self, idAgent, hostname, version, port, comunity):
		if idAgent in self.pool:
			return False

		tiempo_actual = int(time.time())		

		newAgent = {  
		    'idAgent': idAgent,
		    'hostname': hostname,
		    'version': version,
		    'port': port,
		    'comunity': comunity,
		    'time': tiempo_actual	
		}

		t = Monitor(newAgent)
		self.pool.update({idAgent: t})
		t.start()

		self.data['agents'].append(newAgent)
		with open('agents.json', 'w') as f:
		    json.dump(self.data, f)

		crearBases( idAgent )		

		return True

	def removeAgent(self, idAgent):
		if not idAgent in self.pool:
			return False
		else:
			self.pool[idAgent].join()
			a = self.pool.pop(idAgent)
			self.data['agents'].remove(a.agent)

			with open('agents.json', 'w') as f:
			    json.dump(self.data, f)
			return True

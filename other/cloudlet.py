from constants import *

class Cloudlet:
	def __init__(self,name,number_of_user,capacity,x,y,cloud,max_utilization):
		self.number_of_user = number_of_user
		self.capacity = capacity
		self.x = x
		self.y = y
		self.name = name
		self.client_connected_to_ap = []
		self.client_connected_to_server = []
		self.server_state = State.DOWN
		self.total_client_workload = 0
		self.total_energy = 0
		self.total_latency = 0
		self.total_response_time = 0
		self.total_rtt = 0
		self.cloud = cloud
		self.max_utilization = max_utilization
		
	def setUsers(self,users):
		self.number_of_user = users
	def getUsers(self):
		return self.number_of_user
	def getServerState(self):
		return self.server_state
	def setServerState(self,state):
		self.server_state = state
	def getCapacity(self):
		return self.capacity
	def setCapacity(self,capacity):
		self.capacity = capacity
	def setXY(self,x,y):
		self.x = x
		self.y = y
	def getX(self):
		return self.x
	def getY(self):
		return self.y
	def getName(self):
		return self.name
	def addClientToAccessPoint(self,client):
		self.client_connected_to_ap.append(client)
	def getUtilization(self):
		return int(float(self.total_client_workload*100)/self.capacity)
	def getUtilizationWithClient(self,client):
		#this method return the utilization if this cloudlet accept the given client
		workload = client.getWorkload()
		return int(float((self.total_client_workload+workload)*100)/self.capacity)
	def getNumberClientToAccessPoint(self):
		return len(self.client_connected_to_ap)
	def getNumberClientToServer(self):
		return len(self.client_connected_to_server)
	def startServer(self):
		self.setServerState(State.UP)
		self.cloud.addServer(self)
	def canServerAcceptClient(self,client):
		return client.getWorkload()+self.total_client_workload <= (self.capacity*self.max_utilization)/100
	def addClient(self,client):
		self.client_connected_to_server.append(client)
		self.total_client_workload += client.getWorkload()
		self.total_energy = self.getPowerConsumption(self.getUtilization())
		if self.getUtilization() > self.max_utilization:
			self.max_utilization = self.getUtilization()
	def getEnergy(self):
		return self.total_energy
	def addClientLatency(self,latency):
		self.total_latency +=latency
	def addClientResponseTime(self,reponse_time):
		self.total_response_time +=reponse_time
	def addClientRTT(self,rtt):
		self.total_rtt += rtt
	def getLatency(self):
		return self.total_latency
	def getPowerConsumption(self,utilization):
		if utilization >= 0 and utilization <=1:
			return 86
		if utilization >1 and utilization <10:
			return 89.4
		elif utilization>=10 and utilization <20:
			return 92.6
		elif utilization>=20 and utilization < 30:
			return 96
		elif utilization>=30 and utilization <40:
			return 99.5
		elif utilization>=40 and utilization<50:
			return 102
		elif utilization>=50 and utilization<60:
			return 106
		elif utilization>=60 and utilization<70:
			return 108
		elif utilization>=70 and utilization<80:
			return 112
		elif utilization>=80 and utilization<90:
			return 114
		else:
			return 117

	def getReport(self):
		report = {}
		report['utilization'] = self.max_utilization
		if len(self.client_connected_to_server)==0:
			report['total_client'] = 0
			report['energy'] = 86
			report['latency'] = 0
			report['response_time'] = 0
			report['rtt'] = 0
			return report
		report['total_client'] = len(self.client_connected_to_server)
		report['energy'] = self.total_energy
		report['latency'] = round(float(self.total_latency)/len(self.client_connected_to_server),2)
		report['response_time'] = round(float(self.total_response_time)/len(self.client_connected_to_server),2)
		report['rtt'] = round(float(self.total_rtt)/len(self.client_connected_to_server),2)
		
		return report

	def __str__(self):
		state = ""
		if self.server_state == State.DOWN:
			state = "OFF"
		else:
			state = "ON"
		return "Cloudlet {}, AP client->{}, Server State->{}, Server client->{}, utilization->{} %".format(self.name,self.getNumberClientToAccessPoint(),state, self.getNumberClientToServer(),self.getUtilization())


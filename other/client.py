from constants import *
import math

class Client:
	def __init__(self,name,workload,cloud):
		self.name = name
		self.workload = workload
		self.access_point = None
		self.server = None
		self.cloud = cloud

	def getName(self):
		return self.name
	def getWorkload(self):
		return self.workload
	def setAccessPoint(self,access_point):
		self.access_point = access_point
	def getAccessPoint(self):
		return self.access_point
	def setServer(self,server):
		self.server = server
	def connect(self,server):
		self.server = server 
		server.addClient(self)

		#computing latency
		distance = self.cloud.distanceBetweenNode(self.access_point,server)
		routing_switching = 0
		routing_switching = (distance+1)*self.cloud.getSwitchingLatency()
		latency = self.cloud.getTimeUserAP()+(self.cloud.getTimeNodes()*distance)+routing_switching 
		server.addClientLatency(latency)
		#response time
		response_time = latency + self.cloud.getTimeProcessing()
		server.addClientResponseTime(response_time)
		#round trip time
		rount_trip_time = latency*2 + self.cloud.getTimeProcessing()
		server.addClientRTT(rount_trip_time)


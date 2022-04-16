from constants import *
import math
import random
import numpy as np
from cloudlet import *
from client import *
import networkx as nx
import matplotlib.pyplot as plt


class Cloud:
	def __init__(self,number_of_user,number_of_cloudlet,open_algorithm,level_workload,per,cloudlet_capacity,opening_strategy,server_critiria_selection,time_node,time_user_ap,routing_switching,time_processing,graph_type,upper_util,lower_util,quotas,cloudlet_to_open,max_utilization):
		self.number_of_user = number_of_user
		self.real_number_of_user = 0
		self.number_of_cloudlet = number_of_cloudlet
		self.level_workload = level_workload
		self.cloudlet_capacity = cloudlet_capacity
		self.client_served_by_remote_cloud = 0

		self.workload_min = 0
		self.workload_max = 0
		if(level_workload==Workload.LOW):
			self.workload_min = 0
			self.workload_max = 150
		elif(level_workload==Workload.MEDIUM):
			self.workload_min = 150
			self.workload_max = 350
		else:
			self.workload_min = 350
			self.workload_max = 500

		self.upper_util = upper_util
		self.lower_util = lower_util

		self.per = per
		self.list_cloudlets = []
		self.list_clients = []
		self.list_cloudlets_openned = []
		self.total_capacity = 0
		self.total_capacity_available = 0
		self.total_workload = 0

		self.opening_strategy = opening_strategy
		self.server_critiria_selection = server_critiria_selection
		self.open_algorithm = open_algorithm

		self.time_node = time_node
		self.time_user_ap = time_user_ap
		self.routing_switching = routing_switching
		self.time_processing = time_processing

		self.graph = None
		self.graph_type = graph_type

		self.quotas = quotas
		self.cloudlet_to_open = cloudlet_to_open

		self.max_utilization = max_utilization

		self.createCloudlets()
		self.createUser()

	def createCloudlets(self):
		index = 1
		if self.graph_type == Topology.TWOD:
			N = int(math.sqrt(self.number_of_cloudlet))
			self.graph = nx.grid_2d_graph(N,N)
			nodes = list(self.graph.nodes())
			for i in range(len(nodes)):
				cloudlet = Cloudlet(str(index),0,self.cloudlet_capacity,nodes[i][0],nodes[i][1],self,self.max_utilization)
				self.list_cloudlets.append(cloudlet)
				self.total_capacity += self.cloudlet_capacity
				index +=1
		elif self.graph_type == Topology.BARABASI_ALBERT:
			self.graph = nx.barabasi_albert_graph(self.number_of_cloudlet,2)
			nodes = list(self.graph.nodes())
			for i in range(self.number_of_cloudlet):
				cloudlet = Cloudlet(nodes[i],0,self.cloudlet_capacity,0,0,self)
				self.list_cloudlets.append(cloudlet)
				self.total_capacity += self.cloudlet_capacity
				index +=1
			#print("Nodes-APs: ", nodes)
		elif self.graph_type == Topology.DOROGOVTSEV:
			self.graph = nx.dorogovtsev_goltsev_mendes_graph(self.number_of_cloudlet)
			nodes = list(self.graph.nodes())
			for i in range(self.number_of_cloudlet):
				cloudlet = Cloudlet(nodes[i],0,self.cloudlet_capacity,0,0,self)
				self.list_cloudlets.append(cloudlet)
				self.total_capacity += self.cloudlet_capacity
				index +=1
				#dorogovtsev_goltsev_mendes_graph
		else:
			pass

	def getTimeNodes(self):
		return self.time_node
	def getTimeUserAP(self):
		return self.time_user_ap
	def getTimeProcessing(self):
		return self.time_processing
	def getSwitchingLatency(self):
		return self.routing_switching

	def createUser(self):
		average_user = self.number_of_user/self.number_of_cloudlet
		sigma_user= int((float(self.per)/100)*(average_user))	#sigma value for users
		if sigma_user==0:
			sigma_user = 1
		#sigma_workload =sigma_user*10	#sigma value for workload
		#average_workload = average_user*self.level_workload
		#let's assign users to access point
		index_client = 1
		client_per_node = []
		for i in range(len(self.list_cloudlets)):
			quota = self.cloudletHasQuota(i)
			if quota == 0:
				users = abs(int(np.random.normal(average_user, sigma_user))) #users per node
			else:
				users = int(math.floor(self.number_of_user*quota/100))
			self.real_number_of_user += users
			#average_user = (self.number_of_user-self.real_number_of_user)/(self.number_of_cloudlet-i)
			#sigma_user= int((float(self.per)/100)*(average_user))
			cloudlet = self.list_cloudlets[i]
			cloudlet.setUsers(users)
			
			for j in range(users):
				workload = random.randint(self.workload_min,self.workload_max)
				#line = str(index_client)+','+str(workload)+'\n'
				#file = open('workload.csv','a')
				#file.write(line)
				client = Client(str(index_client),workload,self)
				self.list_clients.append(client)
				self.total_workload += workload
				cloudlet.addClientToAccessPoint(client)
				client.setAccessPoint(cloudlet)
				index_client +=1 

	def cloudletHasQuota(self,index):
		if len(self.quotas) == 0:
			return 0
		if len(self.quotas) <= index:
			return 0
		return self.quotas[index]


	def getProprietyAverage(self,list_dict,propriety):
		total_propriety_value = 0
		for dict in list_dict:
			total_propriety_value += dict[propriety]
		return round(total_propriety_value/float(len(list_dict)),2)


	def getTotalCapacity(self):
		return self.total_capacity
	def getAvalableCapacity(self):
		return self.total_capacity_available
	def getTotalWorkload(self):
		return self.total_workload
	def getUtilization(self):
		if self.total_capacity == 0:
			return 0
		else:
			return int(float(self.total_workload*100)/self.total_capacity_available)

	def start(self):
		if self.opening_strategy == OpenStrategy.OPEN_ALL:
			self.openAll()
		elif self.opening_strategy == OpenStrategy.SPECIFIC:
			self.openSpecific()
		else:
			self.openMin()

		self.total_workload = 0

		for client in self.list_clients:
			self.connect(client)
		#save report to csv file
		servers_reports = []
		number_of_cloudlet_opened = 0
		names_of_cloudlet_opened = ''
		for cloudlet in self.list_cloudlets:
			if cloudlet.getServerState()==State.UP:
				servers_reports.append(cloudlet.getReport())
				number_of_cloudlet_opened +=1
				if self.graph_type == Topology.BARABASI_ALBERT:
					names_of_cloudlet_opened += str(int(cloudlet.getName())+1)+"#"
				else:
					names_of_cloudlet_opened += str(cloudlet.getName())+"#"
		names_of_cloudlet_opened = names_of_cloudlet_opened[:-1] # just for removing the last dash :) 

		avg_total_client = self.getProprietyAverage(servers_reports,"total_client")
		avg_latency = self.getProprietyAverage(servers_reports,"latency")
		avg_reponse_time = self.getProprietyAverage(servers_reports,"response_time")
		avg_rtt = self.getProprietyAverage(servers_reports,"rtt")
		avg_utilization = self.getProprietyAverage(servers_reports,"utilization")
		avg_energy = self.getProprietyAverage(servers_reports,"energy")

		total_energy = 0
		total_latency = 0
		total_client_served = 0
		for report in servers_reports:
			total_energy += report['energy']
			total_latency += report['latency']
			total_client_served += report['total_client']

		total_latency = round(float(total_latency)/number_of_cloudlet_opened,2)

		avgs = str(avg_total_client)+","+str(avg_latency)+","+str(avg_reponse_time)+","+str(avg_rtt)+","+str(avg_utilization)+","+str(avg_energy)+"\n"

		critiria = None
		if self.server_critiria_selection ==BrokerPolicy.BEST_LATENCY:
			critiria = "LATENCY"
		elif self.server_critiria_selection ==BrokerPolicy.BEST_ALL:
			critiria ="ALL"
		elif self.server_critiria_selection==BrokerPolicy.BEST_UPPER_LOWER_UTIL:
			critiria = "UPPER_LOWER_UTIL"
		else:
			critiria ="UTILIZATION"

		algorithm = None 
		if self.open_algorithm == OpenAlgorithm.RANDOM:
			algorithm = "RANDOM"
		elif self.open_algorithm == OpenAlgorithm.MOST_USER_FIRST:
			algorithm = "MOST USER FIRST"
		else:
			algorithm = "BEST NEIGHBORS"

		strategy = None
		if self.opening_strategy==OpenStrategy.OPEN_ALL:
			strategy = "OPEN_ALL"
			algorithm = "DEFAULT_OA"
			critiria = "DEFAULT"
		elif self.opening_strategy ==OpenStrategy.SPECIFIC:
			strategy = "SPECIFIC"
			algorithm = "DEFAULT_ASPE"
			critiria = "DEFAULT_CSPE"
		else:
			strategy = "OPEN_MIN"

		graph = None
		if self.graph_type == Topology.TWOD:
			graph = "2D GRAPH"
		else:
			graph = "BARABASI ALBERT"

		workload_level = ""
		if self.level_workload == Workload.LOW:
			workload_level = "LOW"
		elif self.level_workload == Workload.MEDIUM:
			workload_level = "MEDIUM"
		else:
			workload_level = "HIGH"

		sequence = strategy+","+critiria+","+algorithm+","+graph+","+workload_level+","+str(self.number_of_user)+","+str(self.real_number_of_user)+","+str(total_client_served)+","+str(self.client_served_by_remote_cloud)+","+str(len(self.list_cloudlets))+","+str(number_of_cloudlet_opened)+","+names_of_cloudlet_opened+","+str(self.getUtilization())+","+str(self.total_workload)+","+str(total_energy)+","+str(total_latency)+","+avgs
		file = open("reports.csv","a")
		file.write(sequence)
		
	def displayGraph(self):
		#display the graph
		color_map = []
		for cloudlet in self.list_cloudlets:
			if cloudlet.getServerState()==State.UP:
				color_map.append("green")
			else:
				color_map.append("red")
		nx.draw_networkx(self.graph,node_color=color_map,with_labels=True)
		plt.axis('off')
		plt.show() 
		
	def openAll(self):
		for cloudlet in self.list_cloudlets:
			cloudlet.startServer()
	def openSpecific(self):
		for cloudlet in self.list_cloudlets:
			index = int(cloudlet.getName())
			if index in self.cloudlet_to_open:
				cloudlet.startServer()

	def openMin(self):
		cloudlet_capacity_limit = (self.cloudlet_capacity*self.max_utilization/100)
		number_of_cloudlet_needed = int(math.ceil(float(self.total_workload)/cloudlet_capacity_limit)) ##change
		if number_of_cloudlet_needed > len(self.list_cloudlets):
			number_of_cloudlet_needed = len(self.list_cloudlets)
		nbr_cloudlet_opened = 0
		if self.open_algorithm == OpenAlgorithm.RANDOM:
			while nbr_cloudlet_opened < number_of_cloudlet_needed:
				index = random.randint(0,len(self.list_cloudlets)-1)
				cloudlet = self.list_cloudlets[index]
				if cloudlet.getServerState()==State.DOWN:
					cloudlet.startServer()
					nbr_cloudlet_opened +=1

		elif self.open_algorithm == OpenAlgorithm.MOST_USER_FIRST:
			while nbr_cloudlet_opened < number_of_cloudlet_needed:
				best_server = None
				best_nbr_client = None 
				for cloudlet in self.list_cloudlets:
					if cloudlet.getServerState() == State.DOWN:
						nbr_client = cloudlet.getNumberClientToAccessPoint()
						if best_nbr_client==None or nbr_client > best_nbr_client:
							best_nbr_client = nbr_client
							best_server = cloudlet
				if best_server != None:
					best_server.startServer()
					nbr_cloudlet_opened +=1

		else: #best neighbors
			while nbr_cloudlet_opened < number_of_cloudlet_needed:
				best_server = None
				best_distance = None
				for cloudlet in self.list_cloudlets:
					if cloudlet.getServerState() == State.DOWN:
						distance = self.getClientDistanceFrom(cloudlet)
						if best_distance==None or distance < best_distance:
							best_distance = distance
							best_server = cloudlet 
				if best_server != None:
					best_server.startServer()
					nbr_cloudlet_opened +=1

	def addServer(self,cloudlet):
		self.list_cloudlets_openned.append(cloudlet)
		self.total_capacity_available += cloudlet.getCapacity()

	def connect(self,client):
		#choose the best server based on the current critiria
		if self.opening_strategy == OpenStrategy.OPEN_ALL:
			best_cloudlet = self.getBestLatencyServer(client)
			if best_cloudlet == None:
				#we coudn't find any available cloudlet
				#the user will be server by the cloud
				self.client_served_by_remote_cloud +=1
			else:
				client.connect(best_cloudlet)
				self.total_workload += client.getWorkload()
			return

		if self.server_critiria_selection == BrokerPolicy.BEST_LATENCY:
			best_server = self.getBestLatencyServer(client)
		elif self.server_critiria_selection == BrokerPolicy.BEST_UPPER_LOWER_UTIL:
			best_server = self.getBestServerUpperLower(client)
		else:
			best_server = self.getBestServerUtilization(client)
		
		if best_server != None:
			client.connect(best_server)
			self.total_workload +=client.getWorkload()
		else:
			#we coudn't find any available cloudlet
			#the user will be server by the cloud
			self.client_served_by_remote_cloud +=1

	def getBestLatencyServer(self,client):
		client_access_point = client.getAccessPoint()
		if client_access_point.getServerState() == State.UP:
			if client_access_point.canServerAcceptClient(client):
				return client_access_point
		#if he cannot connect to its own server
		best_distance = 100000
		best_server = None
		for cloudlet in self.list_cloudlets:
			if cloudlet.getServerState()==State.UP and cloudlet.canServerAcceptClient(client):
				distance = self.distanceBetweenNode(client_access_point,cloudlet)
				if distance < best_distance or best_server==None:
					best_distance = distance
					best_server = cloudlet
		return best_server
	def getBestServerUtilization(self,client):
		best_utilization = 100
		best_server = None
		for cloudlet in self.list_cloudlets:
			if cloudlet.getServerState()==State.UP and cloudlet.canServerAcceptClient(client):
				utilization = cloudlet.getUtilization()
				if best_server==None or utilization < best_utilization:
					best_utilization = utilization
					best_server = cloudlet 
		return best_server

	def getBestServerUpperLower(self,client):
		best_utilization = 100
		best_server = None
		for cloudlet in self.list_cloudlets:
			if cloudlet.getServerState()==State.UP and cloudlet.canServerAcceptClient(client):
				utilization = cloudlet.getUtilizationWithClient(client)
				if utilization >= self.lower_util and utilization <= self.upper_util:
					best_utilization = utilization
					best_server = cloudlet 

		if best_server == None:
			#if we can't find any cloudlet with the given utilization
			#we select the nearest of this utilization 
			best_value = self.lower_util
			for cloudlet in self.list_cloudlets:
				if cloudlet.getServerState()==State.UP and cloudlet.canServerAcceptClient(client):
					diff_util = self.lower_util - cloudlet.getUtilization()
					if diff_util > 0 and diff_util < best_value :
						best_value = diff_util
						best_server = cloudlet
			if best_server == None:
				#we coudn't find any server so we just return the one with the best utilization
				best_server = self.getBestServerUtilization(client)
				if best_server != None and best_server.getUtilizationWithClient(client) > self.upper_util:
					best_server = None
		return best_server

	def getClientDistanceFrom(self,node_src):
		distance_total = 0
		for node in self.list_cloudlets:
			#if node.getServerState == State.DOWN:
			distance_total +=self.distanceBetweenNode(node_src,node)*node.getNumberClientToAccessPoint()
		return distance_total

	def distanceBetweenNode(self,node1,node2):
		#return int(math.fabs(node1.getX()-node2.getX())+math.fabs(node1.getY()-node2.getY()))
		src = None
		dst = None
		
		if self.graph_type == Topology.TWOD:
			src = (node1.getX(),node1.getY())
			dst = (node2.getX(),node2.getY())
		else:
			src = node1.getName()
			dst = node2.getName()
		return len(nx.shortest_path(self.graph,source=src,target=dst))-1


	def __str__(self):
		for cloudlet in self.list_cloudlets:
			print(cloudlet)
		return "Clients->{}, Workload->{}, Capacity->{}, Utilization->{} %".format(len(self.list_clients),self.getTotalWorkload(),self.getAvalableCapacity(),self.getUtilization())
		
		


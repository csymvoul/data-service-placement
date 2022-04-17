#%%
# from constants import *
from cloud import *

number_of_user = 2000 #average number of user in the system - initial was 20
number_of_cloudlet = 500 #number of cloudlet - initial was 9
per = 50 #pourcentage between 1-99 to compute sigma
cloudlet_capacity = 10000#cloudlet capacity in Mips

#those two are used when the Broker policy best upper lower is selected
upper_util = 90
lower_util = 70

opening_strategy = OpenStrategy.OPEN_MIN
server_critiria_selection = BrokerPolicy.BEST_LATENCY
open_algorithm = OpenAlgorithm.BEST_NEIGHBORS
max_utilization = 90
quotas = []
cloudlet_to_open = []



level_workload = Workload.MEDIUM

graph_type = Topology.TWOD

time_node = 1 #ms
time_user_ap = 10 #ms
routing_switching = 0.2 #ms
time_processing = 2 #ms serving cloudlet processing

cloud = Cloud(number_of_user,number_of_cloudlet,open_algorithm,level_workload,per,
              cloudlet_capacity,opening_strategy,server_critiria_selection,time_node,
              time_user_ap,routing_switching,time_processing,graph_type,upper_util,lower_util,
              quotas,cloudlet_to_open,max_utilization)
cloud.start()
print(cloud)
#%%
cloud.displayGraph()

#%%
"""
number_of_users = [100,200,400]
number_of_cloudlets = [9,16,32]
opening_strategies = [OpenStrategy.OPEN_ALL,OpenStrategy.OPEN_MIN]
server_critirias_selection = [BrokerPolicy.BEST_LATENCY,BrokerPolicy.BEST_UTILIZATION,BrokerPolicy.BEST_UPPER_LOWER_UTIL]
open_algorithms = [OpenAlgorithm.RANDOM,OpenAlgorithm.BEST_NEIGHBORS,OpenAlgorithm.MOST_USER_FIRST]
level_workloads = [Workload.LOW,Workload.MEDIUM,Workload.HIGH]

graph_types = [Topology.TWOD,Topology.BARABASI_ALBERT]

for nu in number_of_users:
	for nc in number_of_cloudlets:
		for os in opening_strategies:
			for srs in server_critirias_selection:
				for oa in open_algorithms:
					for lw in level_workloads:
						for gt in graph_types:
							for i in range(5):
								cloud = Cloud(nu,nc,oa,lw,per,cloudlet_capacity,os,srs,time_node,time_user_ap,routing_switching,time_processing,gt,upper_util,lower_util,[],[],max_utilization)
								cloud.start()
								print(cloud) 
"""
								

								
								
								




								


# %%

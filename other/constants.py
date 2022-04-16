from enum import Enum
class State(Enum):
	DOWN = 1
	UP = 2

class BrokerPolicy(Enum):
	BEST_UTILIZATION = 1
	BEST_LATENCY = 2
	BEST_ALL = 3
	BEST_UPPER_LOWER_UTIL = 4 #between 70%-90%
	DEFAULT = 5
class OpenStrategy(Enum):
	OPEN_ALL = 1
	OPEN_MIN = 2
	SPECIFIC = 3
class Workload(Enum):
	LOW = 1
	MEDIUM = 2
	HIGH = 3
class OpenAlgorithm(Enum):
	RANDOM = 1
	MOST_USER_FIRST = 2
	BEST_NEIGHBORS = 3 #for best latency
class Topology(Enum):
	TWOD = 1
	BARABASI_ALBERT = 2
	DOROGOVTSEV = 3


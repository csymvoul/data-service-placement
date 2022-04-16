import math
block_size = 5
def parseData():
	#open file
	file = 'reports.csv'  
	with open(file) as fp:
		block = []  
		for cnt, line in enumerate(fp):
			if cnt%block_size==0:
				block.append(line)
				computeAverage(block)
				block = []
			else:
				block.append(line)

def computeAverage(block):
	if len(block) < block_size:
		return
	list_total = [0] * 17
	prefix = ''
	prefix_exist = False
	names_of_opened_cloudlet = []
	for line in block:
		fields = line.split(',')
		index,i = 0,0
		for field in fields:
			if index < 5 : 
				index +=1
				if not prefix_exist:
					prefix += field+","
				continue
			if i == 6:
				prefix_exist = True
				i +=1
				names_of_opened_cloudlet.append(field)
				continue
			list_total[i] += float(field)
			i +=1
			index +=1
	final = prefix[:-1]
	index = 0
	to_maximized = [0,1,2,3,4,5]
	for total in list_total:
		if index in to_maximized:
			final += ","+str(math.ceil((total/float(len(block)))))
		else:
			if index == 6:
				#final += ","+str(likelyElement2(names_of_opened_cloudlet,math.ceil(list_total[5]/block_size)))
				final += ","+str(likelyElement(names_of_opened_cloudlet))
			else:
				final += ","+str(round((total/float(len(block))),2))
		index +=1
	
	final +="\n"
	file = open("final.csv","a")
	file.write(final)

def likelyElement(names):
	_dict = {}
	for name in names:
		if name in _dict.keys():
			_dict[name] +=1
		else:
			_dict[name] = 1
	best_name = None 
	best_score = None 
	for key in _dict.keys():
		score = _dict[key]
		if best_score == None or score > best_score:
			best_score = score
			best_name = key 
	return best_name

def likelyElement2(names,nbr):
	_dict = {}
	_nbr_cloudlet = int(nbr)
	for name in names:
		letters = name.split('#')
		for letter in letters:
			if letter in _dict.keys():
				_dict[letter] +=1
			else:
				_dict[letter] = 1
	#now we have to take the _nbr_cloudlet best rank
	list_out = []
	while len(list_out) < _nbr_cloudlet:
		best_key = None 
		best_value = None 
		for key in _dict.keys():
			if not key in list_out:
				if best_value==None or _dict[key] > best_value:
					best_value = _dict[key]
					best_key = key 
		list_out.append(best_key)
	result = ""
	for l in list_out:
		result += l +"#"
	
	return result[:-1]

parseData()


		


			

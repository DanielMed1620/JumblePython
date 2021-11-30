class Jumble():
	
	def get_total_distinct_combinations(self, input_string):
		size = len(input_string)
		temp = {}
		for i in input_string:
			if i not in temp:
				temp[i]=0
			temp[i]+=1
		result =1
		for i in range(1,size+1):
			result = result*i 
		for x,v in temp.items():
			r=1
			for i in range(1,v+1):
				r = r*i 
			result = result//r
		return result
		
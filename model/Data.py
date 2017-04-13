# A dictionary with the attributes as key and the corresponding column as value 
class Data(dict):

	# Set the dictionary
	def __init__(self, values, attributes):
		length = min( len(values), len(attributes) )
		for i in range(length):
			# Special case when option -l rdg is set (TO CHANGE for better maintenance)
			#if values[i] in ['+','-']:
			#	 self['strand'] = values[i]
			if attributes[i] == 'score':
				self[ attributes[i] ] = float(values[i])
			elif str(values[i]).isdigit():
				self[ attributes[i] ] = int(values[i])
			else:
				self[ attributes[i] ] = values[i]

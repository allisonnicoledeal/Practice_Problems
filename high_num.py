def high_num(array):
	highest = array[0]
	for i in range(len(array)):
		if array[i] > highest:
			highest = array[i]
		# print "%r in if" % highest
	return "Highest number: %d"%highest

a = [6,3,8,98,-3,0]

print high_num(a)

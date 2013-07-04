def list_sum(my_list):
	sum = 0
	print len(my_list)
	for i in range(0,len(my_list)):
		sum += my_list[i]
		print sum
		# return sum

list1 = [10, 20, 30, 40]

list_sum(list1)

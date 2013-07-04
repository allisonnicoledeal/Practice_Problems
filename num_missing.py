def num_missing(array):
	test = []
	for i in range(0,100):
		test.append(i+1)
		# test[i] = i + 1 #WHY DOESN'T THIS WORK
		if test[i] != array[i]:
			print test[i]
			return test[i]

my_array = []

for i in range(1,101):
	my_array.append(i)
my_array[76] = 9

num_missing(my_array)



def pal_test(string):
	print "testing %s" % string
	for i in range(0,len(string)/2):
		if string[i] == string[len(string)-1-i]:
			print "continue %s matches %s" % (string[i], 
			string[len(string)-1-i])
			continue

		else:
			print "not a pallindrome at %s and %s" % (string[i], 
			string[len(string)-1-i])
			break

pal_test("hello")
pal_test("racecar")
pal_test("racer")
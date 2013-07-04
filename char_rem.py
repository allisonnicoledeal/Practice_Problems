# how to do with slicing or deleting instead of new_str = front + end

def char_rem(str, char):
	if char not in str:
		print "%s not found in %s" % (char, str)
	else:
		for i in range(len(str)):
		
			if str[i] == char:
				print str[i], i
				front = str[:i]
				if i < len(str)-1:
					end = str[i+1:]
				else:
					end = []
				new_str = front + end
				print new_str
				char_rem(new_str, char)

def char_rem2(str, char):
	while char in str:
		str.del(char)
		
			
ch = "l"
string = "allison"

char_rem2(string, ch)
# ch2 = "e"
# string2 = "hey there"
# char_rem(string2, ch2)
import re
def isValid(s):
	Pattern = re.compile("..(212|1)?..[1-6].[0-9]")
	return Pattern.match(s)
s1 = "2124567890"
s2 = "212-456-7890"
s3 = "(212)456-7890"
s4 = "(212)-456-7890"
s5 = "212.456.7890"
s6 = "212 456 7890"
s7 = "+12124567890"
s8 = "+12124567890"
s9 = "+1 212.456.7890"
s10 = "+212-456-7890"
s11 = "1-212-456-7890"
numbers = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11]
for x in numbers:
	if (isValid(x)):
		print ("Valid Number ")	
	else :
		print ("Invalid Number ")
		
#Output
#Valid Number 
#Valid Number 
#Valid Number 
#Invalid Number 
#Valid Number 
#Valid Number 
#Valid Number 
#Valid Number 
#Invalid Number 
#Valid Number 
#Valid Number 
from math import *

""" Test Values
p = 31
q = 59
n = 1829
r= 1740
k = 5221
e = 23
d = 227
"""


def isPrime(num) : 
	if num > 1:
	   # check for factors
	   for i in range(2,num):
	       if (num % i) == 0:
	           return False
	           break
	   else:
	       return True
def relativlyPrime(x, y):
	if gcd(x,y) != 1:
		return False
	else: 
		return True
def finalCheckPrime(e,d,n,r,k):
	checkMe = k % r
	if (relativlyPrime(e,n) and relativlyPrime(d,n) and
	relativlyPrime(e,r) and relativlyPrime(d,r) and checkMe == 1):
		return True
	else:
		return False

def findED(r, execptionNumber):
	# e & d are two numbers who product equal k where k is 1 mod r
	edCanidateFound = False
	counter = 1
	e = 0
	d = 0
	runNumber = 0
	while edCanidateFound == False:
		k = r * counter + 1

		if isPrime(k) == False:
			#Checks if the number has already been tested 
			# and it's factors are not relativly prime
			for x in execptionNumber:
				if x == k:
					runNumber +=1
					counter += 1
					k = r * counter + 1
			#If the number hasn't been tested then find d and e
			for i in range(2,k):
			    if (k % i) == 0:
			    	e = i
			    	d = k//i
			    	edCanidateFound = True
			    	break
		else:
			counter += 1
	return e,d,k 

def rsa(p,q):
	#check if p and q are prime
	if isPrime(p) and isPrime(q):
		n = p*q
		r = (p-1)*(q-1)
		execptionNumbers = [1]
		e,d,k = findED(r,execptionNumbers)
		ed = e*d
		if 	finalCheckPrime(e,d,n,r,ed) == False:
			execptionNumbers.append(k)
			e,d,k = findED(r,execptionNumbers)
			print('e = ' + str(e))
			print('d = ' + str(d))
			print('n = ' + str(n))
			print('r = ' + str(r))
			print('k = ' + str(k))
	else:
		exit()
pNum = 8337989838551614633430029371803892077156162494012474856684174381868510024755832450406936717727195184311114937042673575494843631977970586746618123352329889
qNum = 7755060911995462151580541927524289685569492828780752345560845093073545403776129013139174889414744570087561926915046519199304042166351530778365529171009493
rsa(pNum, qNum)
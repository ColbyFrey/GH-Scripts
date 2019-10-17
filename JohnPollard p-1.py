import math



def pollard_P_1(n):
    z = []
    prime = []
    for num in range(2,10000):
    	primes = True
    	for i in range(2,num):
        	if (num%i==0):
            		primes = False
            		z.append(num)
   		if primes:
        		prime.append(num)

    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    def e(a, b):
        return pow(a, b, n)

    def mysqrt(n):
        x = n
        y = []
        while(x > 0):
            y.append(x % 100)
            x = x // 100
        y.reverse()
        a = 0
        x = 0
        for p in y:
            for b in range(9, -1, -1):
                if(((20*a+b)*b) <= (x*100+p)):
                    x = x*100+p - ((20*a+b)*b)
                    a = a*10+b
                    break
        return a

    B1 = mysqrt(n)
    for j in range(0, len(prime)):
        for i in range(1, int(math.log(B1)/math.log(prime[j]))+1):
            z.append(prime[j])

    for pp in prime:
        i = 0
        x = pp
        while(1):
            x = e(x, z[i])
            i = i+1
            y = gcd(n, x-1)
            if(y != 1):
                p = y
                q = n//y
                return p, q
            if(i >= len(z)):
                return 0, None

print(pollard_P_1(1829))
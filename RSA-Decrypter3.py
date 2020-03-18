from pwn import *

# solves for a small e when you have n, c 
# Factor using alpertrons calculator (quick calc) - https://www.alpertron.com.ar/ECM.HTM
#bootlegsa3 2019 pico
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


ciphertext = 13612260682947644362892911986815626931

n = 126390312099294739294606157407778835887

e = 65537

phi = 126390312099294739271732633289145585896

d = modinv(e, phi)
m = pow(ciphertext, d, n)

flag = unhex(hex(m)[2:])

print ('flag: {}'.format(flag))
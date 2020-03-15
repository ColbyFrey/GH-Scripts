# Classy Cipher - Crypto

def encrypt(d, s):
	e = ''
	for c in d:
		e += chr((ord(c)+s) % 0xff)
	return e
def decrypt(text):
	counter = 0
	game = []
	plaintext = ''
	for letter in text:
		numberText = ord(letter)+128 
		numberText -= 89
		plaintext += chr(numberText)
	print(plaintext)

decrypt(':<M?TLH8<A:KFBG@V')



#assert encrypt(flag, shift) == ':<M?TLH8<A:KFBG@V'
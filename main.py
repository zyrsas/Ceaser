from random import shuffle
from string import maketrans

alphabet="abcdefghijklmnopqrstuvwxyz" + \
	 "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
         ":.;,?!@#$%&()+=-*/_<> []{}`~^"

def translator(text,alphabet,key):
	trantab = maketrans(alphabet,key)
	return text.translate(trantab)

def caesar_encode(plaintext,s,alphabet):
	return translator(plaintext,alphabet,alphabet[s:]+alphabet[:s])

def caesar_decode(ciphertext,s,alphabet):
	return translator(ciphertext,alphabet,alphabet[-s:]+alphabet[:-s])

def substitution_encode(plaintext,alphabet):
	randarray=range(0,len(alphabet))
	shuffle(randarray)
	key=""
	for i in range(0,len(alphabet)):
		key+=alphabet[randarray[i]]

	return translator(plaintext,alphabet,key),key

def substitution_decode(ciphertext,key,alphabet):
	return translator(ciphertext,key,alphabet)


# Example useage
plaintext="The wheels on the bus go round and round. round" + \
" and round. round and round. The wheels on the bus go round and"+ \
" round, all through the town!"


print 
print "SUBSTITUTION"
ciphertext,key=substitution_encode(plaintext,alphabet)
print "Key: ", key
print "Plaintext:", plaintext
print "Cipertext:", ciphertext
print "Decoded  :", substitution_decode(ciphertext,key,alphabet)

print 
print "CAESAR SHIFT"
ciphertext=caesar_encode(plaintext,5,alphabet)
print "Key: ", 5
print "Plaintext:", plaintext
print "Cipertext:", ciphertext
print "Decoded  :", caesar_decode(ciphertext,5,alphabet)

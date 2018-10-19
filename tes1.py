a=13
b=[1,2,4,13,54]
print (a in b)
print (a not in b)

print ("==============================")

c=13
b=13
print (a is b)
print (a is not b)

print ("==============================")

import math
import random
#import tensorflow as tf
from random import randint
print ({math.sqrt(225)})
#tf.__version__
print ({randint(0,100)})

print ("I/O ==============================")

print ('Hello,World')
str = input('Nama: ')
list = input('angka anda = ')

file = open('tes1.txt','ab') #b = binary mode
file.write(bytes(str+list,encoding='utf-8'))
file.close()

file = open('tes1.txt','rt') #t = text mode
print (file.read())
file.close()

print ("Try/Except==============================")

str = "tes123"
try :
    print (int(str))
except:
    print ("cannt convert")
    
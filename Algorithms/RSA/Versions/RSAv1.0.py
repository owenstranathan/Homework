#This is an RSA encryption implementation done by Owen Stranathan
#for Algorithms class taught by Dr. Zhong Hui Duan 
#this Program will include the following functions:
#Prime Number Generator
#Extended Euclidean Algorithm 
#RSA Encryption
#RSA Decryption
#
#This program is a python script                                            |
#___________________________________________________________________________





#IMPORTS

import random
import math


#FUNCTIONS

#Accepts an integer and returns true if it is prime, false if it is composite
def Fermat(n): 
    #if n is 1 or less then it is not prime
    if n > 1:
        #Repeats the test several times to have a higher confidence of accuracy
        for x in range(5):
            
            #finds an a s.t. 1 < a < n
            a = random.randint(2, n)-1

            # ( a^n-1 ) % n
            if  pow(a,n-1,n) != 1:
                return False
        #if n makes it through the loop then it is very probably prime    
        return True    
    #if n is 1
    else:
        return False
        
        
#finds a random number of length l and returns it if it is prime.
def PrimeGen(l):
    #get a number between 10^l-1 and 10^l which will be a string of numbers of length l 
    n = random.randrange(pow(10,l-1), pow(10,l))
    #if it is prime return it
    if(Fermat(n)):
        return n
    #if not try again
    else:
        return PrimeGen(l)



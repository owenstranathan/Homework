#This is an RSA encryption implementation done by Owen Stranathan
#for Algorithms class taught by Dr. Zhong Hui Duan 
#this Program will include the following functions:
#Fermat Primality test
#Prime Number Generator
#Euclidean Algorithm
#Extended Euclidean Algorithm 
#RSA Encryption
#RSA Decryption
#
#This program is a python script                                            |
#___________________________________________________________________________
############################################################################
#Some Notes on Python:
#pow(a,b,c) returns (a**b)%c //computed more efficiently than pow(a,b)%c i.e. using modular exponentiation
#range(n) = [1,2,3,4,5,6,....,n]
#range(a,n) = [a+1,a+2,a+3,....,n]
#the third arrgument of the range function gives a step for iteration.  


#IMPORTS

import random
import math
import sys

#MAIN


def main(argv):
    public , private = keyGen(100)
    args = sys.argv
    #variable for control flow, based on length of argument list
    ctrl = len(args)
    #test
    a = rsaEncrypt(public[0], public[1], "I have a secret message and this is it")
    print a
    b = rsaDecrypt(private[0],private[1],a)
    print b
    #case: one Arg
    if(ctrl == 2):
        if(args[1].isdigit()):
            print primeGen(int(args[1]))
        else:
            print "Unsupported input detected!\nTraceback:"
            print "arguments are ", args
            print "args[1] must be numeric"
    elif(ctrl == 3):
        if (args[1].isdigit() and args[2].isdigit()):
            print eEuclid(int(args[1]),int(args[2]))
        else:
            print "Unsupported input detected!\nTraceback:"
            print "arguments are ", args
            print "args[1] and args[2] must be numeric"
    elif(ctrl == 4):
        if(args[1].isdigit() and args[2].isdigit() and args[3].isdigit()):
            print altKeyGen(int(args[1]),int(args[2]),int(args[3]))
        else:
            print "Unsupported input detected!\nTraceback:"
            print "arguments are ", args
            print "args[1] and args[2] and args[3] must be numeric"
    elif(ctrl == 5):
        if args[1] == 'e':
            if(args[2].isdigit() and args[3].isdigit()):
                print rsaEncrypt(int(args[2]), int(args[3]), args[4])
            else:
                print "Unsupported input detected!\nTraceback:"
                print "arguments are ", args
                print "args[2] and args[3] must be numeric"
        elif args[1] == 'd':
            if(args[2].isdigit() and args[3].isdigit()):
                print rsaDecrypt(int(args[2]), int(args[3]), args[4])
            else:
                print "Unsupported input detected!\nTraceback:"
                print "arguments are ", args
                print "args[2] and args[3] must be numeric"
        else:
            print "Unsupported input detected!\nTraceback:"
            print "arguments are ", args
            print "args[1] must be either 'e' or 'd', other arguments result in error!"
                

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
def primeGen(l):
    #get a number between 10^l-1 and 10^l which will be a string of numbers of length l 
    n = random.randrange(pow(10,l-1), pow(10,l))
    #if it is prime return it
    if(Fermat(n)):
        return n
    #if not try again
    else:
        return primeGen(l)

#returns the Greatest Common Divisor of 2 numbers
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

#returns a number that is relativly prime to the argument(gcd(p,e) ==1)
def relPrime( p ):
    #1<e<p
    e = random.randrange(2, p)-1
    #if e and p are relatively  prime return e
    if gcd(p,e) == 1:
        return e
    #otherwise keep trying
    else:
        return relPrime(p)


#Extended Euclidean Algorithm returns an (x,y) s.t. gcd(a,b) = ax + by
def eEuclid(a, b):
    #base case for the gcd(a,b) recursion
    if a == 0:
        return ( 0, 1)
    
    else:
        #recursively loop through to the base case
        y,x = eEuclid( b%a, a )
        #returns a value for y,x to be recursively computed
        y,x = (x - (b // a) * y , y)
        return y,x

#this Alternate key gen function exisits simply to meet with the prescriped output format
#detailed in the project prompt 
def altKeyGen(e,p,q):
         n = p*q
         phi = (p-1) *(q-1)
         d, quotient = eEuclid(e, phi)
         if d<0:
             d+= phi
         return (d,n)



#creates public and private RSA encryption keys starting with p and q of length l 
def keyGen(l):
         #Pick two "Large = l" primes for p and q
         p,q = primeGen(l), primeGen(l)
         #compute n as the product of p and q
         n = p*q
         #compute phi(n)
         phi = (p-1) * (q-1)
         #find e s.t. gcd(phi, e) = 1
         e = relPrime(phi)
         #find d and quotient s.t. gcd(phi,e) = e*d + phi*quotient = 1
         d,quotient = eEuclid( e, phi)
         
         #if d is negative add phi back to it then return the tuples
         if d < 0:
             d += phi 
         return (e,n),(d,n)
         

#converts the string to an int that can be converted back
def str2Int(a):
    m = 0
    #for every element of the string
    for i in a:
        #do this 
        m = 128*(m + ord(i))
    #to result in this m = 128^len(m)(m[0]) + 128^(len(m)-1)(m[1]) + ... + 128(m[len(m)-2]) + m[len(m)-1]
    return m    

#converts the string back to a string, since the string would be reversed in the process it also flips the conversion
def int2Str(m):
    #make a blank string and an empty integer to take values
    a = ""
    c = 0
    #while you still have something left in your number
    while m > 0:
        #find the last number added to the number with modulus 
        c = m%128
        #convert to a character and then to a string and add it to the empty string
        a += str(chr(c))
        #remove the number to have a number s.t. m%128 = 0
        m -= c
        #divide by 128 to leave a remainder for the next loop
        m = m/128
    #return a reversed copy of a to get back the original message
    return a[::-1]

 
def rsaEncrypt(e,n,m):
    M = str2Int(m)
    c = 0
    if M < n:
        c = pow(M,e,n)
    else:
        print "M is too big"
    return c

def rsaDecrypt(d,n,c): 
    m = pow(c,d,n)
    return int2Str(m)

if __name__ =="__main__":
    main(sys.argv)

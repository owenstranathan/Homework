This is the readme file for RSA.py written by Owen D. Stranathan
RSA.py is a python script that implements RSA encryption per the specifications given at this link:
http://www.cs.uakron.edu/~duan/class/435/projects/project1/project1.htm
The program will run with any Python 2 interpreter or greater.

This script include the following functions:

main(argv)
	- this is the main function through which the command line argumants are handled.
	- the function takes the list of command line arguments and determines what to do
	- based on the length of said list.

Fermat(integer)
	- uses Fermat's Little Theorem to determine the primality of a number.
	- repeats the test 5 times to have high confidence of accuracy
	- @returns true for prime arguments
	- @returns false for composite arguments

primeGen(integer)
	- uses random.randrange() method to get a random integer of length argument 
	- then uses Fermat() to determine the primality of that integer
	- @returns the number if Fermat() returns true
	- @returns a recursive call to itself if Fermat returns false

gcd(integer, integer)
	- uses recursion to find the greatest common divisor of the two arguments
	- @returns the gcd

relPrime(integer)
	- uses gcd() and random.randrange
	- @returns and integer that is relativly prime to the arguments

eEuclid(integer, integer)
	- uses the gcd() method to find an x,y s.t. gcd(a,b,) = ax + by 
	- @returns (x,y)

altKeyGen(e,p,q)
	- uses the RSA algoritms to find key (d,n) using the aforementioned functions
	- @returns (d,n)

keyGen(l)
	- makes keys (e,n) (d,n) using numbers p and q l bits long
	- @returns (e,n) (d,n)

str2Int(string a)
	- uses the prescribed padding scheme for converting a string to an integer
	- @returns the integer representation of the argument string
	 
int2Str( int m)
	- uses modulus to revert the integer m to a string
	- this function is the inverse of str2Int() function
	- @returns the string reprentation of the integer

rsaEncypt(int e, int n, string m)
	- accepts a string and 2 integer
	- converts the string to an integer
	- encrypt that integer using rsa and the key( e, n) given by the arguments
	- @returns encrypted message

rsaDecrypt(int d, int n, int c)
	- accepts 3 integers
	- decrypts the integer c using rsa and the key(d,n) given by the arguments
	- converts the decrypted integer to a string and reverses it to get back the message that was encrypted


Notes:
#RSA.py is an RSA encryption implementation done by Owen Stranathan                                                 
#for Algorithms class taught by Dr. Zhong Hui Duan                                                                
#this Program will include the following functions:
_______________________________                                                               
About Python native Functions: |
_______________________________|

#pow(a,b,c) returns (a**b)%c //computed more efficiently than pow(a,b)%c i.e. using modular exponentiation        
#range(n) = [1,2,3,4,5,6,....,n]                                                                                  
#range(a,n) = [a+1,a+2,a+3,....,n]                                                                                
#range(a,n,i)= [a, a+i, a+2i,....,n - n%i]

#the third argument of the range function gives a step for iteration.

#random.randrange(a,b) returns a random number within the interval of (a,b)

_______________________________________________________________________
EXCEPTIONS:							       |
_______________________________________________________________________|

This script will work as described with the following exceptions:

rsaEncrypt()
	- if the third argument string results in an integer that is larger than the second argument integer
	- then the program will exit wth the message : "M is too big!"
	- please use appropriately sized arguments


rsaDecrypt()
	- if the third argument is bigger than the second argument 
	- then the program will exit with the following message : "c is too big!"
	- please use appropriately sized arguments

all other exceptions are handled to the best of the programmers knowledge



# import time
# import math


# def check(i,num):
# 	array=[0]*10
# 	k=0
# 	j=0
# 	while (num)!=0:
# 		k=num*10
# 		k=int(k%10)
# 		array[k]+=1
# 		j+=1
# 		#print("num,k",num,k)
# 		#print("array",array)
# 		#print("i",i)
# 		num=num*10-k
	
# 	#for i in range()
# 	print(j)
# 	return j


# def generate():
# 	maxi=-1
# 	l=0
# 	for i in range(2,11):
# 		num=1/i
# 		m=check(i,num)
# 		if m>maxi:
# 			maxi=m
# 			l=i
# 			print(num)
# 	return l

# 		#print(num)
# # def maxi(a):
# # 	for i,v in enumerate(a):
# # 		return max(a),i

# start=time.time()
# result=generate()
# elapsed=time.time()-start

# print("result is %s found in %s"%(result,elapsed))#not working

#983 is the answer tho...
#http://radiusofcircle.blogspot.com

#time module for calculating execution time
import time

#time at the start of execution
start = time.time()

#long division as explained
#https://www.mathsisfun.com/long_division.html
def recurring_decimal(divisor):
	if divisor <10:
		divident = 10
	elif divisor >=10 and divisor <100:
		divident = 100
	else: 
		divident = 1000
	value_to_check = divident #10 or 100 or 1000
	string = ''
	for i in xrange(divisor):
		string += str(divident/divisor)
		divident = divident%divisor
		if divident < divisor:#adding decimal
			divident *= 10
			if divident < divisor:#adding zero after decimal
				divident *= 10
				string += '0'
				if divident < divisor:#adding another decimal after 0
					divident *= 10
					string += '0'
		if divident == value_to_check:
			return string

#sieve of Eratosthenes
#https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
def sieve(n):
	is_prime = [True]*n
	is_prime[0] = False
	is_prime[1] = False
	for i in xrange(2,int(n**0.5+1)):
		index = i*2
		while index < n:
			is_prime[index] = False
			index = index+i
	prime = []
	for i in xrange(n):
		if is_prime[i] == True:
			prime.append(i)
	return prime

#We have used euclid Algorithm to find the 
#lcm also called smallest multiple

#gcd function for calculating lcm
def gcd(n1,n2):
	remainder = 1
	while remainder != 0:
		remainder = n1%n2
		n1 = n2
		n2 = remainder
	return n1

#lcm of two numbers using euclid Algorithm
#lcm = (number1*number2)/GCD(number1,number2)
def lcm(n1,n2):
	return (n1*n2)/gcd(n1,n2)

#generating the primes
primes = sieve(1000)

#assuming all the numbers have no repetition
d = {n: 0 for n in range(1,1000)}

#Adding the value for 1/3
d[3] = 1

#generating the length of repeating decimals
#for prime numbers excluding 2, 3 and 5
for i in primes[3:]:
	d[i] = len(recurring_decimal(i))

#looping for numbers greater than 5 
#using the properties of repeating decimals;
#https://en.wikipedia.org/wiki/Repeating_decimal
for i in xrange(6,1000):
	if not d[i]:
		if i % 2!= 0 and i%5!= 0: #number coprime to 10
			for j in primes:
				if i%j == 0:
					number1 = d[j]
					number2 = d[i/j]
					d[i] = lcm(number2,number1)
					break
		else: #number not coprime to 10
			number = i
			while number%2 == 0:
				number = number/2
			while number%5 == 0:
				number = number/5
			d[i] = d[number]

#printing the largest value
#as the index starts from 0, adding 1 ;)
print d.values().index(max(d.values()))+1

#time at the end of execution
stop = time.time()

#printing the total time for execution
print stop- start
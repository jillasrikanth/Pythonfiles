#VARIABLES AND DATATYPES
#1

#A = "Lync"
#L = ["Digital","lync","hyderabad","kukatpally","gachbowli"]
#print(A in L)

#2

#x=45
#y=65

#x = (00101101)
#y = (01000001)
#print(x & y)
#print(x | y)
#print(x ^ y)
#print(x >> y)
#print(x << y)

#3

#import math as m
#z=65.33
#y=print(int(z))
#print(m.sqrt(z))
#print(m.exp(z))
#print(m.factorial(5))
#print(complex(z))
#""Double can't be done in python""
#print (abs(z))



#4

#a = int(input("enter a number::"))
#b = int(input("enter a number::"))
#d = a+b
#print(d)

#5

#a=15
#b=2
#print(a==b)
#print(a!=b)
#print(a > b)
#print(a < b)
#print(a <= b)
#print(a >= b)



#CONDITIONAL STATEMENTS
#z = int(input("enter your marks::"))
#if z > 70 and z < 90:
#	print("distinction")
#elif z > 50 and z < 60:
#	print("first class")
#elif z > 40 and z < 50:
#	print("second class")
#else:
#	print("passed")		


		

#year = int(input("enter year::"))	
#if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
#	print("year is a leap year")
#else:
#	print("the year is not a leap year")



#a = int(input("enter a number you want to be checked:"))
#if (a % 2) == 0:
	#print("the num is even num")
#else:
	#print("the num is odd num")

	

#country = input("enter the country you want to know:")
#state = input("enter the state you want to know:")
#if country == 'india' and state=='telangana':
#	print("No of districts in telanagana are:31")
#elif country == 'india' and state =='AP':
#	print("AP has 13 districts")
#elif country == 'india' and state == 'kerela':
#	print("kerela")
#elif country == 'india' and state == 'assam':
#	print(" assam has 33 districts")
#elif country == 'india' and state == 'karnataka':
#	print(" karnataka has 30 districts")	
#elif country == 'india' and state == 'gujarat':
#	print("gujarat has 33 districts") 

	
#a = 10
#b = 20
#c = 15
#if(a>b)and(a>c) :
#	largest = a
#elif(b>a)and(b>c):
	#largest = b
#else:
#	largest = c

#print("the largest among three is",a,",",b,"and",c,"is",largest)


#CONTROL FLOW


#1

#low = int(input("enter lower num:"))
#high = int(input("enter higher num:"))
#for i in range(low,high+1):
#	if (i%7==0 and i%5==0):
#		print(i)



#2
 
#for i in range(1,10):
#	if i%2==0:
#		print(i**2)


#3

#for i in range(1,100):
#	if i%7==0 and i%2!=0:
#		print(i)
	
		

#str = input("enter a String::")
#for i in range(0,len(str)):
#	if str[i]=='a' or str[i]=='e' or str[i]=='i' or str[i]=='o' or str[i]=='u': 
#		print(str[i])







# string = ["python session is started in digitallync"]
# words=[]
# vowels=[]
# for i in string:
# 	if i not in words:
# 		words.append(i)
# 		for i in range(1,len(string)):
# 			if string(i)=='a':
# 				vowels.append(i)
		
# print(words)		
# print(vowels)



#FUNCTIONS 

def printme():
	print("hello")
printme()
print(type(printme))	




















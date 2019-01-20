# num = 5
# for i in range(1, 11):
#    print(num,'x',i,'=',num*i)


# num = 1
# for i in range(20,30):
# 	if i % 2 == 0:
# 		print(str(i)+"is an even number")
# 	else:
# 		print(str(i)+"is an odd number")



# val = 10
# for i in range(0,5):
# 	for j in range(0,i+1):
# 		ch = chr(val)
# 		print(ch,end =" ")
# 	val = val+1
# 	print()	


# for num in range(5):
#     for i in range(num):
#         print (num, end=" ") 
#     print("\n")





# #FUNCTIONS 
# def printme():
# 	print("hello")
# # printme()
# # print(type(printme))	
# def printme():
# 	print("bye")

# printme()


# def printme(name):  #name--> formal param
# 	print("hello" + name)
# printme("Srikanth")   #"srikanth"--->Actual param


# def addnums(a,b):
# 		print(a+b)
# addnums(10,20)		



# def avg(a,b,c,d,e):
# 		res = (a+b+c+d+e)/5
# 		print(res)
# avg(10,20,30,40,50)
# avg(13,25,130,150,12)


# #RETRUN VALUE
# def avg(a,b,):
# 		res = (a+b)/5
# 		print(res)
# # avg(10,20,30,40,50)
# # avg(13,25,130,150,12)
# 		return res
# print(avg(10,20))		


#DOCSTRING


# def avg(a,b):
# 		"""this finds avg of 2 nums """
# 		res = (a+b)/2
# 		print(res)
# print(avg.___doc___)

		# c=a+b
		# return c
# a = int(input("enter the number"))
# b = int(input("enter the number"))		
# def addnums(a,b):
# 		c=a+b
# 		print(c)
# 		return c

# def subnums(a,b):
# 		c=a+b
# 		print(c)
# 		return c

# def mulnums(a,b):
# 		c=a+b
# 		print(c)
# 		return c		
# def divnums(a,b):
# 		c=a+b
# 		print(c)
# 		return c

# # addres = addnums(a,b)
# # subres = subnums(addres,b)
# # mulres = mulnums(subres,b)
# # divres = divnums(mulres,b)
# divnums(mulnums(subnums(addnums(a,b),b),b),b)



# def category(a,b):
# 		' ' ' 'please select the category do u want 
# 									1.Arith 
# 									2.Logical '' ' '
# 			cat = int(input("enter the category"))
# 			if cat == 1:
# 					arith()
# 			elif cat == 2:
# 					Logical
# 		 else:
# 		 				print("wrong input")
# def arith():
# 			' ' ' ' select an operation
# 									1.add
# 									2.sub
# 									3.mul
# 									4.div ' ' ' '
# 				ope = int(input("eneter an operation"))
# 				num1 = int(input("enter a number"))
# 				num2 = int(input "enetrb a number")									

# print(category.___doc___)		






#VARIABLE PARAETERS:

# def avg(*args):#args is not a keyword we can use any thing we want
# 		print(args)
# 		print(type(args))
# avg(10,20)	
# avg(10,20,30)
# avg()	


# def avg(a,b*args):#args is not a keyword we can use any thing we want
# 		print(a)
# 		print(b)
# 		print(args)
# 		print(type(args))
# avg(10,20)	
# avg(10,20,30)



# def avg(*vars):
# 			s = 0
# 			for i in vars:
# 						s = s+i
# 			res = s/len(vars)
# 			print(res)

# avg(10,20)	
# avg(10,20,30)
# avg(10,20,30,40,50,60)

# def first():
# 	return 100

# def second():
# 	return first
# # print(first)
# # print(second)


# # print(first())#100
# # print(second())#loaction of frist

# # print(type(first()))	#int
# # print(type(second()))#function

# a = second()
# a()
# print(type(a))



#Returing <FUNCTION CALL>

# def first():
# 	print("hello")
# 	return 100

# def second():
# 	print("bye")
# 	return first()
# # print(first)
# # print(second)	

# # print(first())
# # print(second())


# print(type(first()))
# print(type(second()))


# def emp(name,role):
# 	print("emp name is" + name)
# 	print("emp role is" + role)
# emp(role = "pd" , name = "KHAN")


# def makecake(flav,wei,shape):
# 	print("flavour is" +flav)


#LAMBDA FUNCTIONS

# addnums = lambda a,b :a+b
# print(addnums(10,20))

# email = lambda name,organisation :name+organisation
# print(email(jillasrikanth727,gmail.com))



# fO = open("demo.txt","w")
# # fO.write("hello \")
# # fO.write("hello")
# words = ["firt\n","second\n","third\n"]
# fO.writelines(words)


# fO.close()



# foo = open("demo.txt","a")
# foo.write("fourth")
# foo.close()


# fr = open("demo.txt","r")
# print(fr.readline())
# print(fr.readline())
# print(fr.read())
# fr.close()





# with open("demo.txt","r") as fr:
# 	print(fr.read())
# 	print(fr.seek(5))

# importing random module 
import random as r
# made an empty dictionary 
usersdict = {}

# function to check keys in dictionary and returns 0 or 1
def chkuser(name):
	if name in usersdict.keys():
		print("User already exists")
		return 0
	else:
		return 1

# generating random numbers of "n" length and returning 
def makeNums(n):
	numpwd = ""
	for i in range(0 , n):
		numpwd = numpwd + str(r.randint(0,9))
	# print(numpwd)
	return numpwd

# generating random chars of "n" length and returning 
def makeChrs(n):
	chrpwd = ''
	l1 = []
	for i in range(0 , n):
		a = chr(r.randint(65 , 90))
		b = chr(r.randint(97 , 122))
		l1.append(a)
		l1.append(b)
		r.shuffle(l1)
	ans = r.sample(l1 , k = n)
	for i in ans:
		chrpwd = chrpwd +i
	# print(chrpwd)
	return chrpwd


def genpwd(name):
	if chkuser(name) == 1:
		password = makeChrs(4)+ makeNums(4)+makeChrs(4)+makeNums(4)
		usersdict[name] = password
		print(password)
		return password
	
genpwd("khan")
genpwd("Hari")
# genpwd("Hari")
# genpwd("khan")
print(usersdict)
f = open("usersdict.txt","w")
f.write( str(usersdict) )
f.write(str(usersdict.name()))

# for x in usersdict:
	 
f.close()






# import random as r
# print(r.random())
# print(r.randint(10,20))
# print(r.randrange(10,20))

# l1 = [x for x in range(1,11)]
# print(l1)
# r.shuffle(l1)
# print(l1)

# print(r.choice(l1))
# print(r.sample(l1))

# name = input("enter a name")
# userdict = {}

# def usercheck(name):
# 	if name in userdict.keys():
# 		print("user already exists")
# 		return 0
# 	else:
# 		return 1	

# def genchars(num):
# 	numpwd = ""
# 	for i in range(0,n):
# 		numpwd = numpwd + str(r.randint(0,9))
# 	return numpwd	
# def fennums(num):
# 	chrpwd = ""
# 	l1 = []
# 	for i in range(0,n):
# 		a = chr(r.randint(65,90))
# 		b = chr(r.randint(67,122))
# 		l1.append(a)
# 		l1.append(b)
# 		r.shuffle(l1)
# 	ans = r.sample(l1,k=n)
# 	for i in ans:
# 		chrpwd = chrpwd + i	





# def genpass(username,finalpwd):
# 	userdict[username] = finalpwd	





# import os
# print(os.name)
# os.mkdir("srikanth")
# os.makedirs("sri/hari/SPR")
# os.rmdir("srikanth")
# print(os.getcwd())
# os.chdir("")ss










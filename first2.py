#num = int(input("enter a num"))
#num = [i for i in range(num+1)]
#print(num)


#num = int(input("enter a num"))
#even=[i for i in range(num+1) if i%2==0]
#print(even)


#sqr = [i**2 for i in range(10)]
#print(sqr)

#esqr = [i**2 for i in range(10) if i%2==0]
#print(esqr)


#a = input("enter a stmnt")
#w = a.split()
#lenwords=[]
#for i in w:
#	lenwords.append(len(i))
#print(lenwords)


#a = input("enter a stmnt")
#wlist = [len(i)  for i in a.split()]
#print(wlist)

#TUPLE

#nums= (3,4,5,6,13,20)
#print(nums)
#print(type(nums))


#char = "aa","b","python","java"
#print(char)
#print(type(char))
#char = list(char)
#char[0] = "AAAA"
#char = tuple(char)
#print(char)
#print(type(char))


#a = [ ]
#l = int(input("enter length"))
#for i in range(0,l+1):

#	ele = input("enter an element")
#	if ele.isdigit():
	#	ele = int(ele)
	#	a.append(ele)
	#elif "." in ele:
	#	e = ele.split(".")
	#	for i in e:
	#			if i.isdigit():
#				ele = float(ele)
#		        a.append(ele)
#		    else:
#		    	a.append(ele)
#	else:		
#		a.append(ele)
#a = tuple(a)	

#print(a)





##DICTONARY

#d = {20:40,"tech":"pyhton"}
#print(d)
#print(type(d))


#Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]} 
#print("\nDictionary with the use of Mixed Keys: ") 
#print(Dict) 


#Accesing of elements

#emp={"name":"srikanth","tech":"python","age":"100","tech":"c++"}
#print(emp["name"])

#MODIFYING
#emp["tech"]="java"
#print(emp)
#emp["location"]="hyd"
#print(emp)

#DELETING

#del emp["tech"]
#print(emp)

#del emp
#print(emp)

#print(len(emp))
#print(emp.keys())
#print(emp.values())
#print(emp.items())
#for i in emp.keys():
#	print(i)

#newdict = emp.copy()
#print(newdict)
#emp.clear()
#print(emp)

#org={"name":"lync","add":"hyd","estd":"2015"}
#print(org)

#emp.update(org)
#print(emp)
#print(org)
#emp.pop("tech")
#print(emp)
##emp.popitem()
#print(emp)


#numsq = {}
#n = int(input("enter a value"))
#for i in range(1,n+1):
#	numsq[i]=i**2
#print(numsq)

#stmt = input("enter a stmnt")
#wordslen = {}
##words = stmt.split()
#for i in words:
#	wordslen[i]=len(i)
#print(wordslen)

#stmt = input("enter a stmnt")
#wordslen = {}
##words = stmt.split()
#for i in stmt.split():
#	wordslen[i]=len(i)
#print(wordslen)

#l1=[1,2,3,4]
#l2=["one","two","three","four"]
#a={}
#if len(l1) == len(l2):
#	for i in range(len(l1)):
#		a[l1[i]] = l2[i]
#else:
#	print("uneaqual lengths")
#print(a)			

##z = zip(l1,l2)
#print(z)
#d = dict(z)
#print(d)

#d= dict(zip(l1,l2))
#print(d)


#d = {i:i*2 for i in range(10) if i%2==0}
#print(d)


#TASK
#stmt = "i love python"
#d = {word:len(word) for word in stmt.split()}
#print(d)
#TASK 2

#stmt = "i love python"
# = {word:len(word) for word in stmt.split() if len(word)>4}
#print(d)


###SETS##
#nums ={1,2,3,4}
#print(nums)
#print(type(nums))

#empset = set(())
#print(empset)
#print(type(empset))

#nums = set((1,2,3,4,))
#print(nums)
#print(type(nums))

#rep = {1,2,3,4,5,6,7,8}
#print(rep)
#print(rep[3])
#for i in rep:
	#print(i)
#rep.add(300)
#rep.remove(2)
#print(rep)
#rep.discard(110)
#print(rep)




s1={10,20,30,40}
s2={20,50,60,70}
s3={10}
s4={100}


#print(s1.union(s2))
#print(s1.intersection(s2))
#rint(s1.difference(s2))
#print(s2.isdisjoint(s1))
#print(s1.isdisjoint(s4))
#print(s1.issuperset(s3))
#print(s1.issubset(s3))




print(s1 | s2)

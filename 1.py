lower = 10
upper = 20
#print("Prime numbers between",lower,"and",upper,"are:")
for num in range(lower,upper + 1):
	if num > 1:
		for i in range(2,num):
			if (num % i) == 0:
				break
		else:
			print(num)
			for num1 in range(lower,upper + 1):
				if num1 != num:
					print(num1)
				else:
					break
          






vowels = ('a', 'e', 'i', 'o', 'u')

fSet = frozenset(vowels)
print('The frozen set is:', fSet)
print('The empty frozen set is:', frozenset())

















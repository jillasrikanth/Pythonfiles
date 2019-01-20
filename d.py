##print("Enter your name:")
##x = input()
##print("Hello, " + x)
x = "hi "
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

def AbyB(a, b):
  try:
    c = (a + b)/(a - b)
  except ZeroDivisionError as error:
    print("a/b result is 0")
  else:
    print(c)

if __name__ == '__main__':
    AbyB(3, 4)
    AbyB(3, 3)
    AbyB(4, 3)

#OUTPUT:
#An Exception
#-7.0 
#a/b result is 0 
#7.0 
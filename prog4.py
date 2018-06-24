def AbyB(a, b):
  try:
    c = (a + b)/(a - b)
  except ZeroDivisionError as error:
    print("a/b result is 0")
  else:
    print(c)

def main():
    AbyB(3, 4)
    AbyB(3, 3)
    AbyB(4, 3)

if __name__ == '__main__':
    main()

#OUTPUT:
#An Exception
#-7.0 
#a/b result is 0 
#7.0 
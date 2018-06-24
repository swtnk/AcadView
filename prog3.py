def get_output():
  try:
    raise NameError("Hi There") #Raise Error
  except NameError as error:
    return 'An Exception'

if __name__ == '__main__':
    print(get_output())

#OUTPUT: An Exception
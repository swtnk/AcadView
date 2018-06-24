def get_output():
  try:
    raise NameError("Hi There") #Raise Error
  except NameError as error:
    return 'An Exception'

def main():
    print(get_output())

if __name__ == '__main__':
    main()

#OUTPUT: An Exception
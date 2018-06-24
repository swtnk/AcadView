def error_detection(lst):
  try:
    return lst[len(lst)]
  except IndexError as error:
    return error

def main():
    print(error_detection([1, 2, 3]))

if __name__ == '__main__':
    main()

#OUTPUT: list index out of range
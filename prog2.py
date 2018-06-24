def error_detection(lst):
  try:
    return lst[len(lst)]
  except IndexError as error:
    return error

if __name__ == '__main__':
    print(error_detection([1, 2, 3]))

#OUTPUT: list index out of range
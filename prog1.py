def error_detection(num):
  if num < num + 1:
    try:
      num = num / (num - num)
      return num
    except ZeroDivisionError as error:
      return error

if __name__ == '__main__':
    print(error_detection(3))

#OUTPUT: division by zero
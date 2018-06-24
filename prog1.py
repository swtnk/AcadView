def error_detection(num):
  if num < num + 1:
    try:
      num = num / (num - num)
      return num
    except ZeroDivisionError as error:
      return error

def main():
  print(error_detection(3))

if __name__ == '__main__':
    main()

#OUTPUT: division by zero
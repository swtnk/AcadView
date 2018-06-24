from operator import mul
from functools import reduce
def que1():
    tup = ('Human', 234, 28.9, [34, 53, 90])
    return tup

def que2(tup):
    return max(tup), min(tup)

def que3(tup):
    return reduce(mul, tup)

def main():
    ans1 = que1()
    print(ans1, len(ans1), sep=" has length ")
    ans2 = que2((989, 203, 45, 343, 232))
    print(ans2)
    ans3 = que3((1, 2, 3, 4, 5))
    print(ans3)

if __name__ == '__main__':
    main()
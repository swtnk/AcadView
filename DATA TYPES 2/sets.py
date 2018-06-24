def que1():
    try:
        set1 = set(map(int, input('Enter space separated values of set1: ').split(' ')))
        set2 = set(map(int, input('Enter space separated values of set2: ').split(' ')))
        return set1, set2
    except Exception as error:
        print('Please enter integer values only\nTry again:')
        que1()

def que2(sets):
    return sets[0] - sets[1]

def que3(sets):
    return sets[0] == sets[1]

def que4(sets):
    return sets[0].intersection(sets[1])

def main():
    ans1 = que1()
    print(ans1)
    ans2 = que2(ans1)
    print(ans2)
    ans3 = que3(ans1)
    print(ans3)
    ans4 = que4(ans1)
    print(ans4)

if __name__ == '__main__':
    main()
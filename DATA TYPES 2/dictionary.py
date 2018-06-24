import operator

def que1():
    return {'Student1' : 78, 'Student2' : 89, 'Student3' : 82, 'Student4' : 91, 'Student5' : 81}

def que2(result):
    return dict(sorted(result.items(), key=operator.itemgetter(1)))

def que3(string):
    return {x : string.count(x) for x in set(string)}

def main():
    ans1 = que1()
    print(ans1)
    ans2 = que2(ans1)
    print(ans2)
    ans3 = que3('MISSISSIPPI')
    print(ans3)

if __name__ == '__main__':
    main()
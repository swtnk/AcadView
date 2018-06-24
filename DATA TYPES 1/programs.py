def que1():
    try:
        return list(map(str, input('Enter space separated names of companies: ').split(' ')))
    except Exception:
        print('Please enter string values only.\nTry Again:\n')
        que1()

def que2(companies):
    companies_to_add = ['google', 'apple', 'facebook', 'microsoft', 'tesla']
    return companies + companies_to_add

def que3(companies):
    return({x : companies.count(x) for x in set(companies)})

def que4():
    try:
        return sorted(list(map(int, input('Enter space separated integer values in list: ').split(' '))))
    except Exception:
        print('Please enter integer values only.\nTry Again:\n')
        que4()

def que5():
    a = [1, 11, 111, 1111, 11111]
    b = [2, 22, 222, 2222, 22222]
    return sorted(a + b)

def que6_stack(x):
    a = [1, 2, 11, 22, 111, 222, 1111, 2222, 11111, 22222]
    a.append(x)
    return a.pop()

def que6_queue(x):
    a = [1, 2, 11, 22, 111, 222, 1111, 2222, 11111, 22222]
    a.append(x)
    return a.pop(0)

def main():
    ans1 = que1()
    print(ans1)
    ans2 = que2(ans1)
    print(ans2)
    ans3 = que3(ans2)
    print(ans3)
    ans4 = que4()
    print(ans4)
    ans5 = que5()
    print(ans5)
    ans6_stack = que6_stack(48)
    print(ans6_stack)
    ans6_queue = que6_queue(48)
    print(ans6_queue)

if __name__ == '__main__':
    main()

# amazon flipkart amd intel
# 9 5 6 7 3 8 2 1
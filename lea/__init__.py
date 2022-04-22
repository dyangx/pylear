import requests as requests

import lea
from lea.Coroutine import run
from lea.File import File


def xprinx():
    return 1, 2, 3


def map_func():
    value = map(int, [1, 2, 3])
    print(type(value))
    print(value)


def func2():
    f = lambda x: x + x
    print(f('1234'))


def bb(x):
    def bb2(y):
        return x * y

    return bb2


def count():
    funcs = []
    for f in [1, 2, 3, 4]:
        def func(x):
            val = lambda: x * x
            return val
        funcs.append(func(f))
    return funcs


def count_test():
    f1, f2, f3, f4 = count()
    print(f1())
    print(f2())
    print(f3())
    print(f4())


def func2():
    name = "张三"
    value = "this is %s" % name
    print(value)


def func3():
    nums = (x for x in range(10))
    for i in nums:
        print(i)
    print(range(10))


def func4():
    try:
        x = input("Enter x:")
        y = input("Enter y:")
        print(x/y)
    except ZeroDivisionError as e:
        print(e)
    print("final s")


def func5():
    url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
    r = requests.get(url)
    # print(r.json())
    print(r.json().keys())


if __name__ == '__main__':
    func5()

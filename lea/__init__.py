import json

import pygal
import requests as requests

from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

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
    print(r.status_code)
    return r

def func6():
    with open("C:/Users/ll18/Desktop/sty/test/test.json", 'w',encoding='utf-8') as f:
    # with open("../file/test.json", 'w',encoding='utf-8') as f:
        r = func5()
        # f.write(str(r.json()))
        json.dump(r.json(),f)
        # f.close()
    with open("C:/Users/ll18/Desktop/sty/test/test.json", 'r', encoding='utf-8') as f:
        js = json.load(f)
        print(js)


def func7():
    url = "https://api.github.com/rate_limit"
    r = requests.get(url)
    s = str(r.json()).replace("'","\"")
    print(s)


def img():
    URL = 'https://api.github.com/search/repositories?q=language:python&sort=star'
    r = requests.get(URL)
    print("Status code:", r.status_code)
    response = r.json()
    response_dicts = response['total_count']
    repo_dicts = response['items']

    name,stars = [],[]
    for repo_dict in repo_dicts:
        name.append(repo_dict['name'])
        stars.append(repo_dict['stargazers_count'])
    my_style = LS('#333366', base_style=LCS)
    chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
    chart.title = 'Most-Starred Python Projects on GitHub'
    chart.x_labels = name
    chart.add('', stars)
    chart.render_to_file('../file/python_repos.svg')


if __name__ == '__main__':
    img()

"""
我们可以创建一个输出任意范围内 Fibonacci 数列的函数:
"""

"""
无返回值得
"""


def fib(n):
    """请输入一个数："""
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
    print()


fib(10)  # 0 1 1 2 3 5 8

print(fib)  # <function fib at 0x00000255F93643A8>

"""
有返回值的
"""


def fib1(n):
    """请输入一个数："""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    # 这是需要在循环结束后返回
    return result
    print()


f10 = fib1(10)
print(f10)

"""
最有用的形式是对一个或多个参数指定一个默认值。这样创建的函数，可以用比定义时允许的更少的参数调用，比如:
"""


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


# 使用的是后面两个默认值
# ask_ok('Do you really want to quit?')  # Do you really want to quit?: ?
# ask_ok('OK to overwrite the file?', 2)  # OK to overwrite the file?: ?
ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

"""
默认值只会执行一次。这条规则在默认值为可变对象（列表、字典以及大多数类实例）时很重要。比如，下面的函数会存储在后续调用中传递给它的参数:

[1]
[1, 2]
[1, 2, 3]
"""


def f(a, L=[]):
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))


"""
可以这样写
"""
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

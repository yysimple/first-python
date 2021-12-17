def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


"""
要么全是关键字参数，要么全是占位的方式
"""
# parrot(1000)                                          # 1 positional argument
# parrot(voltage=1000)                                  # 1 keyword argument
# parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
# parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
# parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
# parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword


"""
当存在一个形式为 **name 的最后一个形参时，它会接收一个字典 (参见 映射类型 --- dict)，
其中包含除了与已有形参相对应的关键字参数以外的所有关键字参数。 这可以与一个形式为 *name，
接收一个包含除了已有形参列表以外的位置参数的 元组 的形参 (将在下一小节介绍) 组合使用 (*name 必须出现在 **name 之前。) 
例如，如果我们这样定义一个函数:
"""


def cheeseshop(kind, *args, **keys):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in args:
        print(arg)
    print("-" * 40)
    for key in keys:
        print(key, ":", keys[key])


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

print("-" * 40)


"""
zyy/wcx/ysq
haha.heihei.xixi

"""
def concat(*args, sep="/"):
    return sep.join(args)

str1 = concat("zyy", "wcx", "ysq")
print(str1)

str2 = concat("haha", "heihei", "xixi", sep=".")
print(str2)

list(range(3, 6))            # normal call with separate arguments

"""
当参数已经在列表或元组中但需要为需要单独位置参数的函数调用解包时，
会发生相反的情况。例如，内置的 range() 函数需要单独的 start 和 stop 参数。
如果它们不能单独使用，请使用 * 运算符编写函数调用以从列表或元组中解包参数:
"""
args = [3, 6]
print(list(range(*args)))         # call with arguments unpacked from a list


"""
-- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !
"""
def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)



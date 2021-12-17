
"""
以这种方式进行导入模块，必须用他的全路径才可以用他的方法
"""
# import src.basic_python.module.fibonacci
# print(src.basic_python.module.fibonacci.fib(5))


"""
这也会加载子模块 echo ，并使其在没有包前缀的情况下可用，因此可以按如下方式使用:
"""
# from src.basic_python.module import fibonacci
# print(fibonacci.fib(5))


"""
另一种形式是直接导入所需的函数或变量:
"""
# from src.basic_python.module.fibonacci import fib
# print(fib(10))


"""
如果不在src.basic_python.module这个模块下 指定可以导入的模块 import * 将什么都不会导入

"""
from src.basic_python.module import *
print(fibonacci.fib(5))
print(hello.say_hello("wcx"))
print(world.world())


"""
当在字典中循环时，用 items() 方法可将关键字和对应的值同时取出
gallahad the pure
robin the brave
"""
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)


"""
当同时在两个或更多序列中循环时，可以用 zip() 函数将其内元素一一匹配。

{0}, {1}；两个是占位符
"""
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

"""
消重并排序
"""
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for arg in sorted(set(basket)):
    print(arg)


"""
有时可能会想在循环时修改列表内容，一般来说改为创建一个新列表是比较简单且安全的
"""
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for val in raw_data:
    if not math.isnan(val):
        filtered_data.append(val)

print(filtered_data)  # [56.2, 51.7, 55.3, 52.5, 47.8]

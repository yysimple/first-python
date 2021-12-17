"""
一对花括号可以创建一个空字典：{} 。另一种初始化字典的方式是在一对花括号里放置一些以逗号分隔的键值对，而这也是字典输出的方式。
"""
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel['zyy'] = 1515
print(tel)

print(tel['jack'])

del tel['sape']

print(tel)

# {'jack': 4098, 'guido': 4127, 'zyy': 1515}
print("-" * 40)

# ['jack', 'guido', 'zyy']
print(list(tel))

print(sorted(tel))

'guido' in tel

'jack' not in tel

# 此外，字典推导式可以从任意的键值表达式中创建字典
print({x: x ** 2 for x in (2, 4, 6)})

"""
dict() 构造函数可以直接从键值对序列里创建字典。
"""
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(dict)  # <class 'dict'>

map = dict(sape=4139, guido=4127, jack=4098)
print(map)




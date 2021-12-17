#  ----------- 列表 -------------
# 定义列表
squares = [1, 4, 9, 16, 25]
print(squares)  # [1, 4, 9, 16, 25]
print(squares[0])  # 1
print(squares[:-3])  # [1, 4]
# 所有的切片操作都返回一个新列表，这个新列表包含所需要的元素。就是说，如下的切片会返回列表的一个新的(浅)拷贝:
print(squares[:])
print(squares + [36, 49, 64, 81, 100])  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 与 immutable 的字符串不同, 列表是一个 mutable 类型，就是说，它自己的内容可以改变:
squares[2] = 19
print(squares)  # [1, 4, 19, 16, 25]

squares.append(123)
print(squares)  # [1, 4, 19, 16, 25, 123]

# 给切片赋值也是可以的，这样甚至可以改变列表大小，或者把列表整个清空:
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters[2:5] = ['C', 'D', 'E']
print(letters)  # ['a', 'b', 'C', 'D', 'E', 'f', 'g']
letters[2:5]  # ['a', 'b', 'f', 'g']
letters[:] = []  # []
print(len(letters))  # 0

# 也可以嵌套列表 (创建包含其他列表的列表), 比如说:
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)  # [['a', 'b', 'c'], [1, 2, 3]]
print(x[0])  # ['a', 'b', 'c']
print(x[0][1])  # b




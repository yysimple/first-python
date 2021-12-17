"""
一个元组由几个被逗号隔开的值组成
"""
t = 12345, 54321, 'hello!'
t[0]

print(t)

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u)

# Tuples are immutable:
# t[0] = 88888


# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
print(v)


"""
空元组可以直接被一对空圆括号创建，
含有一个元素的元组可以通过在这个元素后添加一个逗号来构建（圆括号里只有一个值的话不够明确）。丑陋，但是有效。例如
"""
empty = ()
singleton = 'hello',    # <-- note trailing comma
len(empty)

print(len(singleton))

print(singleton)



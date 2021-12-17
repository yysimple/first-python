# ----------------- for ------------------

"""
cat 3
dogs 4
ant 3
"""
animals = ["cat", "dogs", "ant"]
for w in animals:
    print(w, len(w))

"""
['pig', 'cat', 'dogs', 'ant']
"""
for w in animals[:]:  # 如果这里是animals将是无瑕循环
    if len(w) > 3:
        animals.insert(0, "pig")
print(animals)


"""
0 1 2 3 4 5 ....
"""
for num in range(10):
    print(num)
print("-------")

"""
5 6 7 8 9
"""
for num in range(5, 10):
    print(num)

print("-------")

"""
以指定的幅度增加（甚至是负数；有时这也被叫做 '步进'） 0 3 6 9
"""
for num in range(0, 10, 3):
    print(num)

print("-------")

"""
要以序列的索引来迭代，您可以将 range() 和 len() 组合如下:
    0 one
    1 two
    2 three
    3 four
"""
a = ["one", "two", "three", "four"]
for i in range(len(a)):
    print(i, a[i])

"""
range() 所返回的对象在许多方面表现得像一个列表，但实际上却并不是。
此对象会在你迭代它时基于所希望的序列返回连续的项，但它没有真正生成列表，这样就能节省空间。
range(0, 10)
"""
print(range(10))

print(list(range(5)))  # [0, 1, 2, 3, 4]

print(list(range(5, 5)))  # []






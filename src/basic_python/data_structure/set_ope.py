"""
它的基本用法包括成员检测和消除重复元素。
花括号或 set() 函数可以用来创建集合。注意：要创建一个空集合你只能用 set() 而不能用 {}
"""
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed

'orange' in basket                 # True  fast membership testing

'crabgrass' in basket              # False


# Demonstrate set operations on unique letters from two words


"""
{'b', 'c', 'r', 'a', 'd'}
{'b', 'r', 'd'}
{'m', 'b', 'c', 'z', 'r', 'a', 'l', 'd'}
{'c', 'a'}
{'m', 'b', 'r', 'z', 'l', 'd'}
"""
a = set('abracadabra')
b = set('alacazam')
print(a)                                  # unique letters in a

print(a - b)                              # letters in a but not in b

print(a | b)                              # letters in a or b or both

print(a & b)                              # letters in both a and b

print(a ^ b)                              # letters in a or b but not both
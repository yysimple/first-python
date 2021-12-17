fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))  # 2

print(fruits.count('tangerine'))  # 0

print(fruits.index('banana'))  # 3
print(fruits.index('banana', 4))  # 6 Find next banana starting a position 4

fruits.reverse()
print(fruits)

fruits.append('grape')
print(fruits)


fruits.sort()
print(fruits)

print(fruits.pop())



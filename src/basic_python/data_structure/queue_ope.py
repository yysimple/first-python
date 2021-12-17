from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
print(queue)
queue.popleft()                 # The first to arrive now leaves
queue.popleft()                 # The second to arrive now leaves
print(queue)                           # Remaining queue in order of arrival

# 这样x还是会一直存在
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

squares = list(map(lambda x: x**2, range(10)))
print(squares)

"""
前面的 x**2 就是操作， 最后会按着这个操作返回一个新的列表
"""
squares = [x**2 for x in range(10)]
print(squares)

coms = [(x, y) for x in [1, 2, 3] for y in [4, 5, 6] if x != y]
print(coms)

"""
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
"""
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print([[row[i] for row in matrix] for i in range(4)])

print(list(zip(*matrix)))




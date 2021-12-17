import math
print(f"只取pi的后三位： {math.pi: .3f}")

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    # print(f'{name:10} ==> {phone:10d}')
    # name: 后面不能加空格
    print(f"{name:10} ==> {phone:10d}")

animals = 'eels'
print(f'My hovercraft is full of {animals}.')  # My hovercraft is full of eels.
print(f'My hovercraft is full of {animals!r}.')  # My hovercraft is full of 'eels'.

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))


for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))





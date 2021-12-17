"""
2 is a ....
3 is a ....
4 equals 2 * 2
5 is a ....
6 equals 2 * 3
7 is a ....
8 equals 2 * 4
9 equals 3 * 3
当和循环一起使用时，else 子句与 try 语句中的 else 子句的共同点多于 if 语句中的子句: try 语句中的 else 子句会在未发生异常时执行，
而循环中的 else 子句则会在未发生 break 时执行。
"""
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, "equals", x, "*", n // x)
            break
    else:
        print(n, "is a ....")

print("------")

"""
Found an even number 2
Found a number 3
Found an even number 4
Found a number 5
Found an even number 6
Found a number 7
Found an even number 8
Found a number 9
"""
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)

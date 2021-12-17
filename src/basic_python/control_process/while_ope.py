# ----------------- while ------------------
a, b = 0, 1
while a < 10:
    # print(a, end="")  0112358this is a value: 375
    print(a)
    a, b = b, a + b

# 字符串会打印不带引号的内容, 并且在参数项之间会插入一个空格, 这样你就可以很好的把东西格式化, 像这样:
i = 15 * 25
print("this is a value:", i)  # this is a value: 375


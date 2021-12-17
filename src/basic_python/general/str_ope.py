print("\"Yes,\"")  # "Yes,"
print('"has"')  # "has"
#  ----------- 操作字符串 -------------
"""
C:\some
ame

C:\some\name

"""
print('C:\some\name')

print(r'C:\some\name')

"""
字符串字面值可以跨行连续输入。一种方式是用三重引号：
\""" .. \""" 或 '''...'''。字符串中的回车换行会自动包含到字符串中，如果不想包含，在行尾添加一个 \ 即可。如下例:
"""

print("""\
Usage: thingy [OPTIONS] 
     -h \n  Display this usage message                     
     -H hostname               Hostname to connect to
""")

# 字符串可以用 + 进行连接（粘到一起），也可以用 * 进行重复:
print(3 * 'un' + 'ium')  # unununium

# py thon ,:就是一个空格
# 相邻的两个或多个 字符串字面值 （引号引起来的字符）将会自动连接到一起.
print("py", "thon")

# Put several strings within parentheses to have them joined together.  只对字面量有作用 表达式和变量不支持
text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)

word = "python"
print(word[1])  # y 索引从0开始
# print(word[7])  # 超过索引不会输出 IndexError: string index out of range
print(word[-1])  # n
print(word[0:2])  # py
# 意切片的开始总是被包括在结果中，而结束不被包括--> [0:2)。这使得 s[:i] + s[i:] 总是等于 s
print(word[:4] + word[4:])  # python
# 切片中的越界索引会被自动处理:
print(word[4:42])  # on
# Python 中的字符串不能被修改，它们是 immutable 的
print(len(word))  # 6

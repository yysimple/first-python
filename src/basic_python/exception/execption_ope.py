import sys


"""
最后的 except 子句可以省略异常名，以用作通配符。
但请谨慎使用，因为以这种方式很容易掩盖真正的编程错误！
它还可用于打印错误消息，然后重新引发异常（同样允许调用者处理异常）:
"""
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise


"""
try ... except 语句有一个可选的 else 子句，在使用时必须放在所有的 except 子句后面。对于在try 子句不引发异常时必须执行的代码来说很有用。
"""
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()


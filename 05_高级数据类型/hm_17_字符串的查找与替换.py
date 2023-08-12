hello_str = "hello world"

# 1.判断是否以指定字符串开始
print(hello_str.startswith("hello"))

# 2.判断是否以指定字符串结束
print(hello_str.endswith("world"))

# 3.查找指定字符串
# index同样可以查找子字符串在大字符串中的位置
# find查找不到的会返回-1 index查找不到的程序会报错
print(hello_str.find("llo"))
print(hello_str.find("abc"))


# 4.替换字符串
# replace使用后会返回一个新的字符串，但不会改变原来的字符串
print(hello_str.replace("world", "python"))
print(hello_str)


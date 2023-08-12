# 判断空白字符
space_str = "     \r\n"

print(space_str.isspace())

# 判断字符串中是否只包含数字

# 1> 不能判断小数
# num_str = "1.1"
# 2> unicode 字符串
# num_str = "1"
# 3> 中文数字
num_str = "一千零一"
print(num_str)
# 检查一个字符串是否仅有十进制的数字字符构成
# 如果是则返回True 否则返回False
print(num_str.isdecimal())
# 判断单个字符或字符串中是否仅含有数字
print(num_str.isdigit())
# 判断字符串是不是仅含有数字（包括全角书数字和中文数字）
print(num_str.isnumeric())

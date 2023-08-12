# 假设：以下内容是从网络上抓取的
# 要求：1.将字符串中的空白字符全部去掉  2.再使用" "作为分隔符，拼接成一个整齐的字符串

poem = "\t\n登鹤雀楼 王之涣\t 白日依山尽\t\t  黄河入海流\t  欲穷千里目\t  更上一层楼"

print(poem)

# 1.拆分字符串
# split(str = "", num)
# 以str为分隔符拆分string 如果num有指定值 则仅拆分num+1个子字符串
# str默认包含'r' 't' 'n'和空格
poem_list = poem.split()
print(poem_list)
# 2.合并字符串
# string.join(seq)
# 以string为分隔符 把seq中的所有元素合并为一个新的字符串
result = " ".join(poem_list)
print(result)

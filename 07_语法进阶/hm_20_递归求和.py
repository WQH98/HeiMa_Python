# 1 定义一个函数sum_numbers
# 2 能够接收一个num的整数参数
# 3 计算1+2+...+num的结果

def sum_numbers(num):

    if num == 1:
        return 1

    num += sum_numbers(num - 1)
    return num


print(sum_numbers(100))

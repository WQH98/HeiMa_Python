for num in [1, 2, 3]:

    print(num)

    if num == 2:
        break
    # 如果循环体内部使用break退出了循环 else下方的程序则不会执行

else:
    print("else")

print("finish")
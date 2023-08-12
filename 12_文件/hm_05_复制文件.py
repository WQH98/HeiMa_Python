# 打开文件
file_read = open("README")
file_write = open("README[复件]", "w")

# 读写操作
text = file_read.read()
file_write.write(text)

# 关闭文件
file_read.close()
file_write.close()

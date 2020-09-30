# 一个简单的加法器
a = input('请输入第一个数:')
b = input('请输入第二个数:')

try:
    a = int(a)
    b = int(b)
except:
    a = input('请输入第一个数:')
    b = input('请输入第二个数:')

print("两数之和：",a+b)

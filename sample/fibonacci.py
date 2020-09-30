num = 50
a = 0
b = 1
#斐波那契数列 
#前两个数相加等于下一个数
for i in range(num):
    c = a + b
    a = b
    b = c 
    print(c)
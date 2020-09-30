num = 50
a = 0
b = 1
step = 0
#斐波那契数列 
#前两个数相加等于下一个数
for i in range(num):
    c = a + b
    a = b
    b = c
    step += 1
    print(c)
    print('已循环次数:',step)
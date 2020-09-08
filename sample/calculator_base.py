a = int(input('a:'))
b = int(input('b:'))
arithmetic = input("运算符")

if arithmetic == "+":
    print(a+b)
elif arithmetic =="-":
    print(a-b)
elif arithmetic == "*":
    print(a*b)
elif arithmetic == "/":
    print(a/b)
else:
    print("非法输入")


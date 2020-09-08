ctr = True

while ctr:
    a = int(input("a "))
    b = int(input("b "))
    arithmetic = input("运算符 ")
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
    ctr = True if input("输入任意键继续或输入exit退出\n")!="exit" else False
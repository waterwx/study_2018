i = 1
num = int(input("请输入你的需要的行数：")) + 1
while i<=num:

    j = 1
    while j<=num-i:
        print("*", end="")
        j += 1
    print("")
    i += 1


sex = input("请输入你的性别：")

if sex == "女":
    color = input("你白么？")
    money = int(input("请输入你的财产综合:"))
    beautiful = input("你美么？")

    if color == "白" and money>100000 and beautiful == "美":
        print("白富美。。。。")
    else:
        print("矮挫穷......")

else:
    height = input("你高么？")
    money = int(input("请输入你的财产总和？"))
    beautiful = input("你帅么？")
    if height == "高" and money >=100000 and beautiful == "帅":
        print("高富帅。。。。。")
    else:
        print("矮挫穷......")

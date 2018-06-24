ticket = int(input("获取车票信息，1表示有票；0表示无票：")) # 1表示有车票 0表示没有车票
knifeLenght = int(input("获取刀的长度单位cm：")) #cm

# 先判断是否有车票
if ticket == 1:
    print("通过了车票的检查，进入了车站，接下来要安检了")

    # 判断刀的长度是否合规
    if knifeLenght <= 10:
        print("通过了安检，进入了候车厅")
        print("马上就要见到TA了,很开心。。。。。。")
    else:
        print("安检没有通过，等待公安处理。。。。。")
else:
    print("兄弟你还没有票呢，先去买票，才能进站。。。。")



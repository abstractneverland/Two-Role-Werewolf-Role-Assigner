import random
def Six():
    List = ["狼人", "隐狼", "预言家", "女巫", "猎人", "守卫", "盗贼", "平民", "平民", "平民", "平民", "平民"]
    flag = False
    while flag == False:
        for i in range(12):
            num = random.randint(0, 11 - i) + i
            temp = List[i]
            List[i] = List[num]
            List[num] = temp
        flag_1 = True
        for i in range(6):
            if List[2 * i] == "预言家" and List[2 * i + 1] == "狼人":
                flag_1 = False
            if List[2 * i] == "预言家" and List[2 * i + 1] == "隐狼":
                flag_1 = False
            if List[2 * i] == "狼人" and List[2 * i + 1] == "预言家":
                flag_1 = False
            if List[2 * i] == "隐狼" and List[2 * i + 1] == "预言家":
                flag_1 = False
            if List[2 * i] == "平民" and List[2 * i + 1] == "平民":
                flag = True
            if List[2 * i] == "盗贼" and List[2 * i + 1] == "平民":
                flag = True
            if List[2 * i] == "平民" and List[2 * i + 1] == "盗贼":
                flag = True
        if flag_1 == False:
            flag = False
    for i in range(6):
        for j in range(100):
            print("请按Enter查看身份。")
        input("请按Enter查看身份。")
        print(f"你是{List[2 * i]}和{List[2 * i + 1]}。")
        input("请离开前按Enter，防止下一位玩家窥见身份。")
    for i in range(100):
        print("请按Enter查看身份。")
    for i in range(5):
        input()
    for i in range(6):
        print(List[2 * i], List[2 * i + 1])
def Eight():
    List = ["狼人", "狼人", "隐狼", "预言家", "女巫", "猎人", "守卫", "白痴", "禁言长老", "盗贼", "平民", "平民", "平民", "平民", "平民", "平民"]
    flag = False
    while flag == False:
        for i in range(16):
            num = random.randint(0, 15 - i) + i
            temp = List[i]
            List[i] = List[num]
            List[num] = temp
        flag_1 = True
        for i in range(8):
            if List[2 * i] == "预言家" and List[2 * i + 1] == "狼人":
                flag_1 = False
            if List[2 * i] == "预言家" and List[2 * i + 1] == "隐狼":
                flag_1 = False
            if List[2 * i] == "狼人" and List[2 * i + 1] == "预言家":
                flag_1 = False
            if List[2 * i] == "隐狼" and List[2 * i + 1] == "预言家":
                flag_1 = False
            if List[2 * i] == "平民" and List[2 * i + 1] == "平民":
                flag = True
            if List[2 * i] == "盗贼" and List[2 * i + 1] == "平民":
                flag = True
            if List[2 * i] == "平民" and List[2 * i + 1] == "盗贼":
                flag = True
        if flag_1 == False:
            flag = False
    for i in range(8):
        for j in range(100):
            print("请按Enter查看身份。")
        input("请按Enter查看身份。")
        print(f"你是{List[2 * i]}和{List[2 * i + 1]}。")
        input("请离开前按Enter，防止下一位玩家窥见身份。")
    for i in range(100):
        print("请按Enter查看身份。")
    for i in range(5):
        input()
    for i in range(8):
        print(List[2 * i], List[2 * i + 1])
n = int(input("请输入游戏人数。\n"))
if n == 6:
    Six()
if n == 8:
    Eight()
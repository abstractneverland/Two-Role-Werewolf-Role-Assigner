import random
def Six():
    List = ["Werewolf", "Hidden Werewolf", "Prophet", "Witch", "Hunter", "Guard", "Duplicate", "Villager", "Villager", "Villager", "Villager", "Villager"]
    flag = False
    while flag == False:
        for i in range(12):
            num = random.randint(0, 11 - i) + i
            temp = List[i]
            List[i] = List[num]
            List[num] = temp
        flag_1 = True
        for i in range(6):
            if List[2 * i] == "Prophet" and List[2 * i + 1] == "Werewolf":
                flag_1 = False
            if List[2 * i] == "Prophet" and List[2 * i + 1] == "Hidden Werewolf":
                flag_1 = False
            if List[2 * i] == "Werewolf" and List[2 * i + 1] == "Prophet":
                flag_1 = False
            if List[2 * i] == "Hidden Werewolf" and List[2 * i + 1] == "Prophet":
                flag_1 = False
            if List[2 * i] == "Villager" and List[2 * i + 1] == "Villager":
                flag = True
            if List[2 * i] == "Duplicate" and List[2 * i + 1] == "Villager":
                flag = True
            if List[2 * i] == "Villager" and List[2 * i + 1] == "Duplicate":
                flag = True
        if flag_1 == False:
            flag = False
    for i in range(6):
        for j in range(100):
            print("Please check your identities by pressing Enter.")
        input("Please check your identities by pressing Enter.")
        print(f"You are the {List[2 * i]} and the {List[2 * i + 1]}.")
        input("Please press Enter before you leave.")
    for i in range(100):
        print("Please check your identities by pressing Enter.")
    for i in range(5):
        input()
    for i in range(6):
        print(List[2 * i], List[2 * i + 1])
def Eight():
    List = ["Werewolf", "Werewolf", "Hidden Werewolf", "Prophet", "Witch", "Hunter", "Guard", "Idiot", "Silencer", "Duplicate", "Villager", "Villager", "Villager", "Villager", "Villager", "Villager"]
    flag = False
    while flag == False:
        for i in range(16):
            num = random.randint(0, 15 - i) + i
            temp = List[i]
            List[i] = List[num]
            List[num] = temp
        flag_1 = True
        for i in range(8):
            if List[2 * i] == "Prophet" and List[2 * i + 1] == "Werewolf":
                flag_1 = False
            if List[2 * i] == "Prophet" and List[2 * i + 1] == "Hidden Werewolf":
                flag_1 = False
            if List[2 * i] == "Werewolf" and List[2 * i + 1] == "Prophet":
                flag_1 = False
            if List[2 * i] == "Hidden Werewolf" and List[2 * i + 1] == "Prophet":
                flag_1 = False
            if List[2 * i] == "Villager" and List[2 * i + 1] == "Villager":
                flag = True
            if List[2 * i] == "Duplicate" and List[2 * i + 1] == "Villager":
                flag = True
            if List[2 * i] == "Villager" and List[2 * i + 1] == "Duplicate":
                flag = True
        if flag_1 == False:
            flag = False
    for i in range(8):
        for j in range(100):
            print("Please check your identities by pressing Enter.")
        input("Please check your identities by pressing Enter.")
        print(f"You are the {List[2 * i]} and the {List[2 * i + 1]}.")
        input("Please press Enter before you leave.")
    for i in range(100):
        print("Please check your identities by pressing Enter.")
    for i in range(5):
        input()
    for i in range(8):
        print(List[2 * i], List[2 * i + 1])
n = int(input("Please input the number of players.\n"))
if n == 6:
    Six()
if n == 8:
    Eight()
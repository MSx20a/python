row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
counter = 0


def display():
    """
    顯示此三個陣列
    """
    print(row1)
    print(row2)
    print(row3)


def usr_choice():
    """
    判斷使用者輸入的值是否有在範圍內
    """
    choice = input("Please input a number range 1 to 9:")
    while not choice.isdigit() or (int(choice) not in range(1, 10)):
        if not choice.isdigit():
            print("Sorry,you choice not a valid.")
        else:
            print("You choice is not within range of 1 to 9.")
        choice = input("Please input a number range 1 to 9:")
    return int(choice)

# usr_choice()


def OX_control():
    """
    設定第一次輸入＝“O”,第二次輸入＝“X”,第三次輸入＝“O”......以此類推
    """
    global counter  # 讓函式外counter的值能隨著執行次數+1
    mylist = ["X", "O"]
    counter += 1
    return mylist[counter % 2]  # 1%2=1

# print(OX_control())
# print(OX_control())


def update_table(index: int):
    """
    會將使用者輸入的數字轉換成九宮格相對應的位置將O,X放入row1,row2,row3中
    """
    global row1, row2, row3
    if index in range(1, 4):
        if row1[index-1]==" ":   #判斷只有空的位置才能放入O,X
            row1[index-1] = OX_control()
            return True
        else:
            return False
    elif index in range(4, 7):
        if row2[index % 3-1]==" ":
            row2[index % 3-1] = OX_control()  # 4,5,6除三取餘數並減1=0,1,-1剛好對應row2的0,1,2
            return True
        else:
            return False
    else:
        if row3[index % 3-1]==" ":
            row3[index % 3-1] = OX_control()  # 原因同上
            return True
        else:
            return False
# update_table(1)
# update_table(2)
# update_table(8)
# update_table(3)
# update_table(7)
# update_table(6)
# display()


def check_win():
    """
    判斷誰是贏家，把圈圈叉叉的所有贏的可能寫下來
    橫的三種
    直的三種
    對角斜線的兩種
    平局
    """
    player_1_win = False
    player_2_win = False
    if row1[0] == row1[1] == row1[2] and (row1[0], row1[1], row1[2] != " "):
        if row1[0] == "O":
            player_1_win = True
        else:
            player_2_win = True
    elif row2[0] == row2[1] == row2[2] and (row2[0], row2[1], row3[2] != " "):
        if row2[0] == "O":
            player_1_win = True
        else:
            player_2_win = True
    elif row3[0] == row3[1] == row3[2] and (row3[0], row3[1], row3[2] != " "):
        if row3[0] == "O":
            player_1_win = True
        else:
            player_2_win = True
    elif row1[0] == row2[0] == row3[0] and (row1[0], row2[0], row3[2] != " "):
        if row1[0] == "O":
            player_1_win = True
        else:
            player_2_win = True
    elif row1[1] == row2[1] == row3[1] and (row1[1], row2[1], row3[1] != " "):
        if row1[1] == "O":
            player_1_win = True
        else:
            player_2_win = True
    elif row1[2] == row2[2] == row3[2] and (row1[2], row2[2], row3[2] != " "):
        if row1[2] == "O":
            player_1_win = True
        else:
            player_2_win = True
    elif row1[0] == row2[1] == row3[2] and (row1[0], row2[1], row3[2] != " "):
        if row1[0] == "O":
            player_1_win = True
        else:
            player_2_win = True
    elif row1[2] == row2[1] == row3[0] and (row1[2], row2[1], row3[0] != " "):
        if row1[2] == "O":
            player_1_win = True
        else:
            player_2_win = True
    if player_1_win:
        return "player1 is winner."
    elif player_2_win:
        return "player2 is winner."
    else:
        return "no one win."

# def start_game():
#     """
#     將ox_setting寫好的函式引用過來並執行
#     """
#     while True:
#         display()
#         choice=usr_choice()
#         update_table(choice)
#         result=check_win()
#         return result

# start_game()

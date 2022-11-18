import ox_setting


def start_game():
    """
    將ox_setting寫好的函式引用過來並執行
    """
    while True:
        print("playing now....")
        ox_setting.display()
        while True:
            choice = ox_setting.usr_choice()
            if ox_setting.update_table(choice):
                break
            else:
                print("Input position error!!")
        result = ox_setting.check_win()
        return result
        # if result=="player1 is winner.":
        #     return "Congratulations,player1 !!"
        # elif result=="player2 is winner.":
        #     return "Congratulations,player2 !!"


start_game()
print(bool(start_game))
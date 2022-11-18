name = input("Enter your name: ")  # only get string
money = input("Enter your cash: ")  # only get string
hungry = input("Are you hungry:(Y/N) ")  # nly get string

if hungry.upper() == "Y":
    if int(money) >= 100:  # 得到的money是string要轉換成integer才能做比較大小
        print(f"{name} can eat hamburger.")
    elif 100 > int(money) >= 50:
        print(f"{name} can eat sandwich.")
    else:
        print(f"{name} can eat Chinese omelet.")
elif hungry.upper() == "N":
    print(f"{name} are no hungry.")
else:
    print("Plase input Y or N.")

print("-------------------------------")


# in Python 比較True or Flase不會使用"==",而是會照以下寫法
x = True
if x:
    print("I am X police.")
else:
    print("I am a losser.")
y = False
if not y:
    print("Go home sleeping.")
else:
    print("I am a sun boy.")

print("-------------------------------")


cmd = input("Give a command:")
# membership operator(return bool)
if cmd in ("cd", "ls", "dir"):
    print(f"{cmd} is valid command.")
else:
    print(f"{cmd} is invalid command.")

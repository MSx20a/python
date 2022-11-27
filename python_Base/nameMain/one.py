# 在one.py執行one.py此時__name__=__main__
# 將one.py import至two.py此時__name__=one(檔名)
# if __name__ == "__main__"可以控制直接執行或者是被import所要做的行為

def a():
    print("This is one by a.")


def c():
    print("This is one by c.")


if __name__ == "__main__":
    a()
    print(__name__)
else:
    print(f"This is from {__name__}.")

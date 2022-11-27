# 在two.py執行two.py此時__name__=__main__
# 此時one.py的__name__=one
# if __name__ == "__main__"可以控制直接執行或者是被import所要做的行為
import one

one.c()


def b():
    print("This is two.")


if __name__ == "__main__":
    b()
    print(__name__)
else:
    print(f"This is from {__name__}.")

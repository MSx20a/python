# python處理例外的語法

def operation1():
    """
    基本運算
    """
    try:
        result = 10+10
    except:
        print("type error")
    finally:
        # finally底下的code不管有沒有出現例外都會執行
        print(result)


# operation1()


def file_control():
    """
    寫入讀取文件
    """
    try:
        with open("myfile.txt", mode="w") as x:
            f = x.write("Neo Cafe.")  # f＝寫入多少字元
    except TypeError as e:
        print(e)
    except OSError as e:
        # 文件不存在時會跳出OSError
        # as後加上一個varible可以將python內建給user的錯誤訊息顯示出來
        print(e)
    except:
        print("other Error!")
    else:
        # else底下的code在沒有出現例外的情況下才會執行
        print(f"{x.name} is write scuess!!")


# file_control()


def hello():
    """
    演示ecursionError（遞迴錯誤）
    """
    try:
        print("hello")
        hello()
    except RecursionError as e:
        # 當遞迴出現stack overfloat會發生遞迴錯誤
        print(e)

# hello()


# 在python中所有的exceprion都是一個class，因此用class來設計我們的exceprion
# 繼承BaseException，詳細可至https://docs.python.org/3/library/exceptions.html
class NegativeNumberExceprion(BaseException):
    def __init__(self, age) -> None:
        super().__init__()
        self.age = age
        if age < 0:
            print("error age.")


def input_age(age):
    if age < 0:
        # raise關鍵字可以擲出我們設定好的例外錯誤，並且會停執行之後的程式碼
        raise NegativeNumberExceprion(age)
    else:
        print(f"You're {age} years old.")


def result():
    try:
        input_age(50)
    except TypeError as e:
        print(e)
    except:
        print("other error")


# result()


# pythonic的作法，可以提高code的可閱讀性
def division(a, b):
    if type(a) != int or type(b) != int:
        raise ValueError("Not valid type given!")
    if b == 0:
        raise ZeroDivisionError("Second argument con not be 0!")
    return a/b


# raise擲出的異常會被try捕獲並交由except處理
try:
    # print(division(10,0))
    # print(division("10",2))
    print(division(10, 2))
except Exception as e:
    print(e)

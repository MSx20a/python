class Banks():
    """
    計算客戶在銀行內的存款
    """
    bankName = "Taipei Bank"  # Class Attribute(定義屬性)，也可以在初始化內定義但會比較吃記憶體

    def motto(self):  # 定義方法
        return "以客為尊"
    # 私有屬性：物件名稱.__類別名稱；可以預防被從class外更改值
    # 每次執行此class都會先執行__init__，且self代表this

    def __init__(self, userName, money) -> None:  # 初始化方法
        self.__name = userName  # 設定存款者
        self.__balance = money  # 設定存款金額

    def get_userName(self):
        return self.__name

    def get_balance(self):
        return self.__balance

    def saveMoney(self, money: int):
        """
        money：要存入的金額
        """
        self.__balance += money
        return (f"存款{money}完成.現有存款：{self.__balance}")

    def withdraw_money(self, money: int):
        """
        money：要提領的金額
        """
        self.__balance -= money
        return (f"提款{money}完成.現有餘額：{self.__balance}")


userBank = Banks("Alvin", 1500)  # 定義物件userBank
print(userBank.__doc__)  # 可以查看此class的註解內容
#  如果要呼叫class內的屬性用此發法比較好，以防更改class名稱時需要一起修改
print("目前服務銀行是：", userBank.__class__.bankName)
print("銀行服務理念是：", userBank.motto())
print(f"{userBank.get_userName()}有{userBank.get_balance()}的存款.")
print(userBank.saveMoney(50000))
print(userBank.withdraw_money(10760))
print(type(userBank))
print("------------------------------------")


class Scooter():
    """
      改車參數
    """

    def __init__(self, srefit, sHp, sKgm, sWeight) -> None:
        self.sName = "Racings"
        self.refit = srefit
        self.hp = sHp
        self.kgm = sKgm
        self.weight = sWeight
        self.manufacturer = "Kymco"

    def choose(self):
        print(f"是否有改裝:{self.refit}")

    def power_h(self):
        print(f"馬力：{self.hp},")

    def power_k(self):
        print(f"扭力：{self.kgm},")

    def equipment_w(self):
        print(f"裝備重：{self.weight}.")


RCS = Scooter("Yes", 19.24, 1.47, "130kg")
print(f"製造商：{RCS.manufacturer},")  # 輸出已經設定好的值
print(f"重機名稱：{RCS.sName},")
RCS.choose()
RCS.power_h()
RCS.power_k()
RCS.equipment_w()
print("------------------------------------")


class exchange():
    """
    私有屬性(Private Attribute)：物件名稱.__類別名稱；可以預防被從class外更改值
    私有函式(Private Method)：要在method前加上__即可；可以避免從class呼叫此函式
    """

    def __init__(self, r: float, s: float) -> None:
        self.__rate = r  # 設定匯率（private）
        self.__serviceCharge = s  # 設定手續費(private)

    def __cal_rate(self, usa_d: int):
        return int(self.__rate*usa_d*(1-self.__serviceCharge))

    def usa_to_Taiwan(self, usa_d: int):
        result = self.__cal_rate(usa_d)
        return result


x = exchange(32, 0.02)
# x.__cal_rate(8000),此函式是私有函式直接呼叫會出現error
usDallor = 8000
print(f"{usDallor}美元可以換{x.usa_to_Taiwan(usDallor)}台幣.")
print("------------------------------------")


class Score():
    """
    使用getter和setter的方法來獲取私有屬性(Private Attribute)
    """

    def __init__(self, score) -> None:
        self.__score = score

    # getter：獲取數屬性值函數
    def getScore(self):
        print(f"This is 'getScore':{self.__score}.")
        # return self.__score

    # setter：設定屬性值函數
    def setScore(self, new_score):
        if new_score > 0 and new_score < 100:
            self.__score = new_score
            print(f"This is 'setScore':{self.__score}.")
        else:
            print("New score setting invalid.")
       # return self.__score

    # Python style: 新屬性式＝property(getter,[setter,[fdel,[doc]]])
    sc = property(getScore, setScore)


stu = Score(0)
print(stu.sc)
stu.sc = 80
print("------------------------------------")


class Circle():
    """
    計算圓面積
    """
    PI = 3.141596
    all_circle = []

    def __init__(self, r) -> None:
        self.r = r
        self.__class__.all_circle.append(self)

    def area(self):
        return self.__class__.PI*(self.r**2)

    @staticmethod
    def total_area1():
        total = 0
        for i in Circle.all_circle:
            total += i.area()  # 迴圈裡的i指的是area的記憶體位置<__main__.Circle object at 0x7f832c608820>；要把值抓出來才能做運算
        return total

    # cls=Circle
    @classmethod
    def total_area2(cls):
        total = 0
        for i in cls.all_circle:
            total += i.area()  # 迴圈裡的i指的是area的記憶體位置<__main__.Circle object at 0x7f832c608820>；要把值抓出來才能做運算
        return total


c = Circle(5)
print(c.total_area1())
print(c.total_area2())
print("------------------------------------")


class People():
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")


class Stduent(People):  # inheritance 繼承
    def __init__(self, name, age, id) -> None:
        super().__init__(name, age)
        self.id = id

    def run(self):
        print(f"{self.name} can run.")


class English_teacher(People):   # inheritance 繼承
    def __init__(self, name, age) -> None:
        super().__init__(name, age)

    def teaching(self):
        print(f"{self.name} is understand English very well.")


sdt1 = Stduent("Alvin", 30, 60401)
thr1 = English_teacher("Timmy", 32)
print(sdt1.eat)
sdt1.eat()
thr1.teaching()
print("------------------------------------")


class Employee():
    """
    虛擬屬性@property的用法
    """

    def __init__(self) -> None:
        self.income = 0

    def earn_money(self, money):
        self.income += money

    @property
    def tax_amount(self):
        return self.income*0.005

    # tax_amount屬於Employee的屬性，所以也可以設定他的值
    @tax_amount.setter
    def amount(self, tax_money):
        self.income = tax_money*200


m = Employee()
m.earn_money(50000)
print(int(m.tax_amount))  # @property會讓底下設置function轉成虛擬的propert
m.amount = 600
print(m.income)  # setter會將incomee由50000改成120000
print("------------------------------------")


class Gundam():
    """
    __hash__:在object中如果有此函式，那此object就可以被當做dict的key
    __eq__：會在2個object有做比較時，去尋找object內是否有此函式，用法如下
    1.先檢查class是否相同
    2.檢查key是否相同
    __str__：可以在內部添加對於此object的描述（給使用者看的）
    __repr__：用來給開發者debug用的
    """

    def __init__(self, name, id, hight, weight) -> None:
        self.name = name
        self.id = id
        self.hight = hight
        self.wight = weight

    def __key(self):
        return (self.name, self.id, self.hight, self.wight)  # 用tuple的格式回傳

    def __hash__(self) -> int:
        return hash(self.__key())  # hash會回傳物件記憶體位置，且要帶入的資料格式為tuple

    def __eq__(self, other) -> bool:  # other指的是要被比較的object
        if isinstance(other, Gundam):  # isinstance：可以判斷事否為Gundam object
            return self.__key() == other.__key()  # 比較2個tuple內的key是否相同

    def __str__(self) -> str:
        return f"{self.name} Gundam為日本電視動畫《機動戰士鋼彈SEED》系列中登場，虛構的有人式人型機器兵器（MS），主角煌·大和於故事後半搭乘之座機。機體名「Freedom」為英語的「自由」之意，機體設計為大河原邦男"

    def __repr__(self) -> str:
        return f"name:{self.name},id:{self.id},hight:{self.hight},wight:{self.wight}"


g1 = Gundam("Freedom", "ZGMF-X10A", 18.03, 71.5)
g2 = Gundam("Justice", "ZGMF-X09A", 18.56, 75.4)
g3 = Gundam("Freedom", "ZGMF-X10A", 18.03, 71.5)

print(g1.__hash__)
print(g1)
print(repr(g1))
print(g1 == g2)
print(g1 == g3)

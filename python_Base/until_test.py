# unittest介紹
# 以下code可以協助測試up()執行結果是否有符合預期

import unittest


def up(text: str):
    return text.title()  # title()函式可以讓字串以標題的格式呈現

    # 補充有一個和title()很像的函式capitalize()，他的功能是只讓字串的開頭第一個字母變成大寫


print(up("how are you !!"))


class MyTest(unittest.TestCase):
    def test_one(self):
        text = "small"
        r = up(text)
        self.assertAlmostEqual(r, "Small")  # 會比較此2參數的直是否相等

    def test_ewo(self):
        text = "bigger one"
        r = up(text)
        self.assertAlmostEqual(r, "Bigger One")


if __name__ == "__main__":
    unittest.main()  # 此行會直接執行class內的test_one,test_two

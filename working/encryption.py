# from datetime import datetime
# import pytz
from pprint import pprint
import hashlib
import rsa


class PayEncry():
    """請求加密"""

    def __init__(self, paraMeter: dict, key: str) -> None:
        """初始化參數

        Args:
            paraMeter (dict): 請求傳參，以dict傳送
            key (str): 金鑰
        """
        self.paraMeter = paraMeter
        self.key = key

    def body(self):
        """

        Returns:
            _type_: _description_
        """
        newPmDict = {}
        for key, value in self.paraMeter.items():
            if value:
                newPmDict[key] = value
        sortPmDict = dict(sorted(newPmDict.items()))
        return sortPmDict

    def payMd5(self):
        concatenationParameter = ""
        for key, value in self.body().items():
            concatenationParameter += f"{key}={value}&"
        sign = f"{concatenationParameter[:-1]}{self.key}"
        md5 = hashlib.md5()
        md5.update(sign.encode('utf-8'))
        result = md5.hexdigest().upper()
        # pprint(sign)
        # pprint(result)
        return result

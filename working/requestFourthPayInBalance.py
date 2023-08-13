import requests
from datetime import datetime
import pytz
import os
from datetime import datetime
from dotenv import load_dotenv
from pprint import pprint
from encryption import PayEncry

load_dotenv()
domain = os.getenv("fourthDomain")
key = os.getenv("key_PayIn")


def queryBalance(merchantNo: str, channelCode: str):
    """
    查詢商戶通道的餘額

    Args:
        merchantNo (str): 商戶號;
        channelCode (str): 通道編碼;

    Returns:
        dict: 查詢結果
    """
    pmbody = {
        "merchantNo": merchantNo,
        "channelCode": channelCode,
        "timestamp": datetime.now(pytz.timezone(
            "UTC")).isoformat(timespec='milliseconds').replace("+00:00", "Z"),
    }

    x = PayEncry(pmbody, key)
    sign = x.payMd5()
    body = x.body()
    body["sign"] = sign
    print("body：")
    pprint(body)

    header = {"Content-Type": "application/json", "charset": "utf-8"}
    response = requests.post(
        f"https://{domain}/api/payin/balance", json=body, headers=header)
    if response.status_code == 200:
        # print("response：")
        # pprint(response.json())
        return response.json()
    else:
        print("錯誤訊息：")
        pprint(response.text)


if __name__=="__main__":
    queryBalance("MA323080409512810340109637","LinePay1")

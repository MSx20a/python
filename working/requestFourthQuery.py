import requests
from datetime import datetime
import pytz
import os
from datetime import datetime
from dotenv import load_dotenv
from pprint import pprint
from encryption import PayEncry
import time

load_dotenv()
domain = os.getenv("fourthDomain")
key = os.getenv("key_PayIn")


def query(merchantNo:str, transactionNumber:str,j:int):
    data = {}
    data["merchantNo"] = merchantNo
    data["transactionNumber"] = transactionNumber
    data["timestamp"] = datetime.now(pytz.timezone("UTC")).isoformat(
        timespec='milliseconds').replace("+00:00", "Z")
    x = PayEncry(data, key)
    qsSgin = x.payMd5()
    qsBody = x.body()
    qsBody["sign"] = qsSgin
    i = 0
    while i < j:
        print("查詢訂單狀態：")
        print("body：")
        pprint(qsBody)
        qsHeader = {"Content-Type": "application/json", "charset": "utf-8"}
        qsResponse = requests.post(
            f"https://{domain}/api/payin/query", json=qsBody, headers=qsHeader)
        if qsResponse.status_code == 200:
            print("response：")
            qsResponseDict = qsResponse.json()
            pprint(qsResponseDict)
            if qsResponseDict["data"]["orderStatus"] == "Succes":
                break
            elif qsResponseDict["data"]["orderStatus"] == "Fail":
                break
        else:
            print("錯誤訊息：")
            print(qsResponse.status_code)
            pprint(qsResponse.text)
        time.sleep(5)
        i += 1

query("MA323060508111811855758946","T230804064304A300258894276")
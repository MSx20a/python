import requests
from datetime import datetime
import pytz
import os
from dotenv import load_dotenv
from pprint import pprint
from encryption import PayEncry
import time



load_dotenv()
domain = os.getenv("fourthDomain")
key = os.getenv("key_PayIn")

pmDict = {
    "merchantNo": os.getenv("merchantNo_PayIn"),
    "orderNumber": f"PP-{datetime.now().strftime('%Y%m%d%H%M%S')}",
    "channelCode": os.getenv("channelCode_PayIn"),
    "orderAmount": os.getenv("orderAmount_PayIn"),
    "customNo": os.getenv("customNo_PayIn"),
    "customName": os.getenv("customName_PayIn"),
    "bankCode": os.getenv("bankCode_PayIn"),
    "redirectUrl": os.getenv("redirectUrl_PayIn"),
    "callbackUrl": os.getenv("callbackUrl_PayIn"),
    "timestamp": datetime.now(pytz.timezone(
        "UTC")).isoformat(timespec='milliseconds').replace("+00:00", "Z")
}

x = PayEncry(pmDict, key)
sign = x.payMd5()
# print(sign)
body = x.body()    
body["sign"] = sign
print("body:")
pprint(body)
header = {"Content-Type": "application/json", "charset": "utf-8"}
response = requests.post(
    f"https://{domain}/api/payin", json=body, headers=header)
if response.status_code == 200:
    print("response:")
    responseData=response.json()
    pprint(responseData)
    time.sleep(5)
    i = 0
    while i<10:
        pmQuery = {
            "merchantNo": os.getenv("merchantNo_PayIn"),
            "transactionNumber": responseData["data"]["transactionNumber"],
            "timestamp": datetime.now(pytz.timezone("UTC")).isoformat(timespec='milliseconds').replace("+00:00", "Z")
        }
        y = PayEncry(pmQuery, key)
        qsSign = y.payMd5()
        qsBody = y.body()
        qsBody["sign"] = qsSign
        print("查詢訂單狀態：")
        print("body：")
        pprint(qsBody)
        qsHeader = {"Content-Type": "application/json", "charset": "utf-8"}
        qsResponse = requests.post(
            f"https://{domain}/api/payin/query", json=qsBody, headers=qsHeader)
        if qsResponse.status_code == 200:
            print("response：")
            qsResponseDict=qsResponse.json()
            pprint(qsResponseDict)
            if qsResponseDict["data"]["orderStatus"]=="Succes":
                break
            elif qsResponseDict["data"]["orderStatus"]=="Fail":
                break
        else:
            print("錯誤訊息：")
            print(qsResponse.status_code)
            pprint(qsResponse.text)
        time.sleep(2)
        i+=1
else:
    print("錯誤訊息:")
    print(response.text)

# , "__tenant": os.getenv("tenantId_PayIn")

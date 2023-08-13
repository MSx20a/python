import requests
from datetime import datetime
import pytz
import os
import time
from dotenv import load_dotenv
from pprint import pprint
from encryption import PayEncry
from requestFourthPayInBalance import queryBalance
from requestFourthQuery import query

load_dotenv()
domain = os.getenv("fourthDomain")
key = os.getenv("key_PayOut")

pmDict = {
    "merchantNo": os.getenv("merchantNo_PayOut"),
    "channelCode": os.getenv("channelCode_PayOut"),
    "orderNumber": f"PP-{datetime.now().strftime('%Y%m%d%H%M%S')}",
    "orderAmount": os.getenv("orderAmount_PayOut"),
    "bankCode": os.getenv("bankCode_PayOut"),
    "bankAccountName": os.getenv("bankAccountName_PayOut"),
    "bankAccountNumber": os.getenv("bankAccountNumber_PayOut"),
    "bankBranchName": os.getenv("bankBranchName_PayOut"),
    "phone": os.getenv("phone_PayOut"),
    "timestamp": datetime.now(pytz.timezone(
        "UTC")).isoformat(timespec='milliseconds').replace("+00:00", "Z"),
    "callbackUrl": os.getenv("callbackUrl_PayOut"),
}

channelBalance = queryBalance(
    os.getenv("merchantNo_PayOut"), os.getenv("channelCode_PayOut"))
availableBalance = channelBalance["data"]["availableBalance"]
print(f"可用餘額：{availableBalance}")

if float(pmDict["orderAmount"]) < float(channelBalance["data"]["availableBalance"]):
    x = PayEncry(pmDict, key)
    sign = x.payMd5()
    body = x.body()
    body["sign"] = sign
    print("body:")
    pprint(body)
    header = {"Content-Type": "application/json", "charset": "utf-8"}
    response = requests.post(
        f"https://{domain}/api/payout", json=body, headers=header)
    if response.status_code == 200:
        print("response:")
        responseData = response.json()
        pprint(responseData)
        time.sleep(5)
        query(os.getenv("merchantNo_PayOut"),
              responseData["data"]["transactionNumber"], 3)  # 查詢訂單
else:
    spread = float(pmDict['orderAmount']) - \
        float(channelBalance['data']['availableBalance'])
    print(f"{pmDict['channelCode']}通道餘額只剩{availableBalance}不足出款，請再加值{spread}")
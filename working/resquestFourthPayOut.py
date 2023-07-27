import requests
from datetime import datetime
import pytz
import os
from dotenv import load_dotenv
from pprint import pprint
from encryption import PayEncry

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

x = PayEncry(pmDict,key)
sign = x.payMd5()
body = x.body()
body["sign"] = sign
print("body:")
pprint(body)
header = {"Content-Type": "application/json",
          "charset": "utf-8", "__tenant": os.getenv("tenantId_PayOut")}
respone = requests.post(
    f"https://{domain}/api/payout", json=body, headers=header)
if respone.status_code == 200:
    print("respone:")
    pprint(respone.json())
else:
    print("錯誤訊息:")
    print(respone.text)

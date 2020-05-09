import requests
from dbtools import chaxun
url = "http://192.144.148.91:2333/get_title_img"
res = requests.get(url)

try:
    assert res.status_code == 200  
    print("状态码校验成功") 
except:
    print("状态码不为200")
try:
    assert res.json().get("status") == 200
    print("返回值校验成功")
except:
    print("返回值不为200")

for 
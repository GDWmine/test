import pymysql

# name = input("请输入用户名：")
# pwd = input("请输入密码：")
def chaxun(sql):
    db = pymysql.connect(host="106.52.239.168",port=3306,user="root",password="1qaz!QAZ",database="ljtestdbb",charset="utf8")
    cursor = db.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    db.close
    print(res)

# chaxun("show tables;")

def jiafa(a,b):
    res = a+b
    print(res)

import random
def randomphone(n):
    a = []
    for i in range(n):
        phone = random.randint(13500000000,19999999999)
        print("",phone)
        if phone in a:
            print("重复了")
        else:
            a.insert(0,phone)
            print(a)
    with open("./phone.txt", "w") as f:
        for i in range(len(a)):
            s = str(a[i]).replace('[','').replace(']','')#去除[],这两行按数据不同，可以选择
            s = s.replace("'",'').replace(',','') +'\n'   #去除单引号，逗号，每行末尾追加换行符
            f.writelines(s)
    with open("./phone.xlsx", "w") as fe:
        for i in range(len(a)):
            s = str(a[i]).replace('[','').replace(']','')#去除[],这两行按数据不同，可以选择
            s = s.replace("'",'').replace(',','') +'\n'   #去除单引号，逗号，每行末尾追加换行符
            fe.writelines(s)

randomphone(500)
import json


with open('tst.json',encoding='utf-8') as f:
    dat=json.load(f)#获取到的dat是一个列表
    print(dat[1])
    for i in dat:
        print(f"姓名:{i.get('name')},年龄:{i.get('age')},爱好:{i.get('hobby')[1]}  "
              f"性别:{i.get('sex')},城市:{i.get('address').get('city')}")
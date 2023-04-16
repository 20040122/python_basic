import json

dic1={"name":"张三","age":19}
with open('tst2.json','w',encoding='utf-8') as f:
    json.dump(dic1,f,ensure_ascii=False,indent=4)
import random
import json

mys = []
for i in range(10):
    mys.append(random.randint(1,51))

print(mys)

with open('data.json','w',encoding='utf-8') as f:
    json.dump(mys,f)
with open('data.json',encoding='utf-8') as g:
    a=json.load(g)
    a.sort(reverse=True)
    print(a)
with open('data1.json','w',encoding='utf-8') as h:
    for i in range(5):
        json.dump(a[i] ,h)
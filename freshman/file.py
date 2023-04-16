with open('a.txt',encoding='utf-8') as f:
    while True:
        a=f.readline()
        if a=='':
            break
        else:
            print(a,end='')
num=input("请输入一个数字:")
try:
    num=8/int(num)
    print(num)
except Exception as e:
    print(f"发生了{e}")
def sr(list1):
    list1 = list1.split()
    num = list(map(int, list1))
    sr = sum(num) / len(num)
    return sr
while True:
    a=input()
    if a=='':
        break
    else:
        print(sr(a))

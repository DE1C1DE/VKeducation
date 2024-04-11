inp=input()
inp=inp.replace(" ","")
inp=list(inp)
a=[]
for i in inp:
    a.append(int(i))
print(a)
e=list(map(lambda x: -x if x%2==0 else x**2, range(a[0], a[1], a[2])))
for i in e:
    print(i)
#Недоделан

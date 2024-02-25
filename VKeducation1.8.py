obr=int(input())
b=list()
count=0
c=list()
while True:
	a=input()
	if a =="":
		break
	a=a.split()
	a=list(map(int, a))
	m=max(a)
	b.append(m)
ns=sorted(b[0:obr])
s=ns[: :-1]
s=str(s)
s=s.replace(" ",";")
s=s.replace(",","")
print(s)
#VKeducarion не засчитывает ответ, в отчёте выдавая ошибку исполнения, при исполнении в компиляторе исполняется корректно

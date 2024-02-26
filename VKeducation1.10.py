a=input().lower()
b=a.split()
count=[]
name=[]
for i in b:
	c=b.count(i)
	count.append(c)
	name.append(i)
m=max(count)
ind=count.index(m)
print(name[ind], m)

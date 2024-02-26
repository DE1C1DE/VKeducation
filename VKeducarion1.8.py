a=input()
a=a.lower()
b=list(a)
cou=list()
r=list()
for i in b:
 if b.count(i)>1:
  if not i in cou:	
  	r.append(i)
  	cou.append(i)  
  continue
 else:
  r.append(i)
r.sort()
r=str(r)
r=r.replace(",","")
r=r.replace("'","")
print(r)

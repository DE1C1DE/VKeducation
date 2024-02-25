text=input().lower()
count=0
m1=[]
m2=[]
m=[]
result=[]
text1=text.replace('!', "")
text2=text1.replace('$', "")
text3=text2.replace('#', "")
text4=text3.replace('%', "")
text5=text4.replace("?", "")
text6=text5.replace(".","")
text7=text6.replace(",","")
text8=text7.replace(":","")
text7=text6.replace(";","")
text8=text7.replace("^","")
text9=text8.replace("*","")
text10=text9.replace("(","")
text11=text10.replace(")","")
text=text11
text=text.split()
for e in text:
    count=text.count(e)
    if count>2:
        m1.append(e)
        for i in m1:
            if len(i)>=5:
                m2.append(i)
m2=set(m2)
for c in m2:
    if len(set(c))>=4:
        c=str(c)
        result.append(c)
result.sort
for w in result:
    print(w)
#p.s: писал ночью и голова особо не соображала, сейчас понимаю, что можно сделать проще, но лень переделывать, работает же. 

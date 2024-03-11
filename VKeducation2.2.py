def a(list1):
    if list1[0]=='!':
        list1=list1.upper()
    else:
        list1=list1.lower()
    list1=list1.replace("!",'')
    list1=list1.replace('%','')
    list1=list1.replace('@', '')
    list1=list1.replace('#','')
    return list1
print(a(input()))
#VKeducation не засчитывает, хотя всё точно по заданию

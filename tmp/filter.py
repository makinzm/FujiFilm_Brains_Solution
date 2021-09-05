lst=list(range(1,11))

lst_a=list(filter(lambda x: x>8,lst))

lst_b=[]
for i in lst:
    if i>8:
        lst_b.append(i)

print(lst)
print(lst_a)
print(lst_b)
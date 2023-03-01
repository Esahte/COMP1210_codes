lst = [x for x in range(1, 10)]
print(lst)

lst2 = []
while len(lst):
    lst2.append(lst.pop(0))
print(lst2)


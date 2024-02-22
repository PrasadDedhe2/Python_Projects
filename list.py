mylist = ['hey']
mylist_1 = ['idiot','kk']
print(type(mylist))
mylist.append('ok')
mylist.append('ok1')
mylist.remove('ok1')
mylist.sort()
print(mylist)
mylist.reverse()
print(mylist)
print(len(mylist))
print(mylist.count('ok'))
print(mylist[1])
print(mylist.append(mylist_1)) #does not work appending one list into another
mylist.append(2342)
print(mylist[2][0])
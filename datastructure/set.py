myset = {13,1,2,3,4,4,4,4,4,4}
myset_1 = {2,3,41,12,13}



# Sets support various set operations such as union, intersection, difference, and symmetric difference.
# These operations enable you to perform common set operations efficiently and easily. For example,
# you can find the intersection of two sets to determine the common elements between them. Also sets are unique, i.e.
# no elements are being repeated.
# Also, as set is unordered you cannot get indexed value, like mysetl[0] = 13, it is not allowed

print('myset ', myset, ' myset_1 ', myset_1 )
print(type(myset))
myset.add(5)
myset.remove(2)
print('added 5, removed 2',myset)
print('sorted myset',sorted(myset))
print('intesection of two sets',myset_1.intersection(myset))
print('union of two sets',myset.union(myset_1))
print(myset)
print(myset_1)
print('difference between two sets w.r.t myset', myset.difference(myset_1))
print('difference between two sets w.r.t myset_1', myset_1.difference(myset))
print('difference update of two sets w.r.t myset', myset.difference_update(myset_1))
print(myset)
print(myset_1)
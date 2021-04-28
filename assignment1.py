#program to iterate over dictionary
d={"a":1,"b":2,"c":3,"d":4,"e":5}
for k,v in d.items():
    print(f"{k}:{v}")

#program to sort dictionary by keys-use itemgetter
from operator import itemgetter
d1={"b":3,"a":4,"e":5,"c":2,"d":1}
for i in sorted(d1, key=itemgetter(0)) :
    print ((i, d1[i]), end =" ")
print("\n")

#program to sort list of dictionary by one key:use lambda
l=[{"z":3,"c":12},{"y":5,"b":6},{"x":7,"a":8}]
print(list(sorted(l,key=lambda x:[i for i in x.keys()][1])))

#program to get sum of elements having same index from two list-use lambda
l1=[1,2,3,4,5,6]
l2=[6,7,8,9]
s=list(map(lambda x:sum(x),list(zip(l1,l2))))
print(s)

#program to find sum of all item in the dictionary
d2={"a":100,"b":400,"c":600}
sum=0
for i in d2:
    sum=sum+d2[i]
print(sum)

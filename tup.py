tup=(1,2,3,76,342,"green",True)
#tup[0]=90 Cannot change
print(tup)
print(tup[0])
print(tup[-1])
print(tup[2])
#print(tup[34]) out of range
if 1 in tup:
    print("Yes 1 present inn this tuple")
tup2 = tup[1:4]
print(tup2)    
#operations on sets

#union (|)
s1=  {1,2,3,4,5}
s2={4,5,6,7,8,9 }
print(s1 | s2 )

#intersection (&)
print(s1 & s2 )

#differnce (-)
print(s1 - s2)
print(s2 - s1)

#symmetric diff (^)
print (s1 ^ s2 )

#membership test
print(1 in s1 )
print(10 not in s2)
print (10 in s1 )

#iteration
for i in s1:
    print(i)
dictt = {'name': 'aashi', 'age': 20, 'gender': 'female', 'weight': 51.8}

#len
print(len(dictt))

#sorted 
print(sorted(dictt))
print(sorted(dictt ,reverse=True) )

#min
print(min(dictt))

#max
print(max(dictt))

#items 
print(dictt.items()) # it will return a view object that displays a list of a dictionary's key-value tuple pairs

#keys
print(dictt.keys())

#values
print(dictt.values())

#update 
d1 = { 1: 1 , 2: 3 , 3 : 9}
d2 = {2:4 , 4:16}
d1.update(d2)
print(d1)


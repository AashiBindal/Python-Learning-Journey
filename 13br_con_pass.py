#break 
for i in range(1,10):
    if i==5 :
      break 
    print(i)

#print prime no. 
lower = int(input('enter lower no. : '))
upper = int(input('enter upper no. : '))
for i in range(lower , upper+1):
   for j in range(2,i):
      if i%j==0:
         break 
   else:
        print(i)  
    
#continue
for i in range(1,10):
    if i==5 :
     continue 
    print(i)  

#pass
for i in range (1,10):
   pass    
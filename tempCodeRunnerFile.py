#-------------------------------------------------------------------------


# REDUCE
 # import functools 

import functools

# Sum of all items 
print(functools.reduce(lambda x,y : x+y ,[1,2,3,4,5]))


#find mmin
print(functools.reduce(lambda x,y : x if x<y else y ,[3,44,5,-9,7,-66] ))




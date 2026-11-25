# dictionary operators
student = {
         'name' : 'aashi' ,
         'collage' : 'acropolis' ,
         'sem' : 5 ,
         'subjects' : {
             'dsa' : 100,
             'python' : 99 ,
             'english' : 99 
         }

}
print(student)

#membership operator
print('dsa' in student['subjects']) # it will return True if the key 'dsa' is present in the dictionary student['subjects'] else it will return False
print('weight' in student)
print('weight' not in student)


#iteration 
d = {'name' : 'aashi' , 'age' : 20 , 'gender' : 'female' , 'weight' : 51.8}
for i in d :
    print(i ,':', d[i])
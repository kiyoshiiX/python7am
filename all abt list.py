
         #LIST  like array in C prog, group of sth is list in python.

listKoEg = [1234, 'ram' , True , "dat" , 'java']
print(listKoEg[0])
print(listKoEg[1],listKoEg[4])

         #QUESTION 1; print 3 and 12 from the data  [1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]

data1 = [ [1,2,3,4,5],
         [6,7,8,9,10],
         [11,12,13,14,15]
]
print(data1[0][2]) 
print(data1[2][1])

         #QUESTION 2 ; PRINT 6969 from the data [[1,2,3,4,4],[34,344,3456,[2,6969,4,5]]]
print("answer for question 2\n")
data_cmplx = [1,2,3,4,4],[34,344,3456,[2,6969,4,5]]
print(data_cmplx[1][3][1])  #it says one vitra ko 3 vitra ko 1

        # Mutable datatype; replace garna milne data type
    
data2 = [12,13,14,15,16,17]
data2 [0] = 13
print(data2)         #while printing 12 is replaced by 13
 


 # append()      ; adds an element to END OF THE LIST
data3 = [23,34,45,56,67]   #general output; will be [23,34,45,56,67]  but using append
data3.append(12)
data3.append([1,2,3])
print(data3)

# clear()       ; removes all element
  
# copy()        ; returns a copy of the list
# count()       ; returns the no. of element
# extend()      ; add the element of list (like append but not in a obvious way)
           #data6 = [23,45,657,6786,678,234]
           #data6.extend(234)  #but it takes only one argument not data6.extend(234,45,456)
           #print(data6)

 # index()       ; returns the index of the first element with specified value
 # insert()      ; adds an element at the specified position
print("about insert \n")
data7 = [123,1234,12345,123456,1234567]
data7.insert(0,777)
print(data7)
# pop()         ; removes all the element at the specified position
# reverse()     ; reverses the order of the list
# sort()        ; sorts the list


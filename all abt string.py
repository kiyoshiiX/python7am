
       #String : data values that are made up of ordered sequences of characters


from dataclasses import replace


a = "john"
print(type(a))  #a string

a = '''123'''
print(type(a))  #still a string

a = '123'
print(type(a))  #still a string

name = "Ram_Bahadur"
print(name[3])     #This shows the first or precisely zeroth character of the name
                   # 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
                   # R | A | M | _ | B | A | H | A | D | U | R  |
dosroNam = "Hari"
print(dosroNam[2:]) #first 2 array character are removed

tesroNam = "Shyam"
print(tesroNam[:2]) #last 2 array character are removed

chauthoNam = "Hello"
print(chauthoNam[:-1]) #last 1 array character are removed

pachauNam = "Sophia"
print(pachauNam[2:-1]) #first two and last one array character are removed


    # chr() and  ord()

print(chr(97))    #shows which character is in 97th posioion
print(ord('a'))   #vice versa i.e 97

     #Capitle and small letter

full_name = 'kiyoshi pandey'
print(full_name.upper())  #prints with all upper case
print(full_name.lower()) #prints wt all lower case

arko_name = 'hello how are you'
arko_name = replace("hello","Yo wassup")
print(arko_name)





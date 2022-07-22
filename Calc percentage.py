#enter marks of english, maths, nepali and print its percentage

print("Insert your marks out of hundred here")

English = int(input("Enter your English grade : "))
Maths = int(input("Enter your Maths grade : "))
Nepali = int(input("Enter your Nepali grade : "))

Result = (((English+Maths+Nepali)/300)*100)

print("The Percentage obtained is :", Result)
print(f"Your marks obtained of English ; {English} Maths ; {Maths} , Nepali ; {Nepali} and your final result is {Result}")

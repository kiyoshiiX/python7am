#enter P,T,R and print its simple interest
#enter marks of english, maths, nepali and print its percentage


principal = float(input('Enter the principle amount: '))
time = float(input('Enter the time: '))
rate = float(input('Enter the rate: '))
simple_interest = (principal*time*rate)/100
print("Simple interest is:", simple_interest)
#program to calculate simple interest

#getting input from the user
principal = int(input('principal amount:'))
rate = float(input("interest Rate :"))
years = float(input("number of years :"))
#calculating simple interest
interest= (principal * rate * years )/100

#printing the result
print("simple interest :",round(interest,2))
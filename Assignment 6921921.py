#script for car deals
#list of available cars and their prices
cars = {
        'Mercedes': 500000,
        'Audi': 455000,
        'Ford': 33000,
        'Lamborghini': 760000,
        'Cardillac': 800000,
        ' Hyundai': 930000,
        'Jeep': 320000,
        'Chevrolet': 50000,
        'Mazda': 560000,
        'Alfa Romeo': 45000,
        'Maserati': 76000900,
        'BMW': 6400000,
        'toyota': 9600000,
        'Mercedes-Benz': 650000,
        'Honda': 5800000,
        'Porche': 3200000,
        'Volvo': 45000000,
        'Kia': 7000000,
        'jaguar': 6500000,
        'aston': 867000,
        'pagani huayra': 4580000,
        'altima': 120000,
        'ferrari': 6900000,
        'tesla': 3450000,
        'bentayga': 580000,
        'bugatti': 970000,
        'rolls royce': 100000000,
        'benz c400': 450000000,
        'infiniti': 3568000000,
        'chrysler': 87500000,
        'peugeot': 90000000}
#get user input for car name
carName=input("enter a carName: ")
#check if car name is in the list of available cars
if carName in cars:
    print("Yes")
    #if car name is available, get its price
    carPrice = cars[carName]
    print(f"The price of {carName} is ${carPrice}.")
else:
    #if car name is not present, make the user aware
    print(f"sorry,{carName} is not available.")
#https://github.com/users/Tiwaa-Acheampong-Cecilia/emails/242403744/confirm_verification/23493405?via_launch_code_email=true

    
    
    
cap=60
fuelrange=14
distance=650
maxdist=2000
gallon=4.55
print("Car can travel ", cap*fuelrange, "kms")
print("Car will use %.2f" %(distance/fuelrange),"litres to travel 650kms")
# no ceiling function so invert floor function
print("To travel 2000 kms the car must refuel", (-(maxdist//-(cap*fuelrange))),"times")
print("Car can travel ", gallon*10*fuelrange, " on 10 gallons")

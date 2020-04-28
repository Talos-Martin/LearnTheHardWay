cars = 100
space_in_a_car = 4
drivers = 30
#This is a comment above the passengers variable
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity=cars_driven*space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are ",cars, " cars available")
print("There are only ", drivers, "drivers available")
print("There will be ", cars_not_driven, "empty cars today")
print("We can transport ", carpool_capacity, "people today")
print("We have ", passengers, "to carpool today")
print("We need to put ", average_passengers_per_car, "in each car")

#His error: carpool_capacity != cap_pool_capacity. 2 different variables.
#4.0 vs 4. Result is also float or not depending on input number

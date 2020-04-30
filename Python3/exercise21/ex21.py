
def add(a,b):
    print(f"Adding {a} and {b}")
    return a+b

def substract(a,b):
    print(f"Subtracting {b} from {a}")
    return a-b

def multiply(a,b):
    print(f"Multiplying {a} and {b}")
    return a*b

#returns floating point , interesting
def divide(a,b):
    print(f"Dividing {a} by {b}")
    return a/b

print("A little math exercise")

age=add(30,5)
weight=substract(120,40)
height=multiply(40,4)
iq=divide(300,3)

print(f"Result: Age: {age} - Weight: {weight} - Height: {height} - IQ: {iq}")

print("Not really a puzzle")
what = add(age, substract(height, multiply(weight, divide(iq, 2))))
#-3805 ?
print(f"Result: {what}")

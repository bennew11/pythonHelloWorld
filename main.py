from network import Network

# variables
# branch1 change
var3 = 3

print(var1)

#casting
var1 = int(var1)

var1 = str(var1)

print(f"this is a string {var1}")

# math functions
var4 = len(var2)

print(var4)

class test:
    def __init__(self, a):
        self.a = a

    def print_a(self):
        print(self.a)

print(var2[0])

price1 = 3.14159
price2 = -987.65
price3 = 12.34


print(f"Price 1 is {price1:.1f}")

# string methods

str_prac = "hell i am in lower case"
print(f"lower case {str_prac}")
str_prac = str_prac.upper()
print(f"here is the uppercase {str_prac}")
#string index
print(f"here is the first character {str_prac[0]}")
fruits = ["apple","orange","banana"]

print(fruits[0])

doubles  = [x*2 for x in range(1,11)]

print(doubles)

prac = [x*3 for x in range(1,11)]

print(prac)

var1 = "hold me back"
var2 = 5.0

var3 = int(var2)
print(f"var3 = {var3}")

var5 = len(var1)

print(f"length of var1 = {var5}")

print(f"first element of var1 is {var1[0]}")

var31 = 5.0

var32 = int(var3)

print(f" the value of var32 is {var32}")

cubes = [x**3 for x in range(1,100)]

print(f"cubes in the range {cubes[0]}")

net = Network([2, 3, 1])

print(f" the number of layers {net.num_layers}")
print(f" the number of biases {net.biases}")
print(f" the number of weights {net.test}")



print("Hello World")
a = 5 
print(a)
b = "this is Arpit"
print(b)
c = 10
c = "will this work ?"
print(c)

print("--------------------")

def add_two_number(a, b):   #this is how function is defined
    print("hello")
    print(f"the sum is: {a+b}") # note f is same as $ in c# to print the variable 
    return a + b

sum = add_two_number(10, 20)
print(sum)

print("--------------------")

def test_function(a, b):
    if a < 0 or b<0:
        print("one values are -ve")
    else:
        print(f"both of them are +ve")      #note: no need to return anything if you want void
    if a < 0:
        sum = add_two_number(a, b)
        print(sum)
    elif b < 0:
        print("this is else fi condition")
    else:
        print(" this is else case")

test_function(-1, -2)
test_function(1, 2)


print("--------------------")

status = 400

match status:       #there is no switch case in python there is match case 
    case 200:
        print("200")
    case 404: 
        print("not found")
    case x:                 # acts like default
        print("unknown")

print("--------------------")

for i in range(5): #[0,5] 
    print(f"this is {i}th loop")

print("--------------------")

for i in range(0, 5, 2): #range(start(inclusive), stop(exclusive), skip = 1)
    print(f"this is {i}th loop")

print("--------------------")

for i in range(0, 10, 4): #range(start(inclusive), stop(exclusive), skip = 1)
    print(f"this is {i}th loop")

print("--------------------")

for i in range(5, 0, -1): #range(start(inclusive), stop(exclusive), skip = 1)
    print(f"this is {i}th loop")

print("--------------------")

i = 4
while i > 0:
    print("this is loop", i)
    i-= 1 # without this loop will not end

print("--------------------")


length = int(input("length of an array : "))

for i  in range(0, length, 1):
    print("Array at i = ", i)
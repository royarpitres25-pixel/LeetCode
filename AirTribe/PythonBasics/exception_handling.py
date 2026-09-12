def devide_two_numbers(a, b):
    if b==0:
        print("cannont device by zero")
        return
    return a / b

result = devide_two_numbers(10,0)
print(result)


def devide_two_numbers(a, b):
    try:
        return a / b
    except:
        print("cannont device by zero")

result = devide_two_numbers(10,0)
print(result)
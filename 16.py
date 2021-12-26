input_from_user = int(input("enter  your age: "))

if input_from_user > 0:
    print("age is ok")

input_from_user = int(input("enter  your amount of pets: "))

if input_from_user > 0:
    print("amount of pets is ok")


def check_input(gt, input_string):
    input_from_user = int(input(input_string))
    if input_from_user > gt:
        return True
    else:
        return False


result = check_input(0, "enter your age: ")
if result == True:
    print("age is ok")
result = check_input(2, "enter  your amount of pets: ")
if result == True:
    print("amount of pets is ok")


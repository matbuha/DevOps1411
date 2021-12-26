isTrue = False
a = 2
b = 2.5
strone = "one"
strthree = "Three"

if a >= 2 and strone == "one" or not strthree == "two":
    print("a is greater then 2")
elif b == 2.5:
    print("something")
elif strone == "3":
    print("bla")
else:
    print("a is lower then 2")


my_other_list = ["roni"]
my_list = ["hen", "lior", "shay", "ariel"]
if my_list[0] == "hen":
    print("we found hen!")
if "hen" in my_list:
    print("yes he is")
if my_other_list:
    print("hello")

if len(my_list) > 0:
    print("hey")

c = 5
d = 5
e = 9
if c is d:
    print("c is d")

if type(e) is int:
    print("e is an integer")


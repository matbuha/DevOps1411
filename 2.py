"""my_number = "4"
result = float(my_number) - 2
print(result)
# print("your result is " + str(result))
my_list = [10, 20, 30, 40, 50, 60, 70, 80]
print(my_list[0:2])
print(my_list[4:0:-1])

print(my_list[::2])"""

my_str = "hello and welcome to \\\"devops experts\\\""
print(my_str)
my_dict = {"fname": "ariel",
           "lname": "ben zikri",
           "age": 34,
           "ID": 300972429}
key_to_print = input(f"enter a key {list(my_dict.keys())}: \n")
print("you chose to print: " + str(my_dict[key_to_print]))

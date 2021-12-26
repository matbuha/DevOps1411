from os import getenv
print("Hello world")
name = getenv("NAME")
if name == "ariel":
    print("you are ok")
else:
    print("I don't know who are you")

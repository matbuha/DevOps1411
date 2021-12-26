"""a = "hello world"
b = 4
c = ["alef", "bet", "gimel", "dalet"]
for i in range(b):
    print(str(i + 1) + ")" + a)"""

"""for i in range(len(c)):
    print(c[i])"""

"""for name in c:
    if name == "alef":
        continue
    else:
        print(name)"""
"""d = 0
while d < 10:
    print(d)
    d = d + 1"""

"""for i in range(1, 101):
    if i % 7 == 0 or "7" in str(i):
        continue
    print(i)"""

a = "a"
while a != "q":
    a = input("enter q or not: \n")

if a in range(5):
    print(a)
else:
    print("finished")

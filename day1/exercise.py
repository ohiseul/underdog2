a = "Dog is love"

print(a[7:11])
print(a.replace("Dog","Cat"))

b = "lalalalalalalalalalala"
print(b.count("l"),b.count("a"))


c = "010-1234-5678"
print(c.replace("-",""))

a = "hello"
b = "python"
print(a+" ! "+b)

a = [1,2,3]
a[2] = 4
print(a)

del a[2]

a = [0, 1, 2, 3, 4, 5, 6, 7, 8]
del a[1:6]
print(a)


a = [0,1,2,3]
a.append(4)
a.append(5)
print(a)

a.append(["0","1","2","3"])
print(a)
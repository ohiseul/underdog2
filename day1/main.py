""""
print('hello')

a=10
b=5
c="안녕하세요"




print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**b)

a += 50
print(a)
a -= 20
print(a)


print('*' * 10)

happy_face ='🥰'
print(happy_face)

"""

a = "3"
b = "5"
b = "5" * 5
print(a+b)

a = "3"
b =  5 
# print(a+b) 에러



print(type(a))
print(type(b))
print(type(3.5))
print(type(5>3))
print(type(True))


a = "256"
print(int(a),type(int(a)))
print(float(a),type(float(a)))

print("hello", "world")


number_list = [1,2,3,4,5]
names = ["이름1","이름2","이름3","이름4"]

random_list = [3, 3.9 , "python", False, True]

print(random_list)

for element in random_list:
    print(type(element))


# tuple 리스트와 비슷하지만 한번 만들어진 튜플은 데이터 변경 불가능

my_list = [1, 2, 3, 4, 5]
print(my_list[2])
my_list[2] = 50
print(my_list[2])

my_tuple = (1, 2, 3.5, "hello", False)
print(my_tuple[2])
# my_tuple[2] = 50  does not support item assignment
# print(my_tuple[2])

a = "hello world 😘"
b = "esg"

print(len(a))
# print(len(b))
# print(len(my_list))

print(a[0])
print(a[12])

# 슬라이싱 개념
print(a[0:12])
print(a[1:2])
print(a[2:3])
print(a[3:6])
print(a[4:13])
print(a[5:14])
print(a[6:15])

my_list = [1, 2, 3.5, "hello" ,[1, 2, 3, 4, 5] ,True, False]
print(my_list[3:5])

class_name= "chatgpt api"
print(len(class_name))
print(class_name[4:])
print(class_name[:7])

class_name.count("a")



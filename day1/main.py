"""
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

find_str = "python!"
print(find_str.find("y"))


title = "   PYTHON class   "
print(title.upper())
print(title.lower())
print(title.strip())

print(title.upper(),title.lower(),title.strip())

quote= "Life is too short"
print(quote.replace("too", "very"))
print(quote.replace("o", "0"))
print(quote.replace(" ", ""))
print(quote.split(" "))


quote2= "Learn Python"
print(quote2.split(" "))
print(quote2.split("p"))
print(quote2.split("arn"))


example = "a:b:c:d"
print(example.split(":"))

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

a.extend(["0","1","2","3"])
print(a)


a = [9,3,6,1,12,2,33,4,8,5]
print(sorted(a))
print(a)
a.sort()
print(a)

a=["a","b","c","d"]
a.reverse()
print(a)

a.append(10)
print(a)
a.insert(2,"0")
print(a)


a =[1,2,3,1,2,3]
a.remove(3) #첫번째로 나오는 3 삭제
print(a)
a.pop() #맨뒤로 나오는거 삭제 마지막3
print(a)


a=["a","b","c","d","e"]
print(a.pop(1))
print(a)

a= "lalalalalalaaaa"
print("count of a is :" , a.count("a"))

a=["A","c","b","E","B","D","e"]
print(a.count("A"))
print(sorted(a))

my_list = [0] *10
my_tuple = (0,) *10

print(my_list)
print(my_tuple)

my_list = [1,2,3,["a","b","c"]]
print(my_list[3][2])
print(len(my_list))
print(len(my_list[3]))


my_dictionary = dict()
print(my_dictionary)
my_dictionary = {"name":"이름","location":"서울"}
my_dictionary["age"] = 29
my_dictionary["office_location"] = "지역"
my_dictionary["favorite_foods"] = [{"name":"이름2","is_healthy":True},{"name":"이름3","is_healthy":False}]

print(my_dictionary)


print(my_dictionary["name"])
print(my_dictionary.get("office_location", "Unknown"))

print(my_dictionary.keys())
print(my_dictionary.values())
print(my_dictionary.items())

for key, value in my_dictionary.items():
    print("key",key)
    print("value",value)



print(5 < 3)
print(5 < 10)
print("age" in my_dictionary)

if "age" in my_dictionary:
    pass
else:
    my_dictionary["age"] = 50



a = {"a" : 90 , "b" : 80 , "c" : 70, "d": 60}

print(a["a"],a["b"])
print(a.get("a"))

if('b' in a):
    print(a["b"])

my_set = {1,2,3}
my_set.add(4)
my_set.add(4)
my_set.add(4)

print(my_set)


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}
set2.add(8)
set2.update([9,10,11,12])

print(set1 & set2)
print(set1 | set2)
print(set1 - set2)

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
ss1 = set1 & set2
ss2 = set1.intersection(set2)
ss3 = s1 - s2
ss4 = s1.difference(set2)


print("------")
print(s1 & s2)
print(s1 - s2)

s3 ={1,2,3,4,4,4,9,11,11,11,14}
print(s3 | s3)


my_list = list(set(s3))
print(my_list)

my_list.sort()
print(my_list)
my_list = sorted(my_list)
print(my_list)



print(5  == "5")
print(5  != "5")
print(5 > 3)
print(3 <= 2)







print(5 >3 and 10 >1)
print(5 >3 or 10 <1)
print(not 1 >2)
print(not False)
print(not True)


if True:
    print()
    print()
elif (3> 5 amd 2 <4):
    print()
elif:
    print()


"""

score = int(input("점수가 몇점인가요 : "))

if score >= 60 :
    print("pass입니다")
else:
    print("false 입니다")

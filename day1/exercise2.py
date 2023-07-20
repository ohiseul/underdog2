# 구구단
for x in range( 2, 10 ) :
    print( x, "단" )
    
    for i in range( 1, 10) :
        print( x, "*", i, "=", x*i )



# 커피자판기
coffee_dictionary={
    "latte" :{
        "price":2000,
        "type":"ice"
    },
    "americano" :{
        "price":1500,
        "type":"ice"
    }
}

def coffee_box():
    pay = int(input("가격을 입력해주세요:"))
    type = input("커피를 주문해주세요:")

    if coffee_dictionary.get('type'):
        coffee_info = coffee_dictionary[type]
        price = coffee_info[price]
        if pay >= price : 
            print(type," 커피 나왔습니다! 거스름돈은 ",pay - price,"원 입니다") 
        elif pay < price :
            print("돈이 부족합니다")
    else :
        print("잘못된 주문입니다.")

coffee_box()



# 체질량 지수
height = float(input("키:")) 
weight = float(input("몸무게:")) 
 
def bmi_check(height,weight):
    BMI = round(weight / (height * 0.01)**2 , 2)
    print("BMI:",BMI)

    if BMI < 18.5 :
        print("저체중")
    elif BMI < 25 : 
        print("정상")
    elif BMI < 30 :
        print("과체중")
    else :
        print("비만")

bmi_check(height,weight)
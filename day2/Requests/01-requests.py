import requests
import secrets

# def main():
#     response = requests.get(f"http://api.exchangeratesapi.io/v1/latest?access_key={secrets.API_KEY}")
#     print(response.status_code)
#     print(response.headers['Content-Type'])
#     # print(type(response.text))
#     response_json = response.json()
#     print(response_json['success'])
#     print(response_json['timestamp'])

def main():
    payload = {"access_key": secrets.API_KEY}
    response = requests.get(f"http://api.exchangeratesapi.io/v1/latest"
                            , params = payload )

    print(response.status_code)
    if response.status_code != 200:
        print("에러: ", response.status_code)
        return  
    response_dictionary = response.json()
    # print("JSON data: ", response_dictionary)
    
    success = response_dictionary['success']
    timestamp = response_dictionary['timestamp']
    date = response_dictionary['date']
    base = response_dictionary['base']
    KRW = response_dictionary['rates']['KRW']
    AUD = response_dictionary['rates']['AUD']
    USD = response_dictionary['rates']['USD']

    print(f"성공코드 {success}")
    print(f"timestamp {timestamp}")
    print(f"date {date}")
    print(f"base {base}")
    print(f"KRW {KRW}",f"AUD {AUD}",f"USD {USD}",)







    # 받은 response를 dictionary 

    # success는 뭐다
    # timestamp 몇이다
    # base krw 기준으로 달러는 얼마다


if __name__ == "__main__":
    main()
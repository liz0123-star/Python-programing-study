
# # a = 1

# # if a > 5:
# #     print(a)
# #     print(a)

# # print('끝')
# # print(a)


# # password = 'data'
# # answer = input('비밀번호를 입력해주세요.: ')

# # if(answer == password):
# #     print('correct')


# # num = int(input('숫자 하나 입력해주세요: '))
# # if int(num % 2 == 0):
# #     print('짝수')


# math = 83
# science = 90

# if (math >= 80 and science >=  80):
#     print('합격')


# if (math < 80 or science <  80):
#     print('탈락')

# if 1:
#     print('탈락')


# # num = int(input('숫자 입력: '))

# # if (num % 5 == 0 and num % 7 == 0):
# #     print('35의 배수')

# #10과 15의 공약수
# # num = int(input('숫자 입력: '))

# # if ( 10 % num == 0 and 15 % num == 0):
# #     print('10과 15의 공약수')

# a = 1    #브레이크 포인트 -> 49 다음 54번째 줄로 감.
# if a > 5:
#     print(a)

# else:
#     print('5보다작네')

# print('끝')

# num = 21

# if num % 2 == 0:
#     print('짝수')

# else:
#     print('홀수')

# if num % 2 == 1:    #부분점수만..
#     print('홀수')

# a = 83

# if a > 70:
#     print(a)
#     if a == 100:
#         print('100점')
#     else:
#         print('100점은 아니네')

# num = 11

# if num % 2 == 1:
#     print('홀수')

# else:
#     print('짝수')

# message = '홀수' if num % 2 == 1 else '짝수'
# print(message)

# math = 83
# science = 90

# if (math < science):
#     print(science)

# else:
#     print(math)

# # num = int(input('숫자 입력: '))

# if (num % 2 == 0 and num > 10):
#     print('x')

# else:
#     print('o')

# year = int(input("연도를 입력하세요: "))

# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 :
#     print("%d년은 윤년입니다." %year)

# else:
#     print("%d년은 윤년이 아닙니다." %year)

# score = 95

# if score >= 90:
#         print('90넘네')
# elif score >= 80:
#     print('80넘네')

# else:
#     print('불합격')

# bill = float(input("주문 금액을 입력해주세요.: "))
# delivery_fee = -1

# if bill >= 50000:
#     print('배달비 무료')

# elif bill >= 30000:
#     delivery_fee = bill * 0.05
#     print("배달비는 %d원" %delivery_fee)

# elif bill >= 10000:
#     delivery_fee = bill * 0.1
#     print("배달비는 %d원"%delivery_fee)

# else:
#     print('배달 불가')


speed = 424

if speed > 100:
    print('위험!')

elif speed > 80:
    ('과속!')

elif speed > 50:
    ('속도 줄이세요')

else:
    ('정상')

user_number = int(input("1부터 100 사이의 숫자를 입력하세요: "))
answer = 42

if user_number < answer:
    print("더 큰 숫자를 입력하세요")

elif user_number > answer:
    print('더 작은 숫자를 입력하세요')

else:
    print('정답입니다.')
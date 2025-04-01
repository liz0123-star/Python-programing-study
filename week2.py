print(1,2,3,sep=',')
print(1,2,3,end=' ')
print(4)

print('hello', end=' ')
print('I"m Tony')

#print("aaaa'") # 가능
#print("aa\"") # 같은 걸로 쓰려면 아스키 써야 함


### 1번 문제
print(1,3,5,7,sep='+', end='=')
print(1+3+5+7)

#파이썬 파일 다운 -> 내 다운로드 폴더 -> 잘라내기 -> 파이썬 폴더로 붙여넣기 해서 가져와야 함.
#학번:          이름:       
#print(1,3,5,7,      )
#print(1+3+5+7)
#저장 눌러서 빨간 동그라미 없앤 뒤 파일 드래그해서 제출.
#문제 ctrl + k + u눌러서 주석 처리 푼 뒤 풀어야 함.
#1번 문제 다 푼 뒤 다시 주석 처리 하고 2번 문제 풀기. (결과 계속 나옴)

# math = 92
# science = 87
# english = 94

# print('수학,과학,영어 점수는 각각 %d점, %d점, %d점 입니다' %(math,science,english))
# print("%s score: %d"%("math", math))
# print("%s score: %d"%("science", science))
# print("%s score: %d"%("english", english))


# math = input('수학 점수를 입력하세요.: ')
# python = input('파이썬 점수를 입력하세요.: ')
# mean_score = (int(math)+int(python))/2
# print('수학 점수는 %s, 파이썬 점수는 %s 입니다' %(math, python))
# print('그리고 평균 점수는 %f점 입니다' %mean_score)
# 문자 입력받은 건 int 쓰지말고 그대로 두기.

# f9 -> 브레이크 포인트 (포인트 직전 줄까지 실행) / f5 -> 디버깅 실행 / f10 -> 한 줄씩 내려옴
# input 함수 주석 처리하지 않으면 input 함수 입력해야 해서 기다림. (아직 브레이크 포인트까지X)
# 브레이크 포인트 2개 이상일 때 f5 한 번 더 누르면 다음 브레이크 포인트까지 실행.
a = 1
b = 5
c = a+b
print(c)
b = 9
c = a + b
print(c)


print(5 // 3)
print(5 % 3)

a = 6
a % 2 == 0 # 짝수
if a % 2 == 0:
    print('짝수')

if a % 2 == 1:
    print('홀수')


print(3 ** 5)

n1 = 5
n2 = 3

x = '100'
y = '100.123'
z = "99.4"

print(int(x),float(y),z)
# print(int(x+1),y,z) -> error
print(int(x)+1,float(y)+1,z)

k = str(float(y)+1)
print(k)

# pi = 3.14159265
# r = float(input('반지름 입력:'))

# length = 2 * pi * r
# area = pi * r **2

# print('원의 둘레는 %f, 넓이는 %f 입니다.' %(length, area))

# a = 2
# b = 3

a,b = 2,3
print(a,b)

a = 10
a += 3 # a = a+3
a/=2
print(a)

a = '동덕' 
a += '여대'
a *= 3
print(a)

a = 10
a *= 5
print(a)

a = 5
b = 10
print(a==b)
print(a!=b)

a = 5
b = 15
print( (a == 5) and (b > 10) )
print( (a == 5) and (b > 100) )
print( (a == 5) or (b > 100) )

print( not(a == 5) )

x = 150
print( 100 < x < 200)
print( (100 < x) and (x < 200) )


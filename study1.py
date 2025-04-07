#1
print('Hello, World!!')

#2
print('I love python!!')

#3
number = float(input('실수 입력: '))
print("%.1f" %number)

#4
a = int(input('정수1 입력: '))
b = int(input('정수2 입력: '))
print(a + b)

#5
c = int(input('정수1 입력: '))
d = int(input('정수2 입력: '))
print("%d + %d = %d" %(c, d, c+d))
print("%d - %d = %d" %(c, d, c-d))
print("%d * %d = %d" %(c, d, c*d))
print("%d / %d = %d" %(c, d, int(c/d)))

#6
print("I am a student.\n *\n\t^^Nice to meet you~")

#7
name = input("당신의 이름은?")
age = int(input("당신의 나이는?"))
height = int(input("당신의 키는?"))

print("이름은 %s, 나이는 %d살, 키는 %dcm입니다." % (name, age, height))

#8
e = int(input("정수 입력: "))
print(e * 0.5)
print(e ** 2)
print(e ** 3)

#9
#9-1

#10
#10-1

#11
#11-3

#12
#12-1

#13
#13-1

#14
#14-4

#15
#15-1

#16
f = int(input('수 입력: '))
if f > 0:
    print("양수입니다.")

elif f < 0:
    print("음수입니다.")

else:
    print("0입니다.")

#17
g = int(input("나이 입력: "))
if g >= 18:
    print('성인입니다.')

else:
    print('미성년자입니다.')


#18
h = int(input('점수를 입력하세요.: '))
if h >= 90:
    print('A')

elif h >= 80 and h < 90:
    print('B')

elif h >= 70 and h < 80:
    print('C')

elif h >= 60 and h < 70:
    print('D')

else:
    print('F')


#19
time = int(input('시간을 입력하세요.: '))
if time < 12:
    print('오전입니다.')

else:
    print('오후입니다.')

#20
i, j, k= map(int, input().split())
if i >= j and i >= k:
    print(i)

elif j >= i and j >= k:
    print(j)

else:
    print(k)

#21
l, m = map(int, input().split())

if (l + m) % 2 == 0:
    print('짝수입니다.')
else:
    print('홀수입니다.')

#22
n = int(input('숫자를 입력하세요.: '))

if n % 3 == 0 and n % 5 == 0:
    print('FizzBuzz')
else:
    print(n)

#23
o = int(input('연도를 입력하세요.: '))

if o % 4 == 0 and o % 100 != 0 or o % 400 == 0:
    print('윤년입니다.')

else:
    print('윤년이 아닙니다.')

#24
p, q = map(int, input().split())

if p > q:
    if p - q > 10:
        print('차이가 10 이상입니다.')

    else:
        print('차이가 10 미만입니다.')
    
elif p < q:
    if q - p > 10:
        print('차이가 10 이상입니다.')

    else:
        print('차이가 10 미만입니다.')

else:
    print('두 수는 같습니다.')

#25
r, s, t = map(int, input().split())

if r % 2 == 0 and s % 2 == 0 and t % 2 == 0:
    print('모두 짝수입니다.')

elif r % 2 != 0 and s % 2 != 0 and t % 2 != 0:
    print('모두 홀수입니다.')

elif r == 0 or s == 0 or t == 0:
    print('0은 포함될 수 없습니다.')

else:
    print('홀수와 짝수가 섞여 있습니다.')
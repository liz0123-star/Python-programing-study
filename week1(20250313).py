#print("Hi")
#print("데이터사이언스")

print(1)
print(2)
# print(3)
# print(4) 
## ctrl + kc : 한 번에 주석 처리
## ctrl + ku : 주석 해제
print(5)

print(1+1)
print('1+1')
print("\'안녕\'")
print("내키는190cm야")
print("내키는%d야!" %190)
print("내키는%d야!" %190.5)
#정수: %d, 실수: %f, 문자: %s
print("내키는%f야!" %190.5)
print("내학점은%s야!" %'A+')

print('이름: %s, 영어: %d, 수학: %d' %('임유진', 99, 87))

print(100+100)
print('%d+%d+%d' %(100,100,100+100))
print('100+100')

print(2*3)
print(2**3)
print(4/2)

x = 2
y = 3
print(x+y)
x = 10
print(x+y)
print('%d, %d'%(x,y))
#띄어쓰기도 중요! 띄어쓰기 한 만큼 띄어져서 나옴
print(x,y)
#띄어쓰기 없이 하려면 x,y 이런 식 말고 무조건 %d 써야 함!

print('\"안녕\"')
#\(이스케이프 문자) 뒤에 있는 따옴표는 글자 그대로 출력!
print("\\")
#역슬래시도 마찬가지
print('안녕\n')

print('안\t녕')
#따옴표 안에 있어야 함

print('안녕')
print('나는')
print('안녕\n나는')

price = 100
print(price, '원', '이지롱', sep= '')
print(1,2,3,sep='x')

x = True
y = False
z = "3.2314"
print(  type(z)  )

a = '동덕 '
b = '여대'

print(a,b, sep='')
print(a+b)
print(a*3)

# x = (90 < 100)
# print(x)
# y = (3 > 10)
# print(y)
# print(type(y))
x = 10
y = 10
z = (x == y)
print(z)

score_math = 100
Score_math = 30
#대소문자 구분함!
score_science = 90
print(score_math + score_science)
print(100+90)

# age = input('너 몇살이야?')
# print(age)
# #print(age+10) (안됨)
# #print(age*3) (안됨)
# x = int(age)
# print(x+10)
# x = int( input('너 몇살이야?'))
# print(x+10)

# name = input('이름: ')
# univ_id = input('학번: ')
# print('제 이름은', name, '이고, 제 학번은', univ_id, '입니다.')

print('## 택배를 보내기 위한 정보를 입력하세요.')
name = input('받는 사람을 입력해주세요. :')
house = input('주소를 입력해주세요. :')
weight = int(input('무게를 입력해주세요. :'))
price = weight*5
print('** 받는 사람 ==>',name)
print('** 주소 ==>', house)
print('** 배송비 ==> %d 원' %(price))

# 1
drive = input("드라이브 이름: ")
directory = input("디렉토리 이름: ")
file = input("파일 이름: ")
user = input("확장자: ")

print(">>>완전한 파일이름: %s%s%s%s" %(drive, directory, file, user))

# 2
answer = 25


num = int(input("숫자를 입력하세요: "))

while True:
    if num > answer:
        print("DOWN!")
        num = int(input("숫자를 입력하세요: "))
        continue
    elif num < answer:
        print("UP!")
        num = int(input("숫자를 입력하세요: "))
        continue
    else:
        print("정답!")
        break

# 3
price = int(input("물건 값을 입력: "))
cash = int(input("받은 금액: "))

# res=cash-price
# for i in [500,100,10,1]:
#     n=res//i
#     print(n)
#     res-=n*i

five = (cash - price) // 500
cash = ((cash - (five * 500)))
hund = (cash - price) // 100
cash = (cash - (hund * 100))
ten = (cash - price) // 10
cash = (cash - (ten * 10))
one = (cash - price) // 1

print(five)
print("거스름돈은 아래와 같습니다.")
print("500원 = %d개, 100원 = %d개, 10원 = %d개, 1원 = %d개" %(five, hund, ten, one))

# 4
i = 7

while i > 0:
    print('*' * i)
    i -= 2
    continue

# 5
answer = ['apple', 39, 'music', 568.2, 'Dongduk', 145, 'hello']

A = ['hello', 62, 'umbrella', 145]
B = ['September', 512.3, 'coffee', 39, 'keyboard', 'notebook', 0.5, 'f12']
C = ['computer', 568.2, 39, 'aPple', 'Dongduk', 'water']

res = input("리스트를 입력하세요: ")


if res != 'A' and res != 'B' and res != 'C':
    print("리스트에 없습니다.")

if res == 'A':
    for i in range(len(A)):
        if A[i] in answer:
            print('O', end='')
        elif A[i] not in answer:
            print('X', end='')

if res == 'B': 
    for i in range(len(B)):
        if B[i] in answer:
            print('O', end='')
        elif B[i] not in answer:
            print('X', end='')

if res == 'C':
    for i in range(len(C)):
        if C[i] in answer:
            print('O', end='')
        elif C[i] not in answer:
            print('X', end='')
# ### 학번:

# print('안녕')

# for i in range(5, 16):
#     print(i)


# cnt = 0

# for i in range(135,1698):
#     cnt +=1 ## cnt = cnt + 1

# print(cnt)

# cnt = 0

# for i in range(10):
#     print('a')
#     print('b')
#     print('c')

# print(cnt)

# cnt = 0

# for i in range(10):
#     print('나는 %d살 입니다.' %i)



# cnt = 0

# for i in range(1,11):
#     if i == 10:
#         print(i, end='=')

#     else:
#         print(i, end='+')

# print(55)

for i in range(5):
    print('*' * i)


for i in range(5):
    if i % 2 == 0:
        print('*' * 10)

    else:
        print('*' * 5)

# for i in range(1, 6):
    



### 학번:              이름:


### 예시1 ###
### coding here ###


### 예시2 ###
# for i in range(1, 6) :
#     print('*' * i)

### 예시3 ###

# for i in range(6) :
#     print('*' * (5-i)  )

### 예시4 ###
# for i in range(1,31) :
#     if i % 3 == 0 :
#         print(i)
#     else:
#         print('x')


### 예시5 ###
# num = int(input('2 이상의 숫자를 입력해 주세요 : '))
### coding here ###

# res = 1
# for i in range(1,num+1):
#     res *= i

# print(res)

# -----------------

# res = 0

# for i in range(1,22):
#     res += i

# print(res)

# res = 1

# for i in range(1,11):
#     res = res * i

# print(res)

# --------------

# res1 = 0
# res2 = 1

# for i in range(1, 101):
#     if i % 2 == 0:
#         res1 += i
#     else:
#         res2 *= i

# print(res1,res2)
    
### 예시6 ###


# dan = 1

# dan = int(input('구구단 몇 단을 계산할까요? : '))

# for i in range (1, 10) :
#     print('%d x %d = %d' %(dan, i, dan*i))


### 예시7 ###

# for i in range(2,10):
#     for j in range(1,10):
#         print('%d x %d = %d' %(i, j, i*j))

# --------------------

# for i in range(3):
#     for j in range(5):
#         print(i,j)
#         # print - 15번 출력
#     # print - 3번 출력

# res = 0
# i = 1

# while i < 11:
#     res += i
#     i += 1
# print(res)

# for i in range(1,11):
#     res += i

# print(res)


# --------------------

### 예시8 ###
### coding here ###

# for i in range(5):
#     print('*' * 10)

# i = 0

# while i < 5:
#     print('*' * 10)
#     i += 1

# --------------------

# for i in range(10):
#     print(i)
#     if i > 5:
#         break

# res = 0
# i = 1

# while i < 11:
#     res += i
#     if res > 40: break
#     i += 1
# print(res)

# for i in range(1,11):
#     res += i
#     if res > 40: break

# print(res)

# --------------------

### 예시9 ###
### coding here ###

# ---------------------

# for i in range(1,31):
#     if i % 3 != 0:
#         continue
#     print(i)

# i = 1
# while i < 31:
#     if i % 2 != 0:
#         i += 1
#         continue
#     print(i)
#     i += 1

# -----------------

# res = 0

# for i in range(1,101):
#     res += i

# print(res)

# res = 0
# i = 1
# while i < 101:
#     res += i
#     i += 1
# print(res)


### 예시10 ###
### coding here ###

gcm = 1

for i in range(1, 31):
    if 30 % i == 0 and 75 % i == 0:
        gcm = i

print(gcm)

gcm = 1
i = 1
while i < 31:
    if 30 % i == 0 and 75 % i == 0:
        gcm = i
    i += 1

print(gcm)
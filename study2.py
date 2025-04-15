#1
num = 1
for i in range(1,11,1):
    print(i, end=' ')

#2
a = int(input("1"))

for i in range(1,a+1,1):
    print(i)

#3
b = int(input("2"))

for i in range(1,b+1,1):
    if i % 2 == 0:
        print(i)

#4
c = int(input("3"))

for i in range(1, 10, 1):
    print("%d x %d = %d" %(c, i, c*i))

#5
d = int(input("4"))
plus = 0

for i in range(1, d+1, 1):
    plus += i

print(plus)

#6
for i in range(1,10,1):
    print("%d * %d = %d" %(2, i, 2*i))

#7
e = int(input("5"))

for i in range(1, e+1):
    if e % i == 0:
        print(i)


#8
f = int(input("6"))
g = int(input("7"))

for i in range(f,g+1,1):
    print(i)

#9
for i in range(1,101,1):
    if i % 3 == 0:
        print(i)

# #10
# h = int(input())
# rst = 0

# while h == 0:
#     rst = h * (h-1)
#     h = h-1

# print(rst)

#11
j = int(input())

for i in range(1,j+1,1):
    print('*' * i)

# #12
# for i in range()


#13
k = int(input())

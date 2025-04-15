a, b, c = map(int, input("숫자를 입력하세요.: ").split())

print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)
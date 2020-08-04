'''
연산자
산술연산자, 비교연산자, 할당연산자, 
논리연산자, Bitwise연산자, 멤버쉽연산자, Identity연산자
'''

'''
산술연산자
사칙연산: +,-,*,/
제곱: **
나머지: %
나누기의 소숫점이하 버리기://
등
'''
print(5 % 2)  # 1
print(5 // 2)  # 2

'''
비교연산자 = 관계연산자
등호 ==
같지 않음 !==
부등호 <,>,<=,>= 등
'''
a = 3
if a != 1:
    print("1이 아님")

'''
할당연산자
변수에 값을 할당하기 위해 사용
= 을 사용
'''
a = 1
a = a * 10
a *= 10

'''
논리 연산자
and, or, not
and: 양쪽 값이 모두 참
or: 어느 한쪽만 참
not: 참이면 거짓, 거짓이면 참
'''
x = True
y = False

if x and y:
    print("Yes")
else:
    print("No")    

'''
Bitwise연산자
&(AND), |(OR), ^(XOR), ~(Complement), <<, >>(Shift)
비트 단위 연산때 사용
'''
a = 8 #0000 1000
b = 11 #0000 1011
c = a & b #0000 1000 (8)
d = a ^ b #0000 0011 (3)

print(c)
print(d)

'''
멤버쉽연산자
in, not in
좌측 Operand가 우측 컬렉션에 속해 있는지 확인
'''
a = [1,2,3,4]
b = 3 in a # True
print(b)

'''
Identity연산자
is, is not 
양쪽 Operand가 동일한 Object를 가리키는지 체크
'''
a = "ABC"
b = c
print(b is c) # True

#또 다른 예시
x = ["스타벅스", "커피빈"]
y = ["스타벅스", "커피빈"]

z = x

print(x is z) # True 
print(x is y) # False 같은 데이터 값이지만 다른 객체이기 때문에, 메모리의 위치가 다름
print(x == y) # True 객체의 동일여부x, 데이터 값이 같은지 묻는것


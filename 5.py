# 조건문 : if
# if문은 한 라인에 모두 쓸 수 있으므로 문법상 조건식 뒤에 :(콜론) 사용
x = 9
if x < 10:
    print(x)
    print("한 자리수")

if x < 100: print(x) # 한 라인에 표현

# if문 조건식이 참이 아닐 경우, elif문 사용, 모든 if문이 거짓일 때, else문 블럭 실행
x = 20
if x < 10:
    print("한 자리수")
elif x < 100:
    print("두 자리수")
else:
    print("세 자리 이상")    

# if문 안에서 수행하지 않고 그냥 Skip하기 위해서 pass 사용
n = 17
if n < 10:
    pass
else:
    print(n)


# 반복문
# 반복되는 루프를 만들기 위해 while 또는 for 사용

# while문
# while 키워드 다음의 조건식이 참일 경우 실행
i = 1
while i <= 10:
    print(i)
    i += 1

# for문
# 컬렉션으로부터 하나씩 요소(element)를 가져와, 루프 내의 문장들을 실행 (foreach 와 비슷)
# "for 요소 변수 in 컬렉션" 형식에서 in 뒤에 놓게 됨
sum = 0
for i in range(11): # python 내장 함수 range(n)는 0 ~ n-1까지의 숫자를 갖는 리스트를 리턴. 따라서 0 ~ 10
    sum += i
print(sum)   

list = ["This", "is", "a", "book"] # 문자열 요소를 갖는 리스트로 부터 각 문자열들을 순차적으로 출력
for s in list:
    print(s)

# break / continue
# break 루프 빠져나오기
# continue 루프 블럭의 나머지 문장들을 실행하지 않고 다음 루프로 직접 돌아가기
i = 0
sum = 0
while True:
    i += 1
    if i == 5:
        continue
    if i > 10:
        break
    sum += i
print(sum)    

# range
# ex)
# range(3)  mean: stop  return: 0, 1, 2  >> 0 ~ 2
# range(3,6)  mean: stop, stop  return: 3, 4, 5  >> 3 ~ 5
# range(2,11,2)  mean: stop, stop, stop  return: 2, 4, 6, 8, 10
numbers = range(2, 11, 3)  # (2, 11, n) 2 ~ 10 중 2 + n 출력
for x in numbers:
    print(x)  # 출력: 2, 5, 8

for i in range(10):
    print("Hello")
# 문자열

# ' 혹은 "를 사용하여 표현

s = '가나다'
s = "가나다" 
# 동일한 표현//

s = '''가나다
라마바사
아자차카
'''
print(s)
# 여러 라인의 문자열은 ''' 또는 """ 3개의 인용부호 사용

s = '가나다\n라마바사\n아자차카'
print(s)
# 여러 라인의 문자열을 한 라인으로 표현은 \n 사용
# 즉 위와 동일한 표현

# 문자열 포맷팅
# 일정한 포맷에 맞춰 문자열을 조합하는 것
# 문자열 포맷 템플릿 안에 대입값이 들어갈 자리를 지정해 두고 나주에 그 값을 채워 넣는 방식
# ex)  "내용 %s" % "A" 와 같은 표현에서 % 앞부분은 포맷 템플릿, % 뒤는 실제 대입할 값
# %를 포맷팅 연산자라 부른다.
# %뒤의 값이 복수 일 경우 튜플로 묶어줌
p = "name: %s age: %d" % ("go0space", 65)
print(p)

p = "x = %0.3f, y = %10.2f" % (3.141592, 3.141592) 
# %10.2f 는 전체 10자리이고 값이 적으면 앞에 빈칸을 채우게 되고, .2는 소수점 2째 자리 까지만 표시 :         3.14
# %-10.2f 일 경우 전체 10자리인데 왼쪽으로 정렬 : 3.14
print(p)

# 문자열 클래스 : str
# 인덱스를 사용해서 문자열 중 특정위치의 문자 표현 가능
# 0부터 시작, 따라서 첫번째 문자는 s[0], 두번째 문자 s[1] ...
s = "ABC"
print(type(s))
v = s[1]
print(v)
print(type(s[1]))

path = r'C:\Temp\test.csv'
print(path)
# 문자열을 표현할 때, r'문자열'과 같이 사용하면, 이는 \를 표현하지 않고 
# Raw String을 직접 사용한다는 것을 표현
# ex) windows에서 파일 경로를 간략히 표현하기 위해 사용

# str mathod
# str.join() - 여러 개의 문자열 하나로 결합, Separator(분리기호),를 join 앞에 사용
s = ','.join(['가나','다라','마바'])
print(s)

s = ''.join(['가나','다라','마바'])
print(s)

# str.split()
# join()의 반대
# 특정 separator를 기준으로 문자열을 분리하여 리스트를 리턴
items = '가나,다라,마바'.split(',')
print(items)

# str.partition()
# 문자열을 partition()의 첫 번째 파라미터로 분리하여 앞부분(prefix), 분리자(seprator), 뒷부분(suffix) 등
# 3개의 값을 tuple로 리턴
departure, _, arrival = "Seattle-Seoul".partition('-')
print(departure)

# str.format()
# 가장 많이 사용
# 다양한 방식의 문자열 포맷팅 지원
s = "Name: {0}, Age: {1}".format("go0space",100) # 첫번째 자리는 0 이기 때문에
print(s) # 위치를 기준으로한 포맷팅

s = "Name: {name}, Age: {age}".format(name="go0space", age=100)
print(s) # 필드명을 기준으로 한 포맷팅

area = (10, 20) # 첫번째 자리는 0 이기 때문에
s = "width: {x[0]}, heigth: {x[1]}".format(x = area)
print(s) # object의 인덱스 혹은 키를 사용하여 포맷팅

# bytes
# str 타입의 문자열을 bytes 타입의 바이트들로 변경하기 위해 str 클래스의 인코딩 method encode() 사용
# 반대는 디코딩 method decode() 사용
s = "Hello"
b = s.encode()
print(b)
s2 = b.decode()
print(s2)

# 특정 인코딩 방식 지정
x = "안녕".encode("UTF-8")
y = x.decode("UTF-8")
# 문자열 안에서 유니코드 값을 사용하려면, \n에 이어 유니코드 값을 적으며 된다.
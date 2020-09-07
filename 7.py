# Dictionary(dict)
# Dictionary는 key-value 쌍을 요소로 갖는 컬렉션
# key로 value를 찾는 hash table 구조를 갖는다.
# key는 immutable 타입이어야 하며, value는 Immutable, Mutable 모두 가능
# key로 문자열이나 tuple은 사용 가능, 리스트는 불가능
# Dictionary의 요소들은 {...}를 사용하여 컬렉션 표현
# key:value 쌍으로 되어 있으며, 요소간은 (,)로 구분
# 특정 요소를 찾아 읽고 쓰기 위해서 Dictionary변수[키] 와 같이 키를 인덱스처럼 사용

scores = {"철수":90, "민수":85, "영희":80}
v = scores["민수"]
scores["민수"] = 88

# dict 클래스의 dict() 생성자를 사용할 수도 있다.

# tuple list로 부터 dict 생성
persons = [('김기수', 30), ('홍대길', 35), ('강찬수', 25)]
mydict = dict(persons)

age = mydict["홍대길"]
print(age)

# key=value 파라미터로부터 dict 생성
scores = dict(a=80, b=90, c=85)
print(scores['b'])

# 추가, 수정, 삭제, 읽기
# 수정  Dictionary[키]=새값 해당 키 인덱스를 사용하여 새 값을 할당하면 됨
# 새로운 요소 추가  맵[새키]=새값  새 키에 새 값을 할당
# 삭제  del 요소와 같이 하여 특정 요소 지우기

scores={"철수":90, "민수":85, "영희":80}
scores["민수"]=88
scores["길동"]=95
del scores["영희"]
print(scores)

# 해시테이블 속성-키는 랜덤하게 리턴 (for 루프는 scores 맵으로 부터 키를 하나씩 리턴)
scores={"철수":90, "민수":85, "영희":80}
for key in scores:
    val = scores[key]
    print("%s:%d" % (key, val))

# dict 매소드
scores={"철수":90, "민수":85, "영희":80}

# key
keys = scores.keys()
for k in keys:
    print(k)

#values
values = scores.values()    
for v in values:
    print(v)

# list() 사용 가능
scores={"철수":90, "민수":85, "영희":80}
items = scores.items()
print(items)

itemsList=list(items) """ dict_items를 리스트로 변환 """

# dict.get() 특정 키에 대한 값 리턴
# 키가 없을 경우 none로 리턴
# 키가 존재하는지 체크하기 위해서 멤버쉽 연산자 in 사용
scores={"철수":90, "민수":85, "영희":80}
v=scores.get("민수")
v=scores.get("길동")
v=scores["길동"]

if "길동" in scores:
    print(scores["길동"])

scores.clear()    
print(scores)
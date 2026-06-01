# tuple
# - list 는 mutable하지만 tuple은 immutable하다→변경불가한 list
# - sequence type(indexing, slicing, iterable)
# - 주로 함수 반환 값, 안전한 데이터 집합을 만들 때 사용

print("---tuple ---")
t1=()
t2=(10)# int타입은 변경 불가능
t3 = (10,) # (tuple)(10)
t4 = (10,20,30)
t5 = 10,20 # () 생략 -> 자동 packing
print(t1,type(t1))
print(t2,type(t2))
print(t3,type(t3))
print(t4,type(t4))
print(t5,type(t5))

#tuple 인데싱, 읽기 전용(수정 불가)
tpl = ('a','b','c','d')
print(tpl)
# tpl[0]='A'
# print(tpl[0],tpl[1],tpl[2],tpl[3])
# 수정 불가 확인

#tuple슬라이싱
print('--- tuple 슬라이싱---')
print(tpl[0:2]) #('a','b')
print(tpl[1::2]) #('b','d')

#tuple unpacking
print('--- tuple unpacking---')
q,w,e,r = tpl
print(q,w,e,r)

*r,t = tpl
print(r,t)

#tuple을 이용한 변수 값 할당
print('--- tuple을 이용한 변수 값 할당---')
num1, num2 = 100, 200 #()생략된 tuple
print("num1:",num1) # 100
print("num2:",num2) # 200

print('--- tuple을 이용한 값 교환(swap)---')
num1, num2 = num2, num1
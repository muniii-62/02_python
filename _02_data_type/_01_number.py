# number(숫자형)
# - 정수
# -실수
# -복소수

#type(변수명 | 값) : 변수 또는 값의 타입을 확인하는 파이썬의 내장 함수
# 정수(int) Integer
n = 123
print(n,type(n))

price = 10_000_000 # 정수 자리수 구분
print(price,type(price))

#정수(int) 최대값
import sys
print(sys.maxsize,type(sys.maxsize))

#2진ㅂ넙, 8진법, 16진법
a = 0b100
print(a)

b = 0o23
print(b)

c = 0xff
print(c)

# 실수(float)
f1=123.456
print(f1,type(f1))

f2 = -99999.99999
print(f2,type(f2))

#소수점 아래 16자리 까지 표현 가능
f3 = 1.12345678901234567890
print(f3,type(f3))

#복소수(complex) j로표현
c = 2j
print(c,type(c))

d=3+4j
print(d,type(d))


# 산술 연산(+, -, *, /, //,%(modulo,나머지,**(거듭제곰))

print("---산술연산---")
print(1+2)
print(1-2)
print(1*2)
print(1/2) # 나누어질떄까지의몫
print(1//2)# ->정수역역에서의 몫
print(1%2) # 1 -> 정수영역에서의 나머지

#거듭제곰
print(3**2)# 9
print(3**3) # 27
print(2**63) #int 양의 최댓값


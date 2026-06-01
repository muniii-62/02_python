#논리형 Boolean

a = True
b = False
print(a,type(a))
print(b,type(b))

# 비교 연산
# A > B : A가 B보다 크면 True, 아니면 False
# A >= B : A가 B 이상이면 True, 아니면 False
# A < B
# A <= B
# A == B : A, B가 같으면 True, 아니면 False
# A != B : A, B가 같지 않으면 True


print("1 > 0.5:", 1 > 0.5) # True
print("1 < 0.5:", 1 < 0.5) # False
print("1 >= 0.5:", 1 >= 0.5) # True
print("1 <= 0.5:", 1 <= 0.5) # False
print("1 == 1:", 1 == 1) # True
print("1 != 1:", 1 != 1) # False

#논리 부정 연산(not)
print(not True) #False
print(not not True) # True

# and 연산
# A가 참 이고 B도 참인 경우에 참
# T  and T == T
# T  and T == F
# F  and T == F
# F  and F == F

# 처음부터 F가있으면 뒤에는 계산하지 않음 (속도적인 이점)

print('--- and ---')
print(100> 0 and 1==1)# True
print(30 > 20 and 123 != 123) #False
print(3<=-3 and 12>12) #False
print(9>=9 / 9*9 and 12 !=12+1) # True

a=9>=9 / 9*9
b=12 !=12+1
print(a and b)

# or 연산
# A 또는 B가 True 이면 결과도 True
# <-> A와 B가 모두 False 이면 False

# T  or T == T
# T  or T == T
# F  or T == T
# F  or F == F (중요)

print('--- or ---')
print( 100> 0 or 1==1)# True
print(10 * 10 == 100 or 1 !=1) #True
print(100 == 0 or 10 == 10) #True
print(10 + 20 * 5 == 100 or 30 /10 +5 == 15) # False

# 합격(true) / 불합격(False)
# 60점 이상입력 시 합격(True) / 아니면 불합격(False)
print('--- 합격/불합격 ---')
# input() 합수 : 키보드 입력을 받는 함수 (str로 저장)
# int()함수: str->int로 변환
score = int(input('점수를 입력하세요: '))
print(score,type(score))

result = score >= 60
print("합격여부:",result)

# print("합격 여부: ", result)
print("합격 여부 : ", '합격' if result == True else '불합격')
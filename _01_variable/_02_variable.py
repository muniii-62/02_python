# 변수(variable)
# - 값(literal) 을 저장하는 메모리 상의 공간
# - 각 변수마다 이름이 지정되어 있음( 이름을 불러서 사용)

#[변수 선언 방법]
# 변수명 = 값
a = 10 #a라는 메모리상의 공간에 10(literal)을 대입
b = '홍길동'

print("a=",a)
print("b=",b)

# 대입 연산자(=)
# - 우항의 값을 좌항의 변수에대입 (무조건 !!)
num = 100
print("num=",num)

#변수는 저장된 값이 변할 수 있따.
num = 900
print("num=",num)

num="abcde"
print("num=",num)

#변수 명명 규칙
# 1. 의미 있는 이름 사용
# 2. 변수명은 snake case를 사용(소문자 + _)
# 단 대문자도 사용은 가능하고 - 소문자와 구분된다

team_name = "오지라퍼스"
print(team_name)    # 오지라퍼스

Team_name = "Ohgiraffers"
print(team_name)    # 오지라퍼스
print(Team_name)    # Ohgiraffers

#한글로도가능은하다 But 인코딩문제로 권장하지 않음
밥조 ="3조"
print("밥조:",밥조)

# 변수명은 숫자로 시작해서는 안된다.(문법 오류 == 빨간줄)
name_1 = "콩쥐"
# 1_name = "팥쥐" #문법 에러
_1_name = '신데렐라'

# 특수문자는 언더스코어(_)제외하고 사용 불가
# tea-name = "오지라퍼스" # 에러
# team@name='오지라퍼스' ->안된다

# 예약어는 변수명으로 사용 불가
# if, for, else, while, elif 등등
import keyword
print(keyword.kwlist) #얘네들이 예약어들

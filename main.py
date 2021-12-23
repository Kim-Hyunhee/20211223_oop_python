# 동작을 어떻게 해야하는지 정리하는 코드

print('책방 관리 프로그램을 시작합니다.')

def add_two_numbers(num1, num2):
    print('두 개의 숫자를 더하는 함수 실행됨')
    result = num1 + num2
    return result

a = add_two_numbers(5, 2)   # 함수에 return이 있다면 그 결과를 변수에 담거나 print 등으로 일반 변수처럼 활용 가능

print(a)

b = add_two_numbers(10, 4)  # => 함수가 위에 있어야 그걸 활용할 수 있다.

print(b)

print(f'11과 15의 합은 {add_two_numbers(11,15)} 입니다.')


# 결과가 없는 함수 예시

def print_my_name(my_name):
    print(f'제 이름은 {my_name} 입니다.')
    
print_my_name('김현희')


# 파라미터가 없는 함수 예시

def get_my_age():
    return 28

age = get_my_age()
print(age)

# 뺄셈 수행 함수 => 파라미터의 대입 순서가 중요한 함수
def minus_two_numbers(num1, num2):
    return num1 - num2

#어느 파라미터에 어떤 값 대입 직접 지정
# 파라미터의 순서와 관계 없다.
result01 = minus_two_numbers(num2 = 7, num1 = 10)
print(f'뺄셈 함수 사용 결과 : {result01}')
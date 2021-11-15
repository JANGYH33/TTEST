#클로져 (closure) : scope에 제약을 받지 않는 변수들을 포함하고 있는 코드블록이다.
# 함수 내의 지역변수를 함수 밖에서 참조를 가능하게 함
from pack1.test10For import aa
from sympy.physics.units import amount

#선행학습

def funcTimes(a,b):
    c = a * b
    #print(c)
    return c

print(funcTimes(2, 3))
kbs = funcTimes(2, 3)
print(kbs)

kbs = funcTimes
print(kbs)
print(kbs(2, 3))
print(id(funcTimes), id(kbs))

del funcTimes

print(kbs(2, 3))

# aa = 10
# print(aa, id(aa))
# del aa
#
# # print(aa) # NameError: name 'aa' is not defined

mbc = sbs = kbs # 주소 치환
print(mbc(3,4))
print(sbs(3,4))

print()
print('--클로저를 사용하지 않은 경우--------')


def out():
    count = 0
    def inn():
        nonlocal count
        count += 1
        return count
    print(inn())
    
#print(count) # NameError: name 'count' is not defined
out()
out()
out()


print('--클로저를 사용한 경우--------')

def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner # <== 요게 바로 클로저 : 내부함수의 주소 반환

#print(outer())

var1 = outer()
print(var1())
print(var1())
print(var1())
print()
var2 = outer()
print(var2())
print(var2())
print()

print(id(var1), id(var2))


print('수량 * 단가 * 세금을 출력하는 함수 작성 ------')

def outer2(tax): # tax는 지역변수
    def inner2(su, dan):
        amount = su * dan * tax
        return amount
    return inner2 # <== 요게 바로 클로저

# 1분기에는 tax(세금)가 0.1로 부과 
q1 = outer2(0.1)
result1 = q1(5, 50000)
print('result1 : ', result1)

result2 = q1(2, 10000)
print('result2 : ', result2)

print()
# 2분기기에는 tax(세금)가 0.1로 부과 
q2 = outer2(0.05)
result3 = q2(5, 50000)
print('result3 : ', result3)

result4 = q2(2, 10000)
print('result4 : ', result4)















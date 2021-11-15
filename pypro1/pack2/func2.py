# 함수 작성

"""
def 함수명([매개변수...):
    수행문
    ...
    [return 반환값]
    
함수명([인수...])

"""
# 파이썬은 모듈 단위로 처리하고 파일로 저장
from conda.cli.common import arg2spec
a = 1
print(a)

def doFunc1():
    print('doFunc1 수행')

def doFunc2(arg1, arg2):
        result = arg1 + arg2
        print(result)
    
print( '뭔가를 하다가 함수 호출')
doFunc1()

print( '뭔가를 하다가 함수 호출2')
doFunc1()

print( '뭔가를 하다가 함수 호출3')
doFunc2(10, 20)
doFunc2('파이썬','만세')
# doFunc2('파이썬',7) 에러 문자 + 숫자는 불가능 *자바는 가능
doFunc2('파이썬',str(7))


def doFunc3(arg1, arg2):
    imsi = arg1 + arg2
    if imsi % 2 == 1:
        return #빈손으로 함수 탈출
    else:
        return imsi
    
    print('처리') # 처리 못함(주의

print(doFunc3(5,6))
print(doFunc3(5,3))
bb = doFunc3(5,3)

print('bb의 결과는 ', bb)

print()


def area_tri(a,b):
    c = a * b / 2
    area_print(c) # 함수가 다른 함수 호출

def area_print(c):
    print('삼각형의 면적은 ', c)
    
area_tri(10,20)
 
print()
def swap(a,b):
    return b, a # return (b,a)와 동일

a = 10; b = 20

cc = swap(a,b)
print(cc)

print()
print()

def isodd(arg):
    return arg % 2 == 1

print(isodd(11))
print(isodd(10))
   
    
#if 조건식에서 함수 사용

myDict = {x:x*x for x in range(11) if isodd(x)}
print(myDict)

    








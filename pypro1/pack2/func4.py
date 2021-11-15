# 함수 인수(argument)와 매개변수(parameter) 키워드로 매칭

def showGugu(start, end = 5):
    for dan in range(start, end + 1):
        print(str(dan) + '단 출력')
        
showGugu(2, 3)
print()
showGugu(3)
print()

showGugu(start = 7, end = 8) #이름으로 매칭
print()

showGugu(end = 8, start = 7)
print()

showGugu(5, end = 6)
print()


#showGugu(start = 5, 6) # SyntaxError: positional argument follows keyword argument
#showGugu(end = 7, 6) # SyntaxError: positional argument follows keyword argument

print('\n 가변인수 처리 ----')

def func1(*ar): # tuple type으로 처리
    print(ar)


func1('비빔밥')
func1('비빔밥', '김밥' , '공기밥')

print()
def func2(a, *ar): #tuple type으로 처리
    print(a)
    print(ar)
 
func2('비빔밥')
print('-------------')
func2('비빔밥', '김밥' , '공기밥')

print()

def selectProcess(choice, *ar):
        if choice == 'add':
            imsi =0
            for i in ar:
                imsi += i
        elif choice == 'mul':
            imsi = 1
            for i in ar:
                imsi *= i
        
        return imsi

print(selectProcess('add', 1,2,3,4,5))
print(selectProcess('mul', 1,2,3,4,5))


print()


def func3(w, h, **other): # **은 dict type인 경우
    print('몸무게: {}, 키: {}'.format(w,h))
    print(other)

func3(66, 177)
func3(66, 177, irum = '홍길동', nai = 23)




    
    
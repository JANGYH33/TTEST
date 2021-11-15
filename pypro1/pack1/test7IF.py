# 조건 판단문 IF
# 파이썬의 경우 띄어쓰기를 인식하기때문에 구분을 잘 해야함.
var = 5

if var >=3:
    print('크구나')
    print('참일 때')
    #pass
else:
    print("거짓일 때")
      
print('end1')

print()

money = 1000
age = 23

if money >= 500:
    item = '사과'
    if age <= 30:
        msg = "와우 젊다"
    else:
        msg = '허걱 나이가 있네'
else:
    item = '감'
    if age <= 30:
        msg = "성인"
    else:
        msg = '미성년'
        
print(item, msg)
print('end2')       


print()

jumsu = 85

if jumsu >= 90:
    print('우수')
else:
    if jumsu >= 70:
        print('보통')
    else:
        print('저조')
        
if jumsu >= 90:
    print('우수2')
elif jumsu >= 70: # java : elseif
    print('보통2')
else:
    print('저조2')
    
print('end3')

print()


print(3 + 2, str(3) + '2', int(str(3)) + 2) #str() , int() 형변환

# jum = int(input('점수 입력'))

#print(jum, type(jum))
jum = 30
if jum >= 90:
    print('good')
elif jum >= 70:
    print('nice')
else:
    print("nomal")

print()

if 90 <= jum <= 100:
    print('2good')
elif 70 <= jum < 90:
    print('2nice')
else:
    print('nomal2')

print()
            
names = ['홍길동', '신선해', '이겨라']
if '고길동' in names: # not in
    print('맞아 내친구')
else:
    print('뉘구?')
    
    
print()

#변수 선언시 if문을 통해 참이면 왼쪽을 실행하고 거짓이면 오른쪽을 실행
a = 'mbc'
b = 9 if a == 'kbs' else 11

print (b)

print()

a = 3 

if a < 5:
    print(0)
elif a <10:
    print(1)
else:
    print(2)
    
#코드를 한줄로
print(0 if a < 5 else 1 if a < 10 else 2)
print()

a = 5
result = a * 2 if a > 3 else a + 2
print('result : ' + str(result))












        
        
        
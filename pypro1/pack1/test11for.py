#range 함수 : 수열 생성

print(list(range(1,6)))
print(list(range(6)))
print(list(range(1,6,1)))
print(list(range(1,6,2)))
print(tuple(range(1,6)))
print(set(range(1,6)))

print()
for i in range(6):
    print(i, end = ' ')

print()
for i in range(6):
    print('hi', end = ' ')
    
print()

print('\n1 ~ 10까지의 합')
tot = 0
for i in range(1,101):
    tot += i
    
print('결과는 ', tot)
print('결과는 ' ,sum(range(1,101)))


print()
for i in range(2,10):
    for j in range(1,10):
        print('{}*{}={}'.format(i, j, i * j), end = ' ')
    print()

#문1) 반복문 for를 이용 : 1 ~ 100 사이의 정수 중 3의 배수이면서 5의 배수의 합, 건수 출력

#등급 맞추기 end for와 같이 따로 종료가 없으므로 라인을 맞춰줘야 함
total = 0
count = 0
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        total += i        
        count += 1

print('합계 =' , total , '건수 :', count)


#문2) 주사위를 두 번 던져서 숫자들의 합이 4의 배수가 되는 경우만 출력
# 1 3
# 2 6


for i in range(1,7):
    for j in range(1,7):
        if (i + j) % 4 == 0:
            print( i ," ", j)





for i in range(6):
    n1 = i + 1
    for j in range(6):
        n2 = j + 1
        n = n1 + n2
        if n % 4 == 0:
            print(n1, ' ', n2)




















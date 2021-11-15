# 연산자

v1 = 3 # 치환

v1 = v2 = v3 = 5

print(v1, v2, v3)

print('출력1', end = ' ')
print('출력2')
print('출력3')

v1 = 1, 2, 3
print (v1)

v1, v2 = 10, 20
print (v1, v2)
print (v1)

v2, v1 = v1, v2
print (v1, v2)
print (v1)


print('여기는어디야------------------------------------')
v1, *v2 = 1,2,3,4,5 # packing 연산
print (v1,v2)
print ('성공')

*v1, v2, v3 = 1,2,3,4,5 # packing 연산
print (v1,v2,v3)
print ('성공')


print('----------')

print (5 + 3, 5-3, 5 * 3, 5/3)
print (5 //3, 5 % 3) # 몫, 나머지
print (divmod(5, 3))
print ( 5 ** 2)

print ('연산자 우선순위 : ', 3 + 4 * 5, (3 + 4) * 5)

print('--관계 연산-------')

print ( 5 > 3, 5 >= 3, 5 == 3, 5 != 3)

print ('-------논리연산-------')

print (5 > 3 and 4 < 3, 5>3 or 4<3, not(5>=3))

print ('--------문자열 연산----')

print ('한' + "국인" + ' 만세' )
print ('한국' + '한국'+ '한국'+ '한국'+ '한국')
print ('한국' * 5)

print('***' * 20)
print( '누적')


a = 10
a = a +1
a += 1
#a++ error
#++a #부호 변경
print (a)

print ('부호 변경')
print (a, a* -1, -a , +a, --a)

print('-------불린형--------')

print(True, False)

#0이거나 값이 없으면 False 있으면 True
print(bool(1), bool(3.5), bool('ok'))
print(bool(0), bool(0.0), bool(''), bool(None), bool([]) , bool({}), bool(set()))

print('-----이스케이프 문자------')
print ('aa\bb')
print ('mbc\nbc')
print ('c: \tbc\tbc')
print (r'aa\bb')
print (r'mbc\nbc')
print (r'c:\tbc\tbc')

print ('\n 출력 서식 연습')
print (1.5678)
print (format(1.5678, '10.3f'))

print('나는 나이가 %d이다' %23 )
print('나는 나이가 %s이다' %'스물셋' )
print('나는 나이가 %f이다' %26 )
print('나는 나이가 %d이고 이름은 %s. 나이:%d'%(23, '홍길동', 22))


print()
print ('이름은 {}, 나이는{}'.format('이기자',25))
print ('이름은 {0}, 나이는{1}'.format('이기자',25))
print ('이름은 {1}, 나이는{0}'.format('이기자',25))
print ('이름은 {0}, 나이는{1} {0}'.format('이기자',25))



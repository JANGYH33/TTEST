# 반복문 for 

for i in [1,2,3,4,5]:
    print(i, end = ' ')
    
print()

# colors = ['r', 'g', 'b'] # list
# colors = ['r', 'g', 'b'] # tuple
colors = ['r', 'g', 'b'] # set

for c in colors:
    print(' 색은 %s'%c, end = ' ' )
    
print()

soft= { 'java' : '웹용언어', 'python' : '만능언어' , 'c' : '시스템개발용'} #dict

for i in soft.items():
    # print(i) #('java', '웹용언어') ....
    print(i[0] + ' ' + i[1]) # java 웹용언어 ...
    
print()

for k in soft.keys():
    print(k, end = ' ')

print()

for v in soft.keys():
    print(v, end = ' ')


print()

for a, b in soft.items():
    print(a, ' , ', b)


print('평균, 분산 표준편차 ------')

jum = [6,5,4,7,3,5]
tot = 0

for i in jum:
    tot += 1
    
    avg = tot / len(jum)
    print ('avg =', avg)

print('구분선-----------')
tot = 0

for i in jum:
    tot += (i-avg) **2
    var = tot / len(jum)
    print('var :', var)

import math
print('std : ', math.sqrt(var))

print()

for n in [2, 3]:
        print('{}단'.format(n))

        for su in [1,2,3,4,5,6,7,8,9]:
            print('{0} * {1} = {2}'.format(n, su, n*su))
            

print('------------구분선')

li = ['a','b','c']
for idx, data in enumerate(li):
        print(idx, ' ', data)
        
print('continue, break -----')
datas = [1,2,3,4,5]
for i in datas:
    if i == 2:continue
    print(i, end = ' ')
else: # 선택적 명령어
    print('정상 처리')
            
print('------------구분선')
            
li1 = [3,4,5]
li2 = [0.5, 1,2]
for a in li1:
    for b in li2:
        print(a + b, end = ' ')


print()

results = [a + b for a in li1 for b in li2]
#print(result)
for d in results:
        print (d, end= ' ')


print('정규표현식, for 사용 연습 : 다량의 문자열을 공백 단위로 분리해 건수 출력')
import re
#웹에서 스크래핑 했다고 가정

ss = '''
영국 일간 가디언은 28일 “오징어 게임, 전 세계를 사로잡은 지옥 같은 호러쇼”라는 제목의 기사를 통해 돌풍의 배경을 분석했다. 가디언은 “이 드라마는 넷플릭스 미국 순위 1위를 차지한 최초의 한국 프로그램으로, 영국에서도 현재 1위에 올라 있다. 살인이 나오는 디스토피아(어두운 미래상) 장르물 ‘헝거 게임’이나 ‘배틀로얄’에 푹 빠진 세대에게 이러한 성공은 놀라운 일이 아니다”고 했다.

이어 ‘기생충’을 언급하면서 두 작품 모두 완전히 분리된 두 계층이 등장한다는
 점을 지적했다. 가디언은 “작품 속 살인 게임이 끔찍하다고 해도, 끝없는 빚에 시달려온 이들의 상황보다 얼마나 더 나쁘겠는가. 등장인물의 과거를 다룬 에피소드는 모두가 불운 끝에 빚을 지게 될 수 있음을 알려준다”고 했다.

프랑스 BFM 방송도 “넷플릭스 상위 10위 안에 이름을 올린 최초의 한국 시리즈가 비평가들과 시청자들을 깜짝 놀라게 했다”며 “오징어 게임은 처음부터 끝까지 긴장감을 유지하며 매우 자세하게 쓰였으며, 영화에서 보기 드문 잔인함을 보여준다”고 설명했다.

BFM은 아울러 “방탄소년단(BTS)부터 영화 기생충, 웹툰까지 한국 문화가 이렇게 전 세계적으로 퍼져 인기를 끌었던 적이 없었다”고 덧붙였다.
'''
   
#print(ss)

ss2 = re.sub(r'[^가-힣\s]','', ss)

print(ss2)         
            
ss3 = ss2.split(' ')
print(ss3)

cou = {} # 단어 횟수를 dict로 적장

for i in ss3:
        if i in cou:
            cou[i] += 1 # 같은 단어가 있으면 누적
        else:
            cou[i] = 1
print(cou)            

print( '\ndict type(사진형)의 변수로 과일 값 계산')

price= {'사과' :2000, '감' :500, '배' : 3000} # 개당 가격
gogek_tom = {'사과':2, '배':3} #손님이 구매한 과일 갯수

bill = sum(price[f] * gogek_tom[f] for f in gogek_tom)
print('과일 값 총액 : {}원'.format(bill))

print('\nfor 문 한줄로 코딩하기')

a = 1,2,3,4,5,6,7,8,9,10
li = []
for i in a:
        if i % 2 == 0:
            li.append(i)
print (li)
#위 코드를 한 줄로 표현
print(list(i for i in a if i % 2 ==0))

print('--------구분선')

datas = [1,2, 'a', True, 3.5]
li = [ i * i for i in datas if type(i) == int]
print(li)

datas = {1,1,2,2,3} # set은 중복 불가

li2 = [i * i for i in datas]
print(li2)



print()
id_name = {1:'tom', 2: 'james'}
name_id = {val:key for key, val in id_name.items()}
print(name_id)

print()
aa = [(1,2), (3,4), (5,6)]
for a,b in aa:
    print(a+b)















    



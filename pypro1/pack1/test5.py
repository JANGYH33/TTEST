# tuple : list와 유사하나 읽기전용 - 속도가 빠름
# t = (1,2,3,4,3)

t = 1,2,3,4,3


print(t, type(t), len(t))
print(t.count(3), t.index(4))

print(t[0], t[0:3])

#t[0] = 10 TypeError: 'tuple' object does not support item assignment
# 읽기 전용이므로 변경 X


imsi = list(t)
print (imsi, type(imsi))

#-------------------------




#---------------------------------
#set 순서x, 중복x

a = {1,2,3,1}

print(a, type(a), len(a))
# print(a[0])

b = {3, 4}
print (b)
#print(a+b) # error

print(a.union(b))
print(a.intersection(b))
print( a | b, a - b, a & b)

a.update({6,7})
print (a)
a.remove(6)
print(a)

li = [1,2,2,3,2,1]
print(li)
s = set(li)
li = list(s)
print(li)


print('---' * 10)
#dict : 순서 x 키:값의 쌍으로 구성

mydic = dict(k1 = 1, k2 = 'mbc' , k3 = 3.4)
print(mydic, type(mydic))

dic = { '파이썬' : '뱀', '자바':'커피', 'spring':'용수철', 'kbs' : 9}
print(dic, type(dic), len(dic))

print(dic['자바'])

# print(dic['커피']) # KeyError : '커피'
dic['오라클'] = '예언자'
print(dic)

del dic['오라클']
print(dic)

dic.pop('자바')
print(dic)

dic['spring'] = '웹용프레임워크'
print(dic)

print(dic.keys())
print(dic.values())
print(dic.get('파이썬'))

print('spring' in dic)
print('summer' in dic)










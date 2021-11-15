# 정규 표현식

import re


ss = "1234 abc가나다ABC_555_6Python is fun. 123123"

print(ss)

print(re.findall('123', ss))
print(re.findall('가나', ss))
print(re.findall('5', ss))
print(re.findall('[0-9]', ss))
print(re.findall('[0-9]+', ss))
print(re.findall('[a-z]+', ss))
print(re.findall('[a-zA-Z0-9]+', ss))
# ' ' 띄어쓰기 시 공백도 인식
print(re.findall('[가-힝0-9 ]+', ss))
# ^는 부정
print(re.findall('[^가-힝0-9 ]+', ss))

print(re.findall('^1+', ss))
print(re.findall('3$', ss))
print()

print(re.findall(r'\d',ss))
print(re.findall(r'\d+',ss))
print(re.findall(r'\d{1,3}',ss))
print(re.findall(r'\d{2}',ss))



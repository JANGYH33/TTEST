# file io

import os


print(os.getcwd()) # 파일 위치를 알 수 있다


try:
    print('파일 읽기 ---')
    #f1 = open(r'C:\work\psou\pypro1\pack5file\ftest.txt', mode = 'r', encoding='utf-8')
    #f1 = open(os.getcwd()) + r
    f1 = open('ftest.txt', mode = 'r' , encoding = 'utf-8')
    
    print(f1)
    print(f1.read())
    f1.close()
    
except Exception as e:
    print('파일 처리 오류 : ', e)
    
try:
    print('파일 저장----')
    f2 = open('ftest2.txt', mode = 'w', encoding ='utf-8') # 파일의 저장
    
    f2.write('My Friend\n')
    f2.write('홍길동, 신기해')
    f2.close()
    print('저장 성공')
    
    f2_1 = open('ftest2.txt', mode = 'a', encoding ='utf-8') #파일의 내용 추가
    f2_1.write('\n 오공')
    f2_1.write('\n 팔계')
    f2_1.write('\n 오정')
    f2_1.close()
    
    f3 = open('ftest2.txt', mode = 'r', encoding ='utf-8') # 파일의 읽기 
    print(f3.read())
    f3.close
    
    print('한 줄 씩 읽기')
    f4 = open('ftest2.txt', mode = 'r', encoding ='utf-8') # 파일의 한 줄 씩 읽기 
    print(f4.readline())
    print(f4.readline())
    print(f4.readline())
    print(f4.readline())
    
except Exception as e :
    print('파일 오류 ' , e)    
    
    
    
    
    
    
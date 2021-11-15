#예외처리 : 파일, 네트워크, 키보드,. db연동, 나누기.....등의 작업을 핟가ㅏ 에러가 발생한 경우 대처하기

def divide(a, b):
    return a/ b

#c = divide(5, 2)
# c = divide(5, 0)      # 그냥 실행시 ZeroDivisionError: division by zero
#
# print(c)


# 에러에 대한 대처 작업 : try ~ except

try:
    kbs = 9
    
    c = divide(5,2)
    #c = divide(5,0)
    print(c)
    
    aa = [1,2]
    print(aa[0])
    #print(aa[5])
    
    f = open('c:/work/abc.txt')
    
except ZeroDivisionError:
    print('두 번째는 0 쓰지마')
except IndexError as e:
    print('참조 범위 오류 :', e)
except Exception as e:
       print('에러 발생 :' , e)     

finally:
    print('에러에 상관없이 반드시 수행됨')
    del kbs
        
print('다음 작업 계속')
# 다른 모듈에서 호출 될 사용자 정의 모듈

tot = 100

def listTotal(*ar):
    print(ar)
    print('리스트 토탈 함수 실행')
    
def abc():
    if __name__ == '__main__':
        print('메인 이야~~~')
        
    
def kbs():
    print("대한민국 kbs")
    
def mbc():
    print("무한도전")
    
    
# 다중상속 : 가전제품의 소리조절 기능(메소드)의 이름을 동일하게 주고 다형성 처리


class ElecProduct:
    volume = 0
    
    
    def volumeControl(self, volume):
        pass
    
    
class ElecTv(ElecProduct):
    
    def volumeControl(self, volume): # 오버 라이딩
        self.volume += volume 
        print('TV 소리 크기 : ', self.volume)
        

class ElecRadio(ElecProduct):
    def volumeControl(self, volume): # 오버라이딩
        vol = volume
        self.volume += vol
        print('라디오 소리 크기 : ', self.volume)
        
    def showProduct(self):
        print('라디오 고유 메소드')
        
tv = ElecTv()
tv.volumeControl(5)
tv.volumeControl(-2) 

print()

radio = ElecRadio()

radio.volumeControl(7)
radio.volumeControl(2)
radio.showProduct()




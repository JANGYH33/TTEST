# 부품을 별도의클래스를 작성

# 핸들

class PohamHanldle:
    quantity = 0 # 회전량
    
    def leftTurn(self, quantity):
        self.quantity = quantity
        return '좌회전'
    
    def rightTurn(self,quantity):
        self.quantity = quantity
        return '우회전'
    
    

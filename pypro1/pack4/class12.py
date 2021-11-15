# 추상 클래스 : 추상메소드를 가지고 있는 클래스


from abc import *
from anaconda_project.internal import metaclass


class TestClass(metaclass = ABCMeta): #추상 클래스가 됨. TestClass 타입의 객체 생성 불가
    @abstractclassmethod
    def abcMethod(self): #추상 메소드
        pass
    
    def normalMethod(self):
        print('추상 클래스 내의 일반 메소드')
        
        

#parent = TestClass() #TypeError: Can't instantiate abstract class TestClass with abstract methods abcMethod

# class Child1(TestClass):
#     pass
#
# c1 = Child1() # TypeError: Can't instantiate abstract class Child1 with abstract methods abcMethod


class Child1(TestClass):
    name = '난 child1 멤버 변수'

    def abcMethod(self): # 메소드 오버라이드 강요당함
        print('추상 메소드를 오버라이드 함. 추상의 마법에서 풀림')

c1 = Child1()

print(c1.name)
c1.abcMethod()
c1.normalMethod()

print('--------' * 10)

class Child2(TestClass):
    def abcMethod(self): # 강요
        print('추상 메소드를 Child2에서도 오버라이드 함')
        print('추상 메소드의 위력을 감상중')
    
    def normalMethod(self):# 선택
        print('추상 클래스 내의 일반 메소드는 해도 되고 안해도 되고 내맘니맘')


c2 = Child2()
c2.abcMethod()
c2.normalMethod()

print('--------다형성------')

mbc = c1
mbc.abcMethod()
print()
mbc = c2
mbc.abcMethod()




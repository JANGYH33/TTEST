# 메소드 오버라이드를 이용해 다형성 구사


class Parent:
    def print(self):
        pass
    
class Child1():
    def printData(self):
        print('Child1에서 override')
        
class Child2():
    def printData(self):
        print('Child2에서 재정의')
        print('부모 메소드와 동일한 이름을 가지나 기능은 다ㅡㄹ다')

    def aa(self):
        print('Child2 고유메소드')
        
c1 = Child1()
c1.printData()

print()

c2 = Child2()
c2.printData()


print( '다형성 : 동일한 명령문이나 기능은 다름-------')

#par = Parent() 
par = c1 # 자식의 객체변수를 치환할 때 꼭 부모 객체변수에 치환할 필요가 없다 일반 변수에 치환하면 된다
c1.printData()

print()

par = c2
c2.printData()

print('------------')

plist = [c1,c2]
for i in plist:
    i.printData()
    print()

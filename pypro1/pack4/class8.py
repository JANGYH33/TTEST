# 상속

class Person:
    say = '나는 사람~'
    nai = 20
    __abc = 'good' # private 멤버변수 ( 현재 클래스에서만 유효 
       
    def __init__(self, nai):
        print('Person 생성자')
        self.nai = nai
    
    def printInfo(self):
        print('나이:{}, 이야기:{}'.format(self.nai, self.say))


    def hello(self):
        print('안녕')
        print(self.__abc)
        
print(Person.say, Person.nai)

#Person.printInfo() # AttributeError: type object 'Person' has no attribute 'printInfo'

p = Person('22')

print(p.say, p.nai)
p.printInfo()
p.hello()


print('***' * 10)

class Employee(Person):
    say = '일하는 동물'
    subject = '근로자'
    def __init__(self):
        print('EmpLoyee 생성자')

    def printInfo(self): # 메소드 오버라이드
        print('Employee 클래스에서 오버라이드한 printinfo')
#자식에서 찾아다가 없으면 부모에게 올라감.

    def e_printInfo(self):
        self.printInfo()
        super().printInfo() #이건 처음부터 부모 메소드를 호출한다.
        print('self',self.say, 'super',super().say)
        
e = Employee()

print(e.say, e.subject)
e.printInfo()
e.e_printInfo()


print('~~~~' * 10)

class Worker(Person):
    
    def __init__(self, nai):
        print('워커 생성자~~')
        super().__init__(nai) # 부모 클래스의 생성자 호출. bound method call
    
    def w_printInfo(self):
        self.printInfo()
    
w = Worker('25')

print (w.say, w.nai)

w.w_printInfo()
    
print('^^^^' * 10) 

class Programmer(Worker):
    def __init__(self, nai):   
        # super().__init(nai) # 아래처럼 쓸 수 있다.
        Worker.__init__(self, nai) # 부모 클래스의 생성자 호출. unbound method call
        
    def p_printInfo(self):
        self.printInfo()
        
pr = Programmer('33')
print(pr.say, pr.nai)
pr.p_printInfo()
  

print('-----클래스 타입 확인----------')

a = 10; print(type(a))

print(type(pr))
print(type(w))
print(Programmer.__base__) 
print(Worker.__base__) 
print(Person.__base__) 

    






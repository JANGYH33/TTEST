

from abc import *
from math import *
class Employee(metaclass = ABCMeta):
    
    def __init__(self,name,nai):
        self.name = name
        self.nai = nai
           
    def irumnai_print(self): # 일반 메소드
        print('이름 : ', self.name , '나이 :' ,self.nai)
            
    @abstractclassmethod
    def pay(self, pay):
        pass
    @abstractclassmethod
    def data_print(self, data_print):
        pass
    
class Tempoary(Employee):
    
    def __init__(self, name, nai, ilsu, ildang):
        Employee.__init__(self, name, nai)
        self.ilsu = ilsu
        self.ildang = ildang
    
    
    def pay(self):  #추상
        return self.ilsu * self.ildang
    def data_print(self): #추상
         print('이름 : ', self.name , '나이 :' ,self.nai 
              ,'월급은 : ', self.pay())
        

class Regular(Employee):
    def __init__(self, name, nai, salary):
        Employee.__init__(self, name, nai)
        self.salary = salary

    def pay(self):  #추상
        return self.salary
    def data_print(self): #추상
        print('이름 : ', self.name , '나이 :' ,self.nai 
              ,'급여 : ', self.pay())
        
class Salesman(Regular):
    def __init__(self, name, nai, salary,sales,commission):
        Regular.__init__(self, name, nai, salary)
        self.sales = sales
        self.commission = commission
    def pay(self):  #추상
        return self.salary + trunc(self.sales * self.commission)
    def data_print(self):
                print('이름 : ', self.name , '나이 :' ,self.nai 
              ,'수령액 : ' , self.pay() )



t = Tempoary('홍길동',25,20,1500000)
r = Regular('한국인',27,3500000)
s = Salesman('손오공',29,1200000,5000000,0.25)

t.data_print()
r.data_print()
s.data_print()





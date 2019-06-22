class Employee:
    raise_amount=100

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay

    @property
    def name(self):
        return (self.first+' '+self.last)

    @name.setter
    def name(self,name):
        self.first,self.last=name.split(' ')

    @name.deleter
    def name(self):
        print("Name deleyed!!!")
        self.first=None
        self.last=None

    def new_pay(self):
        self.pay+=self.raise_amount

    @classmethod
    def set_raise(cls,amt):
        cls.raise_amount=amt
    @classmethod
    def from_string(cls,string):
        first,last,pay=string.split('-')
        return cls(first,last,pay)

class Developer(Employee):
    raise_amount = 900
    def __init__(self,first,last,pay,prog):
        super().__init__(first,last,pay)
        self.prog=prog

    def __repr__(self):
        return ("Developer(%s ,%s ,%s)" %(self.first,self.last,self.pay))
    def __add__(self, other):
        return (self.pay + other.pay)

#emp1=Employee('Sam',pay=600,last='Lakhotia')
#emp2=Employee('ABC','DEF',100)


#emp1.raise_amount=2000
#Employee.set_raise(1212121)
emp1=Developer('Ron','Hardy',8000,'Python')
emp2=Developer('n','rdy',1000,'Python')

emp1.name='gaga jlkjhda'

print(emp1.name)

del emp1.name

print(emp1.first)

print(emp1.last)




#print(emp1)

#print(emp1.first)
#print(emp1.prog)
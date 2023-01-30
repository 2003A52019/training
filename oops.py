#!/usr/bin/env python
# coding: utf-8

# INHERITANCE
# 1.Single
# 2.Multiple
# 3.Multilevel
# 4.Hierarchial
# 5.Hybrid

# In[1]:


#1. single inheritance(1 parent and one child)

#create a parent class
class Animal:
    def speak(self):
        print("this is animal class and speak method")
class Dog(Animal):#inheritance of animal class in dog class
    def bark(self):
        print("this is dog class and bark method")
        
        
        
#Instatiation of child class i.e dog

d=Dog()

#access the datamember of parent class and self class

d.speak()
d.bark()

#Instatiation of parent class i.e parent

a=Animal()
a.speak()

#we can't access the attribute of child class using the object of parent class as inheritance is not bidirectional
#a.bark()


# In[2]:


#2. Multilevel inheritance

class Animal:
    def speak(self):
        print("this is animal class and speak method")
class Dog(Animal):#inheritance of animal class in dog class
    def bark(self):
        print("this is dog class and bark method")
        
class DogChild(Dog): #inheritance of dog into dogchild class
    def eat(self):
        print("this is grand child class and eat method")

DG=DogChild()
#calling method of grandparent class using object of grandchild class
DG.speak()

#calling method of parent of DogChild i.e Dog
DG.bark()
DG.eat()

#instantiating Dog class
b=Dog()
b.speak()

#b.eat
A=animal()
A.speak()


# In[3]:


#3 .multiple inheritance

class calculation1:
    def sum(self,a,b):
        print("this is calculation1 class which is base1")
        return a+b

class claculation2:
    def multiple(self,a,b):
        print("this is calculation2 class which is base2")
        return a*b
    
#multiple inheritance
class Derived(calculation1,claculation2):
    def divide(self,a,b):
        print("this is derived class implementing multiple inheritance")
        return a/b
    
#instantiation
d=Derived()

print("calling method of base1 class:",d.sum(2,3))
print("calling method of base2 class:",d.multiple(2,3))
print("calling method division:",d.divide(2,3))

c=claculation2()
#c.sum(2,3)
c.multiple(2,3)


# In[4]:


#hierarchial
#hybrid

class Base:
    def pintme(self):
        print("base class")
        
class calculation1(Base):
    def sum(self,a,b):
        print("this is calculation1 class which is base1")
        return a+b

class calculation2:
    def multiple(self,a,b):
        print("this is calculation2 class which is base2")
        return a*b
    
#multiple inheritance
class Derived(calculation1,calculation2):
    def divide(self,a,b):
        print("this is derived class implementing multiple inheritance")
        return a/b
    
#instantiation
d=Derived()

print("calling method of base1 class:",d.sum(2,3))
print("calling method of base2 class:",d.multiple(2,3))
print("calling method division:",d.divide(2,3))

c=calculation2()
#c.sum(2,3)
c.multiple(2,3)

c.printme()


# In[5]:


#issubclassmethod

print(issubclass(Derived,calculation2))

print(issubclass(calculation2,Derived))

print(issubclass(Derived,calculation1))


# In[6]:


#isinstance method
print(isinstance(d,calculation1))


# In[7]:


#create a parent class
class Animal:
    def speak(self):
        print("this is animal class and speak method")
class Dog(Animal):#inheritance of animal class in dog class
    def bark(self):
        print("this is dog class and bark method")
        
#Instantiation of child class i.e. dog
d=Dog()

#access the datamember of parent class and self classs
d.speak()


# In[9]:


#method overriding with ___hierarchial____inheritance
class Bank: 
    def getoi(Self):
        return 8
class SBI(Bank):
    def getroi(self):
        return 10
class IDBI(Bank):
    def getroi(Self):
        return 7
    
    
b1=Bank()

b2=SBI()

b3=IDBI()


print("calling the method using b3 instance od IDBI:",b3.getroi())
print("calling the method using b2 instance od SBI:",b2.getroi())
print("calling the method using b1 instance od BANK:",b1.getroi())


# DATA ABSTRACTION

# In[12]:


class Employee:
    __count=0;
    c=4
    def __init__(self):
        Employee.__count=Employee.__count+1
    def display(self):
        print("the num of employee:",Employee.__count)
e=Employee()
e1=Employee()

#pint(e.__count)
print(e.c)
e.display()


# In[2]:


class Base:
    def __init__(self):
        
        self._a=2 # protected member (created using _)
        self.__b=9 # private member(created using __)
class Derived(Base):
    def __init(self):
        Base.__init__(self)
    def display(self):
        print("Hello")
        print("Try to call protected member of class base:", self._a)
        self._a=3
        print("we modified the protected member of base class:",self._a)
        #print("try to access private member",self.__b)    
        
        
        
        
obj1=Derived()
obj2=Base()

obj1.display()
#print("call using obj1:",obj1._a)
#print("call using obj2:",obj2._a)


# POLYMORPHISM

# In[19]:


def add(x,y,z=0):
    return x+y+z

print(add(2,3))
print(add(2,3,4))


# In[1]:


class India():
    def capital(self):
        print("newDelhi")
    def language(self):
        print("hindi")
    def type(self):
        print("developing")
class USA():
    def capital(self):
        print("Washington")
    def language(self):
        print("English")
    def type(self):
        print("developing")
        
obj1=India()
obj2=USA()
obj2.capital()

obj1.language()

for country in (obj1,obj2):
    country.capital()
    country.language()
    country.type()


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


def printme(str):
    "this is a doc string which is optional and wont get printes with output"
    print(str)
    return


# In[2]:


printme("hello,python")


# In[3]:


def changeme(mylist):
    mylist.append([1,2,3]);
    print("inside function defination",mylist)
    return


# In[4]:


mylist=[10,20,30]
changeme(mylist)
print("outside the function:",mylist)


# In[5]:


def changeme1(mylist):
    mylist.append([1,2,3]);
    print("inside function defination",mylist)
    return


# In[6]:


mylist=[10,20,30]
changeme1(mylist)
print("outside the function:",mylist)


# types of arguments in function

# In[7]:


#3. default argument

def info(name,age=34):
    print("name:",name)
    print("age:",age)
    return
info('Lucky')
info('aishu',19)


# In[11]:


#4 variable length argument

def printinfo(agr1, *tuple1):
    print(arg1)
    for x in tuple1:
        print(x)
    return

printinfo(10,20,30,40,50)


# In[12]:


#defining anonymous function

x=lambda a,b: a*b

#call and print anonymous function

print(x(5,6))


# In[14]:


#return statement
def sum(arg1,arg2):
    total=arg1+arg2
    print("inside function:",total)
    return total
    
#sum(10,20)
total=sum(10,20)
print("outside function",total)


# In[16]:


#scope of the variable

total=0 #global variable

def sum(arg1,arg2):
    total=arg1+arg2
    print("inside function:",total)
    return total
    
#sum(10,20)
sum(10,20)
print("outside function",total)


# Class and Object

# In[17]:


class Employee:
    'some docstring'
    id=10
    name='devansh'
    def display(self):
        print(self.id)
        print(self.name)
        
        


# In[19]:


#instantiation of class
emp=Employee()

#accessing the attribute of class
emp.display()


# In[21]:


#using the constructor

class car:
    def __init__(self,modelname,year):
        self.modelname=modelname
        self.year=year
    def display(self):
        print("the model name of car class is:",self.modelname)
        print("the year of car class is:",self.year)
        
c1=car("Toyota",2018)
c1.display()


# In[22]:


emp=Employee()


# In[23]:


del emp.id


# In[28]:


#non-parameterised constructor
class student:
    def __init__(self):
        print("this is non parameterised construcor")
    def showmethod(self,name):
        self.name=name
        print("print",self.name)
        
st1=student()


# In[30]:


st1.showmethod("diskha")


# BUILT IN FUNCTIONS IN OOPS

# In[34]:


class student:
    def __init__(self,name,id,age):
        self.name=name
        self.age=age
        self.id=id
s=student("AJ",1001,23)
#1. setattribute
print(getattr(s,'age'))

#2.has attribute
print(hasattr(s,'age'))

#3.delete attr
delattr(s,'age')

print(hasattr(s,'age'))

print(s.__doc__)
print(s.__module__)
print(s.__dict__)


# In[ ]:





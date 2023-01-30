#!/usr/bin/env python
# coding: utf-8

# In[1]:


##creation of list using string type
NewList=["apple","banana","cherry"]

print(type(NewList))
print(NewList)


# In[2]:


#access the element of list using index value
NewList[2]


# In[3]:


#create list with multiple type
List_with_different_type=["apple",2,True,"Tasty",2.6]
List_with_different_type
print(type(List_with_different_type))


# In[4]:


#create using list constructor list()

listconstruct=list(("a","b","c"))
print(listconstruct)

print(type(listconstruct))


# In[5]:


print(List_with_different_type[1:4:2])


# In[6]:


print(List_with_different_type[-4:-1])


# In[7]:


#some loop operation with list

print(List_with_different_type)
#1.for loop
for i in List_with_different_type:
    print(i)
#2. Range function
for i in range(len(List_with_different_type)):
    print("using range function:",List_with_different_type[i])


# METHODS IN LIST

# In[8]:


#1. Insert method

NewList=["apple","banana","cherry"]

NewList.insert(2,"Mango")

print(NewList)


# In[9]:


#2. append method

NewList.append("dragon")
print(NewList)


# In[10]:


#3. extend

#list1
print(NewList)
#list2
print(List_with_different_type)

#use concatination
#print("using concat:",NewList+List_with_different_type)

#use extend method
NewList.extend(List_with_different_type)
print(NewList)


# In[11]:


#create a tuple of string type
tuple_var=("car","bike")
#list of int type
list1=["1,2,3,4"]
#extend to add tuple into list
list1.extend(tuple_var)
print(list1)


# In[12]:


#4.Remove

list1.remove('car')
list1


# In[13]:


#5. pop
list1=[1,2,3,4]
list1.pop()


# In[14]:


#6. clear

list1.clear()
list1


# In[15]:


#7. copy

NewList=["apple","banana","cherry"]
list1=NewList.copy()

list1


# In[16]:


#8. count of occurence of any element in list

list1.count('mango')


# In[17]:


#9. index method

list1.index('cherry')


# In[18]:


#10. sort and reverse

list1.sort()
list1


# In[19]:


list1.reverse()
list1


# TUPLES

# In[20]:


#empty tuple

tup0=()
type(tup0)


# In[21]:


#tuple with one element

tuple1=(1,)
print(type(tuple1))


# In[22]:


#create a tuple with multiple elements

fruit=('apple','banana','cherry','kiwi','mango')
print(fruit)
print(type(fruit))


# In[23]:


#try to change the value of any tuple index

#to make any change you need to convert the tuple into list

list1=list(fruit)
print(list1)
list1[1]="beery"
print(list1)

#convet it back to tuple

fruit=tuple(list1)

print(fruit)


# In[24]:


#you can use tuple constructor to create any tuple

tuple2=tuple((1,2,3,4,5,6,7,6))
print(type(tuple2))


# In[25]:


tuple2[2:5]


# In[26]:


#iterate using loop

for x in tuple2:
    print(x)


# In[27]:


#membership

if 8 not in tuple2:
    print("yes 8 is not there:",tuple2)
else:
    print("no 8 is there",tuple2)


# In[28]:


#remove method: remove 4 from tuple2

tuple2=list(tuple2)
print(tuple2)
print(type(tuple2))
tuple2.remove(4)
print(tuple2)


# In[29]:


t1=(1,2,3,4,5,6)
print(type(t1))
t1=list(t1)
print(type(t1))
t1.remove(4)
print(t1)
t1=tuple(t1)
print(type(t1))


# In[30]:


print(tuple2.count(6))
print(tuple2.index(6))


# DICTIONARY

# In[31]:


newDict={
    "brand":"ford",
    "model":"mustag",
    "year":2009,
}
print(newDict)


# In[32]:


#find length if dictionary

len(newDict)


# In[33]:


#create dictionary with different ds

thisDic={
    "brand":"ford",
    "model":"mustag",
    "electric":False,
    "color":['red','blue','black']
}

print(thisDic)
print(type(thisDic))


# In[34]:


#try to access the element of dictionary
print(thisDic["color"])

#using get method
print("get method:",thisDic.get("color"))


# In[35]:


print("access the value from dictionary:",thisDic.values())
print("access the key from dictionary:",thisDic.keys())
print("access the items from dictionary:",thisDic.items())


# In[38]:


#nested dictionary

child1={
    "name":'Ram',
    "age":19
}
child2={
    "name":'Ramu',
    "age":21
}
child3={
    "name":'Rani',
    "age":28
}
child4={
    "name":'Raghu',
    "age":25
}
myfamily={
    "key1":child1,
    "key2":child2,
    "key3":child3,
    "key4":child4,
}

print("nested dictionary:",myfamily)


# In[39]:


#copy method
x=myfamily.copy()
x


# In[43]:


#frromkeys method

#create a set

set1={'suresh','mahesh','ramya'}
print(set1)

key='sales'

#create a dictinary using the from key method

thisdic=dict.fromkeys(set1,key)

thisDic


# SETS

# In[1]:


#create a set

fruit={"apple","banana","cherry"}
print(fruit)
print(type(fruit))


# In[3]:


#create using set cluster

thisset=set(("abc",123,True,4.0,"male"))
print(thisset)
print(type(thisset))


# In[4]:


#access the elements

for x in thisset:
    print(x)


# In[5]:


print('abc' in thisset)


# In[7]:


#add method to add element
#fruit={"apple,"banana","cherry"}
fruit.add("orange")
print(fruit)


# In[8]:


#add two set using the update method
newset={'pineapple','mango'}
fruit.update(newset)

print(fruit)

#check if we can add any list to our set
list1=['kiwi','melon']
fruit.update(list1)

print(fruit)


# In[9]:


#remove method

fruit.remove('orange')
print(fruit)


# In[10]:


#discard method:if we give the element which is not there 
#in the list it doenot generates any error

fruit.discard('orange')
print(fruit)


# In[ ]:


#clear()
#del


# In[11]:


x={"apple","banana","cherry"}
y={"google","microsoft","apple"}
z=x.difference(y)
print("value of x",x)
print("value of y",y)
print("value of z",z)


# In[12]:


x={"apple","banana","cherry"}
y={"google","microsoft","apple"}
z=x.difference_update(y)
print("value of x",x)
print("value of y",y)
print("value of z",z)


# In[14]:


x={"apple","banana","cherry"}
y={"google","microsoft","apple"}
z=x.intersection(y)
print("value of x",x)
print("value of y",y)
print("value of z",z)


# In[15]:


x={"apple","banana","cherry"}
y={"google","microsoft","apple"}
z=x.intersection_update(y)
print("value of x",x)
print("value of y",y)
print("value of z",z)


# In[16]:


x={"apple","banana","cherry"}
y={"google","microsoft","apple"}
z=x.union(y)
print("value of x",x)
print("value of y",y)
print("value of z",z)


# In[17]:


x={"apple","banana","cherry"}
y={"google","microsoft","apple"}
z=x.symmetric_difference(y)
print("value of x",x)
print("value of y",y)
print("value of z",z)


# In[18]:


x={"apple","banana","cherry"}
y={"google","microsoft","apple"}
z=x.symmetric_difference_update(y)
print("value of x",x)
print("value of y",y)
print("value of z",z)


# In[19]:


x={"apple","banana","cherry"}
y={"google","microsoft","apple"}
z=x.isdisjoint(y)
print("value of x",x)
print("value of y",y)
print("value of z",z)


# In[20]:


x={"apple","banana","cherry"}
y={"google","microsoft","apple"}
z=x.issubset(y)
print("value of x",x)
print("value of y",y)
print("value of z",z)


# In[22]:


x={"apple","banana","cherry"}
y={"google","microsoft","apple"}
z=x.issuperset(y)
print("value of x",x)
print("value of y",y)
print("value of z",z)


# In[ ]:





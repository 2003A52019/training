#!/usr/bin/env python
# coding: utf-8

# In[1]:


try:
    x=int(input("enter your input"))
except ValueError:
    print("you enter a string, try giving integer as input")


# In[2]:


try:
    print(x1)
except:
    print("your exception has been handled by except block")
finally:
    print("finally")


# In[5]:


try:
    x1="Lucky"
    print(x1)
    f=open("demo.txt",r)
except NameError:
    print("your exception has been handled by except block")
except FileNotFound:
    print("your FileNotFound exception has been handled by except block")
except ValueError:
    print("your ValueError exception has been handled by except block")
else:
    print("no exception is there")
    
finally:
    print("finally")


# In[ ]:





#!/usr/bin/env python
# coding: utf-8
v=int(input())
w=int(input())
if w&1 == 1 or w<2 or w<=v:
    print("invalid input")
else:
    x= ((4*v)-w)//2
print(" tw ",x)
print("fw",v-x)
# In[9]:


#inorder
class bt:
    def __init__(self,data):
        self.data=data
        self.lc=None
        self.rc=None
def insert(root,newvalue):
    if root is None:
        root=bt(newvalue)
        return root
    if newvalue<root.data:
        root.lc=insert(root.lc,newvalue)
    else:
        root.rc=insert(root.rc,newvalue)
    return root
def inorder(root):
    if root==None:
        return
    inorder(root.lc)
    print(root.data)
    inorder(root.rc)             
root = insert(None, 15)
insert(root, 10)
insert(root, 24)
insert(root, 5)
insert(root, 14)
insert(root, 22)
insert(root, 55)
print("inorder traversal")
inorder(root)


# In[4]:


#pre-order
class bt:
    def __init__(self,data):
        self.data=data
        self.lc=None
        self.rc=None
def insert(root,newvalue):
    if root is None:
        root=bt(newvalue)
        return root
    if newvalue<root.data:
        root.lc=insert(root.lc,newvalue)
    else:
        root.rc=insert(root.rc,newvalue)
    return root
def preorder(root):
    if root==None:
        return
    preorder(root.lc)
    preorder(root.rc)  
    print(root.data)
root = insert(None, 15)
insert(root, 10)
insert(root, 24)
insert(root, 5)
insert(root, 14)
insert(root, 22)
insert(root, 55)
print("preorder traversal")
preorder(root)


# In[6]:


#post-order
class bt:
    def __init__(self,data):
        self.data=data
        self.lc=None
        self.rc=None
def insert(root,newvalue):
    if root is None:
        root=bt(newvalue)
        return root
    if newvalue<root.data:
        root.lc=insert(root.lc,newvalue)
    else:
        root.rc=insert(root.rc,newvalue)
    return root
def postorder(root):
    if root==None:
        return
    print(root.data)
    postorder(root.lc)
    postorder(root.rc)  
root = insert(None, 15)
insert(root, 10)
insert(root, 24)
insert(root, 5)
insert(root, 14)
insert(root, 22)
insert(root, 55)
print("postorder traversal")
postorder(root)


# In[19]:


class Node:
    def __init__(self,key,l=None,r=None):
        self.key=key
        self.l=l
        self.r=r
def vot(node,dist, d):
    if node is None:
        return
    d.setdefault(dist, []).append(node.key)
    vot(node.l, dist+1 ,d)
    vot(node.r, dist-1 ,d)
def pvot(root):
    d={}
    vot(root,0,d)
    for value in d.values():
        print(value)
if __name__=='__main__':
    root=Node(1)
    root.l=Node(2)
    root.r=Node(3)
    root.r.l=Node(4)
    root.r.r=Node(5)
    root.r.l.l=Node(6)
    root.r.l.r=Node(7)
    root.r.l.r.l=Node(8)
    root.r.l.r.r=Node(9)
    pvot(root)


# In[1]:


n=int(input())
for i in range(0,n):
    p1=0,p2=n-1
while(p1<p2):
    while(n%2==0 && p1<p2)
        p1++
    while(n%2!==0 && p1<p2)
        p2--
    if(p1<p2):
        temp=p1
        p1=p2
        p1++
        p2++
        



# In[7]:


n=int(input())
a=list(map(int,input().strip().split(" ")))[:n]
e=[]
o=[]
for i in a:
    if(i%2==0):
        e.append(i)
    else:
        o.append(i)
e.sort()
o.sort()
a=e+o
for i in a:
    print(i,end=" ")


# In[7]:


//Dict to Hash table
keys=['NAME','AGE','BRANCH']
values=["ABC",'100',"AERONAUTICAL"]
outsource=zip(keys,values)
DICT=dict(outsource)
print(DICT)


# In[16]:


matrix=[[0,0,0,1,0],
        [2,0,0,0,3],
        [0,0,0,4,0]]
dict={}
print("sparse matrix")
for i in range(len(matrix)):
    print("\n")
    for j in range(len(matrix[i])):
        print(matrix[i][j],end='')
        if(matrix[i][j]!=0):
            dict[(i,j)]=matrix[i][j]
print(dict)


# In[ ]:


string="LEVEL"
index=-1
fs=""
for i in string:
    if string.count[i]==1:
        fs+=1
        break
    else:
        index+=1
if index==1:
    print("all characters")
else
    print("repeated characters",fs)
        


# In[2]:


#non repeated character in string
string="LEVEL"
for i in string:
    count=0
    for j in string:
      if i==j:
        count+=1
      if count>1:
        break
    if count==1:
      print("non repeated character",i)


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# # List Sorting

# In[8]:


lis=[0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]
lis.sort()
print(lis)
print("\n")
lis1=lis[0:5]
del lis[0:5]
lis=lis+lis1
print("\n")
print(lis)


# In[ ]:





# # Merging Of Lists

# In[1]:


a=[10,20,40,60,70,80]
b=[5,15,25,35,45,60]
for i in b:
    a.append(i)
print(a)


#!/usr/bin/env python
# coding: utf-8

# # Substring in a Given String

# In[1]:


import re
a=input("Enter a String: \n")
b=input("Enter the substring: \n")
c= re.finditer(b, a)
d= [i.start() for i in c]
print(d)


# In[ ]:





# In[ ]:





# # islower() & isupper()

# In[ ]:





# In[2]:


a=input("Enter a String: \n")
print(a.islower())


# In[3]:


a=input("Enter a String: \n")
print(a.islower())


# In[ ]:





# In[4]:


a=input("Enter a String: \n")
print(a.isupper())


# In[5]:


a=input("Enter a String: \n")
print(a.isupper())


# In[ ]:





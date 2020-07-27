#!/usr/bin/env python
# coding: utf-8

# # List To Dictionary Using List Comprehension

# In[1]:


l=[1,2,3,4,5,7,8]
l1=["a","b","c","d","e"]
{str(i):l[(l.index(l1.index(i)+1))] for i in l1}


# In[ ]:





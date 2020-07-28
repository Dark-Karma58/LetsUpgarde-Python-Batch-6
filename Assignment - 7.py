#!/usr/bin/env python
# coding: utf-8

# # Dictionary to New Dictionary

# In[1]:


port1={21:"FTP",22:"SSH",23:"telnet",80:"http"}
print({str(port1[i]):str(i) for i in port1})


# In[ ]:





# # List to New List

# In[2]:


LT=[(1,2),(3,4),(5,6),(4,5)]
c=[]
for i in LT:
	for j in i:
		a=0
	b=i[a]+i[a+1]
	a+=2
	c.append(b)
print(c)


# In[ ]:





# # Inner List to Outer List

# In[4]:


List1=[(1,2,3),[1,2],['a','hit','less']]
c=[]
for i in List1:
	for j in i:
		c.append(j)
print(c)


# In[ ]:





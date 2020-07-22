#!/usr/bin/env python
# coding: utf-8

# # Sum of N natural numbers

# In[6]:


a=input("Enter the Range ending :\n")
b=int(a)
c=0
while b>=0:
	c+=b
	b-=1
print("\nThe sum of %d numbers is %d" %(int(a),c))


# In[7]:


a=input("Enter the Range ending :\n")
b=int(a)
c=0
while b>=0:
	c+=b
	b-=1
print("\nThe sum of %d numbers is %d" %(int(a),c))


# In[ ]:





# # Prime number or not

# In[14]:


a=int(input("Enter the Number :\n"))
if (a>1):
    for i in range(2,a):
        if (a%i)==0:
            print("%d is not a prime number" %(a))
            break
    else :
            print("%d is a prime number" %(a))
else :
    print("%d is a prime number" %(a))


# In[15]:


a=int(input("Enter the Number :\n"))
if (a>1):
    for i in range(2,a):
        if (a%i)==0:
            print("%d is not a prime number" %(a))
            break
    else :
            print("%d is a prime number" %(a))
else :
    print("%d is a prime number" %(a))


# In[ ]:





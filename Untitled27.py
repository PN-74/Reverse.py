#!/usr/bin/env python
# coding: utf-8

# In[2]:


fibonacciList = [0, 1]
# finding 10 terms of the series starting from 3rd term
N = 10
for term in range(3, N + 1):
    value = fibonacciList[term - 2] + fibonacciList[term - 3]
    fibonacciList.append(value)
print("10 terms of the fibonacci series are:")
print(fibonacciList)


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from sklearn.preprocessing import OneHotEncoder
encoder=OneHotEncoder(handle_unknown='ignore')
encoder_temp=OneHotEncoder(handle_unknown='ignore')
X = np.array([[0,1,6,2], [1,5,3,5], [2,4,2,7], [1,0,4,2]])
X_temp = np.array([[0,1,6,2], [1,5,3,5], [2,4,2,7]])
print(X)
print(" ")
print(X_temp)
encoder.fit(X)
encoder_temp.fit(X_temp)


# In[ ]:


x = encoder.transform([[2,1,2,1]]).toarray()


# In[ ]:


x.shape


# In[ ]:


for t in encoder.get_feature_names():
    print(t)


# In[ ]:


for t in encoder_temp.get_feature_names():
    print(t)


# In[ ]:


for i in encoder.transform([[2,4,3,4]]).toarray()[0]:
    print(int(i))


# In[ ]:


enc = OneHotEncoder(handle_unknown='ignore')
MF = [['Male', 1], ['Female', 3], ['Female', 2]]
enc.fit(MF)


# In[ ]:


for i in enc.categories_:
    print(i)


# In[ ]:


for i in enc.get_feature_names():
    print(i)


# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 13:36:48 2019

@author: AL-ZAMEL
"""

import pandas as pd
import numpy as np
arr=np.random.rand(25)
print arr
print "*******************************"
df=pd.DataFrame((arr).reshape(5,5),index=['a1','a2','a3','a4','a5'],columns=['b1','b2','b3','b4','b5'])
print df
print "*******************************"
print df.drop('b1',axis=1)
print df
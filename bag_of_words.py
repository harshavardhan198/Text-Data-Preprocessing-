# -*- coding: utf-8 -*-
"""Untitled28.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14_Qev21BpQqRGW68-Q8dTlGb0LADGLrD
"""

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

text_data = np.array(['I love Europe!',
                      'Rita is the  best',
                      'Good read beats both'])

count = CountVectorizer()
bag_of_words = count.fit_transform(text_data)

bag_of_words.toarray()

feature_names = count.get_feature_names()

feature_names

df1 = pd.DataFrame(bag_of_words.toarray(), columns = feature_names)
display(df1)


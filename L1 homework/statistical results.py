import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# pandas
data = {'语文': [68, 95, 98, 90, 80], '数学': [65, 76, 86, 88, 90], '英语': [30, 98, 88, 77, 90]}
df1 = DataFrame(data, index=['张飞', '关羽', '刘备', '典韦', '许褚'], columns=['数学', '英语', '语文'])

# print(df1)

'''
print('学科最低分数为:\n', df1.min())
print('学科最高分数为:\n', df1.max())
print('学科平均分数为:\n', df1.mean())
print('学科方差为:\n', df1.var())
print('学科标准差为:\n', df1.std())
'''
# 具体行的最大值
# print(df1.loc['张飞'].max())

# 所有行的最大值
# print(df1.max(axis=1))  # axis=1表示按行，axis=0表示按列

# 添加列
df1['总成绩'] = df1.apply(lambda x: x.sum(),axis=1)
df1['成绩排名'] = df1['总成绩'].rank()  #有问题
# print(df1)

# 排序
print(df1.sort_values(by='总成绩', ascending=False))



from pandas import Series
import numpy as np

# 一维的数据结构，类似array
s = Series(data=[1, 2, 3, "four"])
print(s)

# 显式索引
s2 = Series(data=[1, 2, 3, "four"], index=["a", "b", "c", "d"])
print(s2)

# 使用numpy作为数据源
s3 = Series(data=np.random.randint(0, 50, size=(4,)))
print(s3)

# 字典
dict = {
    "语文": 100,
    "数学": 98,
    "英语": 110,
    "理综": 280
}

# 字典作为数据
s4 = Series(data=dict)
print(s4)


s5 = Series(data=[1, 2, 3], index=['a', 'c', 'b'])

s6 = Series(data=[1, 2, 3], index=['a', 'd', 'c'])

s7 = s5 + s6

# 切片
print(s7.values[0:2])



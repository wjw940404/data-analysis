from pandas import DataFrame
import numpy as np

# 隐式索引
df1 = DataFrame(data=[[1, 2, 3], [4, 5, 6]])
print(df1)

# 字典创建
dic = {
    "语文": [150, 0],
    "数学": [150, 0],
    "英语": [150, 0]
}
# 显式 行索引（列索引为字典的key）
df2 = DataFrame(data=dic, index=["张三", "李四"])
print(df2)

# 用numpy创建，赋行索引和列索引
df3 = DataFrame(data=np.random.randint(0, 100, size=(6, 4)), index=["赵一", "吴二", "张三", "李四", "王五", "钱六"], columns=["语文", "数学", "英语", "物理"])
print(df3)

# 索引
# df[col]: 取列
# df.loc[row]: 显式索引取行；df.iloc[row]: 隐式索引取行；df.loc[row, col]: 取行、列
# df[[col1, col2]] 取多列， df.loc[[row1, row2], [col1, col2]] 取多行多列

# 取列
print("------取单列------")
print(df3["数学"])

print("------取多列------")
print(df3[["语文", "数学"]])

# 取行
# iloc - 隐式索引； loc - 显式索引
print("------取行------")
print("------iloc------")
print(df3.iloc[1])
print("------loc------")
print(df3.loc[["张三", "李四"]])

# 取多个元素
print("------取多个元素------")
print(df3.loc[["吴二", "王五"], ["语文", "英语"]])

# 切片
# 直接切，切行
print(df3[0:2])

# 需要用iloc 隐式索引 df.iloc[startRow:endRow:step, startCol:endCol:step] 切片
print("------切前两列------")
print(df3.iloc[:, 0:2])





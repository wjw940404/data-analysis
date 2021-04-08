import numpy as np
import matplotlib.pyplot as plt

arr_1 = np.array([[1, 2], [3, 4]])
arr_2 = np.array([[3, 7], [5, 8]])
print(np.dot(arr_1, arr_2))

# 读取图片
arr_img = plt.imread("./../resources/1.jpg")
# 展示图片
plt.imshow(arr_img)

# 创建一个3*4的二维数组，里面值都是1
arr_3 = np.ones(shape=(4, 4))
print(arr_3)

# 创建一个单位矩阵
arr_eye = np.eye(4)
print(arr_eye)

print(arr_3 + arr_eye)

print(np.linspace(0, 100, num=20))

print(np.arange(10, 50, step=2))

arr_random1 = np.random.randint(0, 100, size=(3, 4))
print(arr_random1)

print("-------------------------")
# for循环
for i in arr_random1:
    for j in i:
        print(j)

print("-------------------------")

arr_random2 = np.random.randint(0, 100, size=(4, 3))
print(arr_random2)

print(np.dot(arr_random1, arr_random2))

arr_4 = np.random.randint(0, 100, size=(10,))
# 方差
print(np.var(arr_4))
# 标准差
print(np.std(arr_4))
# 平均值
print(np.mean(arr_4))




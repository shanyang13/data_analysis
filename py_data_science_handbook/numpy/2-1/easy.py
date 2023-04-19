import numpy as np

print(np.__version__)

L = list(range(10))
print("L:\n", L)

print("type(L[0]):\n", type(L[0]))

L2 = [str(c) for c in L]
print("L2:\n", L2)

print("type(L2[0]):\n", type(L2[0]))

a = np.array([1, 4, 2, 5, 3])
print("a:\n", a)

b = np.array([3.14, 4, 2, 3])  # numpy要求数组必须同一类型，，否则向上转换（如果可行）
print("b:\n", b)

c = np.array([1, 2, 3, 4], dtype='float32')
print("c:\n", c)

d = np.array([range(i, i + 3) for i in [2, 4, 6]])  # numpy数组可以被指定为多维的
print("d:\n", d)

e = np.zeros(10, dtype=int)  # 长度为10的全零数组
print("e:\n", e)

f = np.ones((3, 5), dtype=float)  # 创建3*5浮点数数组，数组的值全是1
print("f:\n", f)

g = np.full((3, 5), 3.14)  # 创建一个3*5的浮点数数组，数组的值都是3.14
print("g:\n", g)

h = np.arange(0, 20, 2)  # 从0到20，步长是2的线性序列
print("h:\n", h)

i = np.linspace(0, 1, 5)  # 创建一个5个元素的数组，5个数均匀的分配到0～1，不指定数量默认生成50个
print("i:\n", i)

j = np.random.random((3, 3))  # 创建一个3*3的在0到1均匀分布的随机数组成的数组
print("j:\n", j)

k = np.random.randint(0, 10, (3, 3))  # 创建一个3*3,0到10区间（左闭右开）的随机整型数组
k2 = np.random.randint(5, size=(3, 3))  # 创建一个3*3,0到5区间（左闭右开）的随机整型数组
print("h:\n", k)
print("h2:\n", k2)

l = np.eye(3)  # 创建一个3*3的单位矩阵
print("l:\n", l)

m = np.empty(3)  # 创建一个由3个整型数组成的未初始化的数组，数组的值是内存空间中的任意值
m2 = np.empty((2, 3))
print("m:\n", m)
print("m2:\n", m2)

import numpy as np

a = np.array([[3, 5, 2, 4],
              [7, 6, 8, 8],
              [1, 6, 7, 7]])

print("a[1, 1]:\n", a[1, 1])

a[1, 1] = 20
print("a:\n", a)

a[1, 1] = 3.14  # numpy的数组类型是固定的，默认会保持整型，且不会做出任何提示
print("a:\n", a)

b = np.arange(0, 10)
print("b:\n", b)

print("b[::2]:\n", b[::2])
print("b[::-2]:\n", b[::-2])
print("b[5::2]:\n", b[5::2])
print("b[5::-2]:\n", b[5::-2])

print("a[:2, :3]:\n", a[:2, :3])
print("a[::-1, ::-1]:\n", a[::-1, ::-1])

print("a[:, 0]:\n", a[:, 0])  # 只取第一列
print("a[0, :]:\n", a[0, :])  # 只取第一行
print("a[0:\n", a[0])  # 省略写法

c = np.array([[3, 5, 2, 4],
              [7, 6, 8, 8],
              [1, 6, 7, 7]])
print("c:\n", c)
c2 = c[:2, :2]
print("c2:\n", c2)
c2[0, 0] = 99  # 改变子数组，原始数组也会被修改
print("c2:\n", c2)
print("c:\n", c)

d = np.array([[3, 5, 2, 4],
              [7, 6, 8, 8],
              [1, 6, 7, 7]])
print("d:\n", d)
d2 = d[:2, :2].copy()
print("d2:\n", d2)
d2[0, 0] = 99  # 修改拷贝后的子数组不会改变原始数组
print("d2:\n", d2)
print("d:\n", d)

e = np.arange(1, 10)
print("e:\n", e)

f = np.arange(1, 10).reshape((3, 3))  # 将1到9放到3*3的矩阵中
print("f:\n", f)

g = np.array([1, 2, 3])
g2 = g.reshape((1, 3))  # 将一维数组转变为二位的行
g3 = g.reshape((3, 1))  # 将一维数组转变为二位的列
print("g2:\n", g2)
print("g3:\n", g3)

#  数组的拼接
h = np.array([1, 2, 3])
h2 = np.array([3, 2, 1])
h3 = np.concatenate([h, h2])  # 横向拼接
print("h3:\n", h3)
h4 = np.array([99, 99, 99])
h5 = np.concatenate([h, h2, h4])  # 多条横向拼接
print("h5:\n", h5)
h6 = np.array([[1, 2, 3],
               [4, 5, 6]])
h7 = np.concatenate([h6, h6], axis=1)  # 二维拼接，axis可填1或0，表示拼接的轴
print("h7:\n", h7)
h8 = np.vstack([h, h6])  # 垂直拼接
print("h8:\n", h8)
h9 = np.hstack([h, h2])  # 水平拼接
print("h9:\n", h9)

#  数组的分裂
i = np.array([1, 2, 3, 99, 99, 3, 2, 1])
i, i2, i3 = np.split(i, [3, 5])   # 3，5为数组的分裂点
print("i, i2, i3:\n", i, i2, i3)

g = np.arange(16).reshape((4, 4))
g2, g3 = np.vsplit(g, [2])    # 横向分裂
print("g:\n", g)
print("g2:\n", g2)
print("g3:\n", g3)

g4, g5 = np.hsplit(g, [2])    # 纵向分裂
print("g:\n", g)
print("g4:\n", g4)
print("g5:\n", g5)
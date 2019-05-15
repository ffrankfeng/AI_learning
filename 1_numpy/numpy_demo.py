import numpy

numbers = numpy.array([1,2,3,4])
print(numbers)
print(numbers.dtype)

numbers = numpy.array([1,2,3,'4'])
print(numbers)
print(numbers.dtype)

# 文件读取
person = numpy.genfromtxt("../resources/person.txt",delimiter=",",dtype=str,skip_header=1);
print(person)
#取出第1行低3列数据
print(person[1,3])

# 数据切片
vector = numpy.array([5,10,15,20])
print(vector[0:3])#取出下标0-3

matrix = numpy.array([[5,10,15],
                      [20,25,30],
                      [35,40,45]])
print(matrix[:,1])#取出第1列
print(matrix[1,:])#取出第1行
print(matrix[:,0:2])#取出第0，1列

vector = numpy.array([5,10,15,20])
print(vector == 10)#判断每个元素是否==10
print(matrix == 10)
equal_to_ten = (vector == 10)
print(vector[equal_to_ten])#bool类型的值做索引

print((vector == 5) & (vector == 10))
print((vector == 5) | (vector == 10))

#值类型转换
vector = numpy.array(["1","2","3"])
print(vector.dtype)
print(vector)
vector = vector.astype(float)
print(vector.dtype)
print(vector)

#值操作
matrix = numpy.array([[5,10,15],
                      [20,25,30],
                      [35,40,45]])
print(matrix.min())
print(matrix.sum(axis=1))#按行求和
print(matrix.sum(axis=0))#按列求和

print(numpy.arange(15))#[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]
print(numpy.arange(15).reshape(3,5))#reshape成3*5的矩阵

#3*5的0矩阵
matrix = numpy.zeros((3,5))
print(matrix)

matrix = numpy.ones((3,5),dtype=numpy.int)
print(matrix)

#10-30内，数据间隔为5
numbers = numpy.arange(10,30,5)
print(numbers)

# matrix = numpy.random((2,3))
# print(matrix)

from numpy import pi
#从0-2pi平均取100个值
array = numpy.linspace(0,2*pi,100)
print(array)

# 数值运算
a = numpy.array([20,30,40,50])
b = numpy.array(4)
print(a)
print(b)
c= a - b
print(c)
c = c -1
print(c)
b = b ** 2
print(b)
print(a<35)

#矩阵乘法
A = numpy.array([[1,1],[0,1]])
B = numpy.array([[1,2],[3,4]])
print(A*B)#对应位置相乘
print(A.dot(B))#矩阵相乘
print(numpy.dot(A,B))

#矩阵维度变换
a = numpy.floor(10*numpy.random.random((3,4)))
print(a)
print(a.ravel())
a.shape = (6,2)#reshape矩阵维度
print(a)
print(a.T)#矩阵转置

a = numpy.array([[1,2],[3,4]])
b = numpy.array([[5,6],[7,8]])
c= numpy.vstack((a,b))#矩阵拼接
print(c)
c= numpy.hstack((a,b))#矩阵拼接
print(c)
print(numpy.hsplit(c,2))
print(numpy.hsplit(c,(2,3)))

#矩阵复制
#1、引用复制,a,c指向同一内存
a= numpy.arange(12)
b = a
b.shape = 3,4
print(a.shape)
print(id(a) == id(b))
#2、浅拷贝,a,c指向不同内存，但共用同一个值
c = a.view()
print(c is a)
c.shape =2,6
print(a.shape) #a != c
c[0,0] =12345
print(a) #a的值改变
#3、复制，a,c指向不同内存，不共用同一个值
c = a.copy()
print(c is a)
c[0,0] =11111
print(a) #a的值不变

data = numpy.sin(numpy.arange(20)).reshape(5,4)
#求每列最大值的索引
ind = data.argmax(axis = 0)
print(ind)
data_max =data[ind,range(data.shape[1])]
print(data_max)

a = numpy.arange(0,40 ,10)
print(a)
#矩阵扩展：行变成原来的3倍，列变成2倍
b = numpy.tile(a,(2,3))
print(b)

a = numpy.array([[4,3,5],[1,2,1]])
a.sort(axis=1)#按行排序
print(a)
print(numpy.argsort(a))#按行从小到大的索引
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

matrix = numpy.random((2,3))
print(matrix)
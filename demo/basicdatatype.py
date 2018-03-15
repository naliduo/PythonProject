# region 数字 
# Number数据类型用于存储数值，不允许改变，也就意味着改变Number数据类型的值，将重新分配内存空间
# Python 支持四种不同的数值类型：整型(Int),长整型(long integers无限大小的整数，整数最后是一个大写或小写的L),浮点型(floating point real values),复数(complex numbers)
# Python math 模块提供了许多对浮点数的数学运算函数。
var1 = 1
var2 = 10
print ("var1:",var1,"var2:",var2)
del var1
print ("删除var1对象引用")
print ("var1:",var1,"var2:",var2)
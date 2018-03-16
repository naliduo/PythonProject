# region 数字
# Number数据类型用于存储数值，不允许改变，也就意味着改变Number数据类型的值，将重新分配内存空间
# Python 支持四种不同的数值类型：整型(Int),长整型(long integers无限大小的整数，整数最后是一个大写或小写的L),浮点型(floating point real values),复数(complex numbers)
# Python math 模块提供了许多对浮点数的数学运算函数。
var1 = 1
var2 = 10
print("var1:", var1, "var2:", var2)
# del var1
# print ("删除var1对象引用")
# print ("var1:",var1,"var2:",var2)
# endregion

# region 字符串
# 1.
varstr1 = 'Hello World!'
varstr2 = 'Python Runoob'
print('varstr1[0]:', varstr1[0])
print('varstr2[2:5]:', varstr2[2:5])
print('varstr2[:5]:', varstr2[:5])
print('varstr2[2:]:', varstr2[2:])

# 2.字符串格式化
print('My name is %s and I am %d years old' % ('Zara', 21))

# 3.字符串内建函数 format示例，基本语法是通过{}和:来代替以前的%
str = '{} {}'.format('hello','world') # 不设置指定位置，按默认顺序
print (str)

str1 = '{1} {0} {1}'.format('hello','world')# 设置指定位置，可以不按顺序
print (str1)

str2 = '网站名:{name},url:{url}'.format(name = '百度',url = 'www.baidu.com')
print (str2)

site = {'name':'教程','url':'www.runoob.com'}
print ('网站名:{name},url:{url}'.format(**site)) # 通过字典设置参数 **必须要有

my_list = ['教程列表','www.runoob.com']
my_list1 = ['百度','www.baidu.com']
print ('网站名1:{0[0]},url1:{0[1]};网站名2:{1[0]},url2:{1[1]}'.format(my_list,my_list1)) # 通过列表索引设置参数

# endregion

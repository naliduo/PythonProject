# 序列都可以进行的操作包括索引，切片，加，乘，检查成员
# Python常用的序列包括：列表(list),元组(tuple)
# 列表(list)初始化
list1 = ['physics', 'chemistry', 1873, 2000]  # 列表的数据项不需要具有相同的类型
print(list1)

# 更新列表
list2 = []
list2.append(123)
list2.append(456)
list2.append('anaconda')
list2.append('photo')
print(list2)

# 删除列表元素
list2.remove(123)
print(list2)

del list2[0]
print(list2)

# 脚本操作符
# 列表对 + 和 * 的操作符与字符串相似。+ 号用于组合列表，* 号用于重复列表。
list3 = [1, 2, 3]
list4 = [6, 5, 4]

list3[0] = 10
print(list3[-2])
print(len(list3))
print(list3+list4)
print(list4*4)
print(3 in list3)
for x in list4:
    print(x)

# 函数 	列表元素个数len(list),返回列表元素最大值max(list),返回列表元素最小值min(list),将元组转换为列表list(seq)
import operator
print(operator.lt(list3, list4))

# 方法
# 在列表末尾添加新的对象list.append(obj),统计某个元素在列表中出现的次数list.count(obj),在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）list.extend(seq),
# 从列表中找出某个值第一个匹配项的索引位置list.index(obj),将对象插入列表list.insert(index, obj),移除列表中的一个元素（默认最后一个元素），并且返回该元素的值list.pop(obj=list[-1]),
# 移除列表中某个值的第一个匹配项list.remove(obj),反向列表中元素list.reverse(),对原列表进行排序list.sort([func])


# 元组(Tuple),Python的元组和列表类似，不同之处在于元组的元素不能修改。元组使用小括号，列表使用大括号
# 元组初始化
tup1 = ('physics', 'chemistry', 1234, 4356)
tup2 = 'a', 'b', 'c', 12345
print(tup1)
print(tup2)

# 元组中只包含一个元素时，需要在元素后面添加逗号
tup3 = (50)
tup4 = (50,)
print(tup3)
print(tup4)

# 修改元组
# 元组中的元素值是不允许修改的，但是我们可以对元组进行连接组合，eg：
tup5 = (12, 24.56)
tup6 = ('abc', 'tuple')
tup7 = tup5+tup6
print(tup7)

# 删除元组
# 元组中的元素值不允许删除，但我们可以使用del删除整个元组，eg:
tup8 = ('photo',1234)
del tup8

# 内置函数
# 计算元组元素个数len(tuple),返回元组中元素最大值max(tuple),返回元组中元素最小值min(tuple),将列表转换为元组tuple(seq)
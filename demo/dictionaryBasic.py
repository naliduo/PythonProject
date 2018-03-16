# 字典是可变容器，且可存储任意类型对象
# 键必须是唯一的，但值不必是唯一的。值可以取任意的数据类型，但是键必须是不可变的如：字符串，数字或元组
# 初始化
dict1 = {'abc': 1234, 234: 789}

print(dict1['abc'])
print(dict1[234])

# 修改字典
# 向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对如下实例:
dict2 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'} 
dict2['Age'] = 8 # update existing entry
dict2['School'] = "DPS School" # Add new entry 
print ("dict2['Age']: ", dict2['Age'])
print ("dict2['School']: ", dict2['School'])

# 删除字典元素
dict3 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'} 
del dict3['Name'] # 删除键是'Name'的条目
dict3.clear()     # 清空词典所有条目
del dict3         # 删除词典

# 字典键特性
# 不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
# 条件语句
flag = False
name = 'luren'
if name == 'python':
    flag = True
    print('welcome boss')
elif name == 'conda':
    flag = False
    print('welcome')
else:
    print(name)

# 循环语句
# region while
numbers = [12, 23, 34, 45, 56, 67]
even = []
odd = []
while(len(numbers) > 0):
    num = numbers.pop()  # pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
    if(num % 2 == 0):
        even.append(num)
    else:
        odd.append(num)
print("偶数：", even)
print("奇数：", odd)
# endregion

# region for
for nm in 'Python':
    print ('当前字母：',nm)

fruits = ['banana','apple','mango']
for fruit in fruits:
    print('当前水果：',fruit) 
# endregion 
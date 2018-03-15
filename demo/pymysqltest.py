import pymysql

#创建链接
conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='123456',db='pythondb',charset='utf8')
#创建游标
cursor = conn.cursor()

#执行SQL，并返回受影响的行数
row = cursor.execute('SELECT * FROM student')
print ("行数：",row)
#执行SQL，并返回第一行数据
cursor.execute('SELECT * FROM student')
oneline = cursor.fetchone()

#执行SQL，并返回前三行数据
cursor.execute('SELECT * FROM student')
manyline = cursor.fetchmany(3)

#执行SQL，并返回所有数据
cursor.execute('SELECT * FROM student')
allline = cursor.fetchall()

#提交，否则无法保存新建或者修改的数据
conn.commit()

cursor.close()

conn.close()

for mline in manyline:
    print(mline)

for aline in allline:
    print(aline)
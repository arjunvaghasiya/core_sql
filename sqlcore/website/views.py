
from cgitb import text
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey,create_engine
from sqlalchemy.sql.expression import update,delete
db = create_engine('postgresql://postgres:abc123@localhost/myflaskproject')

meta = MetaData()

student = Table(
    "student",
    meta,
    Column("id",Integer,primary_key = True),
    Column("name",String(50)),
)

likes = Table(	
    "likes",
    meta,
    Column("id",Integer),
    Column("fruits",String(50)),
)

# meta.create_all(db)
conn = db.connect()

# ins = student.insert()
# ins = student.insert().values(name = "chotu")
# result = conn.execute(ins)

# ins2 = likes.insert()
# ins2 = likes.insert().values(id = 4, fruits = "graps")
# result2 = conn.execute(ins2)

# result = conn.execute('SELECT * FROM student INNER JOIN likes ON student.id = likes.id').fetchall()
"""output of this query INNER JOIN"""

# (3, 'shyam', 3, 'apple')
# (1, 'arjun', 1, 'orange')
# (1, 'arjun', 1, 'banana')
# (4, 'raju', 4, 'graps')

# result = conn.execute('SELECT student.name,likes.fruits FROM student INNER JOIN likes ON student.id = likes.id').fetchall()
"""output of this query INNER JOIN"""
# ('shyam', 'apple')
# ('arjun', 'orange')
# ('arjun', 'banana')
# ('raju', 'graps')

# result = conn.execute('SELECT student.name,likes.fruits FROM student LEFT JOIN likes ON student.id = likes.id').fetchall()
"""output of this query LEFT JOIN"""
# ('shyam', 'apple')
# ('arjun', 'orange')
# ('arjun', 'banana')
# ('raju', 'graps')
# ('ram', None)
# ('chotu', None)


# result = conn.execute('SELECT student.name,likes.fruits FROM student RIGHT JOIN likes ON student.id = likes.id').fetchall()
"""output of this query RIGHT JOIN"""
# ('shyam', 'apple')
# ('arjun', 'orange')
# ('arjun', 'banana')
# (None, 'mango')
# ('raju', 'graps')

# result = conn.execute('SELECT student.name,likes.fruits FROM student FULL OUTER JOIN likes ON student.id = likes.id').fetchall()
"""output of this query FULL OUTER JOIN"""
# ('shyam', 'apple')
# ('arjun', 'orange')
# ('arjun', 'banana')
# (None, 'mango')
# ('raju', 'graps')
# ('ram', None)
# ('chotu', None)

# result = conn.execute('CREATE INDEX IX_likes ON likes(fruits ASC)')


# conn.execute('CREATE PROCEDURE SP_user_left_join AS BEGIN SELECT student.name,likes.fruits FROM student LEFT JOIN likes ON student.id=likes.id END')



result = conn.execute('left_join()')



for res in result:
    print(res)


# updt = update(user_table).where(user_table.c.empno==996).values(empno=888)
# delt = user_table.delete().where(user_table.c.name=='raj')
# u = delete(user_table).where(user_table.c.name =='Arjun')
# q = user_table.update().where(user_table.c.name=='raj').values(name='Arjun')

# conn.execute(updt)
# conn.execute(delt)
# conn.execute(u) user_table.select()


# result = conn.execute('SELECT * FROM user_table WHERE id=15').fetchall()

# for row in result:
#     print(row)

# 作者: Antenna
# 2026年05月31日12时55分31秒
# Antenna2000@163.com

#排字符串
my_list = "This is a test string from Andrew".split()
print(my_list)

def change_lower(str_name:str):
    return str_name.lower()

#改变了比较规则，不区分大小写，全部按小写排
print(sorted(my_list,key = change_lower))

print("-"*88)#------------------------------------------------

#排元组
student_tuples = [
    ('yier','A',15),
    ('bubu','B',12),
    ('mitao','B',10)
]
#lambda表达式，就是匿名函数
print(sorted(student_tuples,key = lambda x: x[1]))

print("-"*88)#------------------------------------------------

#排对象
class Student:
    def __init__(self,name:str,grade:str,age:int):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        """
        相对于__str__更方便，可以返回非字符串类型
        :return:
        """
        return repr((self.name,self.grade,self.age))

student = Student('yier','A',15)
print(student)
student_objects = [
    Student('yier','A',15),
    Student('bubu','B',12),
    Student('mitao','B',10)
]

print(sorted(student_objects,key = lambda student: student.age))

print("-"*88)#------------------------------------------------

from operator import itemgetter,attrgetter
print('使用operator')
print(sorted(student_tuples,key = itemgetter(1)))
print(sorted(student_objects,key = attrgetter('age')))

print("-"*88)#------------------------------------------------

#多层排序
print(sorted(student_tuples,key = itemgetter(1,2)))
print(sorted(student_objects,key = attrgetter('age','name')))

#lambda也可以实现多层排序
print(sorted(student_tuples,key = lambda x: (x[1],x[2])))

print("-"*88)#------------------------------------------------

#实现第一个升序，第二个降序
print(sorted(student_tuples,key = lambda x: (x[1],-x[2])))

print("-"*88)#------------------------------------------------

#字典中混合list
mydict = { 'Li' : ['M',7],
         'Zhang': ['E',2],
         'Wang' : ['P',3],
         'Du' : ['C',2],
         'Ma' : ['C',9],
         'Zhe' : ['H',7] }

print(sorted(mydict.items(),key = lambda x: x[1][1]))

print("-"*88)#------------------------------------------------

#字典list中混合字典
gameresult = [
         { "name":"Bob", "wins":10, "losses":3, "rating":75.00 },
         { "name":"David", "wins":3, "losses":5, "rating":57.00 },
         { "name":"Carol", "wins":4, "losses":5, "rating":57.00 },
         { "name":"Patty", "wins":9, "losses":3, "rating": 71.48 }]
print(sorted(gameresult,key = lambda x: x["rating"]))

print("-"*88)#------------------------------------------------
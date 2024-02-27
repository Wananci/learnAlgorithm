## 对所有的比较器来说，返回负数的排前面，正数排后面，0无所谓先后 
from functools import cmp_to_key

class Students():
    def __init__(self, name, age, ids) -> None:
        self.name = name
        self.age = age
        self.id = ids

    def getInfo(self):
        return self.name, self.age, self.id

def ageAscendingComparator(stu1: Students, stu2: Students):  ## 与这相似的，可以定义name，ids的排列顺序
    return stu1.age - stu2.age

stu1 = Students('A', 20, 1001)
stu2 = Students('B', 21, 1000)
stu3 = Students('C', 19, 1002)

stuList = [stu1, stu2, stu3]
stuList = sorted(stuList, key=cmp_to_key(ageAscendingComparator))
for stu in stuList: 
    print(stu.getInfo())

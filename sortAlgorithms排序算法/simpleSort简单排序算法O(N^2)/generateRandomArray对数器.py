import random

def naive_sort(arr):
    # 朴素的、简单但正确的排序算法
    return sorted(arr)

def BubbleSort(mylist) -> None:
    '''
        冒泡排序
    '''
    length = len(mylist)
    if (length == 0 or length < 2):
        return mylist
    for i in range(length):
        for j in range(0, length - i - 1):
            if mylist[j] > mylist[j + 1]:
                mylist[j], mylist[j + 1] = mylist[j + 1], mylist[j]
    return mylist

def InsertSort(mylist):
    """
        插入排序
    """
    length = len(mylist)
    for i in range(1, length):
        for j in range(i, 0, -1):
            if mylist[j] < mylist[j - 1]:
                mylist[j], mylist[j - 1] = mylist[j - 1], mylist[j]
            else:
                break
    return mylist

def generateRandomList(maxSize: int, maxValue: int) -> list:
    """对数器
    random.random() * N 生成 [0,N)
    int(random.random() * N) 生成 [0,N-1]
    Args:
        maxSize (int): 最大的尺寸
        maxValue (int): 最大值

    Returns:
        list: 生成的随机数组
    """
    lens = int((maxSize + 1 ) * random.random())
    randomArray = [int((maxValue + 1) * random.random()) - int(maxValue * random.random()) 
                   for _ in range(lens)]
    return randomArray

## 冒泡排序或者插入排序作为对数器
# config
testTime = 100000
boolSucced = True
maxSize = 100
maxValue = 100
testFuc = BubbleSort # InsertSort

## test now!
for _ in range(testTime):
    arr1 = generateRandomList(maxSize, maxValue)
    arr2 = arr1.copy()
    arr1 = naive_sort(arr1)
    arr2 = testFuc(arr2)
    if arr1 != arr2:
        print(f"Test failed for arr1: {arr1}")
        print(f"Test failed for arr2: {arr2}")
        boolSucced = False
        break
if boolSucced:
    print(f"Test Function is {testFuc.__name__}. \nTest succed!")

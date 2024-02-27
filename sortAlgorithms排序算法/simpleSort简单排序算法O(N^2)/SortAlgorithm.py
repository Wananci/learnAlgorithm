def SelectSort(mylist) -> None:
    '''
        选择排序
    '''
    length = len(mylist)
    if (length == 0 or length < 2):
        return mylist
    for i in range(0, length):
        minIndex = i
        for j in range(i + 1, length):
            minIndex = j if mylist[j] < mylist[minIndex] else minIndex
        swap3(mylist, i, minIndex)

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
                swap3(mylist, j, j + 1)

def InsertSort(mylist):
    """插入排序
        思想就是，step1：0-0有序，step2：0-1有序，step3：0-2有序...直到stepN:0-len(list)-1有序
        与前两个排序不同，插入排序的时间复杂度和数据状况有关，但时间复杂度的估计按照最差情况估计，为O(n^2)
    Args:
        mylist (list): 
    """
    length = len(mylist)
    if (length == 0 or length < 2):
        return mylist
    for i in range(1, length):
        for j in range(i, 0, -1):
            if mylist[j] < mylist[j - 1]:
                swap3(mylist, j, j - 1)
            else:
                break
                
def swap(mylist: list, i: int, index: int):
    temp = mylist[i]
    mylist[i] = mylist[index]
    mylist[index] = temp

def swap2(mylist, i, index): 
    '''
    这里通过异或操作进行交换，节省一个变量的空间，感觉没什么用。。。
    并且，当list[i] == list[index]时，异或操作会变成0
    因此，别用！！！！！！！！
    '''
    mylist[i] = mylist[i] ^ mylist[index]
    mylist[index] = mylist[i] ^ mylist[index]
    mylist[i] = mylist[i] ^ mylist[index]

def swap3(mylist, i, index):
    '''属于python交换'''
    mylist[i], mylist[index] = mylist[index], mylist[i]

## test1
list1 = [2, 3, 1, 5, 1, 4, 7, 0]
SelectSort(list1)
print(list1)

## test2
list2 = [9, 8, 7, 6, 4, 3, 5, 1]
BubbleSort(list2)
print(list2)

## test3
list3 = [9, 8, 7, 6, 4, 3, 5, 1]
InsertSort(list3)
print(list3)


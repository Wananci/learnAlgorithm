from singlyLinkedList import *

def create_linked_list_with_cycle(values, pos) -> Node:
    """创建带环的链表，offered by ChatGPT3.5 

    Args:
        values (list): 一个列表
        pos (int): 入环节点
    """
    
    if not values:
        return None

    head = Node(values[0])
    current = head
    cycle_node = None

    for i in range(1, len(values)):
        current.next = Node(values[i])
        current = current.next

        if i == pos:
            cycle_node = current  # 保存环的入口节点

    if pos < len(values):
        current.next = cycle_node  # 构造环

    return head

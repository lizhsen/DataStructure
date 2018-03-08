# -*- coding:utf-8 -*-

"""
在python中，函数名加（），表示返回的是一个函数的结果，不加括号表示的是对函数的调用
"""
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        tmp = Node(item)
        tmp.setNext(self.head)
        self.head = tmp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


    def reverse_list(self,head):
        current = self.head
        previous = None
        h =self.head
        while current:
            current.setNext(previous)



class OrderList():
    """
OrderedList() 创建一个新的空列表。它不需要参数，并返回一个空列表。
add(item) 向列表中添加一个新项。它需要 item 作为参数，并不返回任何内容。假定该 item 不在列表中。
remove(item) 从列表中删除该项。它需要 item 作为参数并修改列表。假设项存在于列表中。
search(item) 搜索列表中的项目。它需要 item 作为参数，并返回一个布尔值。
isEmpty() 检查列表是否为空。它不需要参数，并返回布尔值。
size（）返回列表中的项数。它不需要参数，并返回一个整数。
index(item) 返回项在列表中的位置。它需要 item 作为参数并返回索引。假定该项在列表中。
pop() 删除并返回列表中的最后一个项。假设该列表至少有一个项。
pop(pos) 删除并返回位置 pos 处的项。它需要 pos 作为参数并返回项。假定该项在列表中。
    """
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        tmp = Node(item)
        if previous == None:
            tmp.setNext(self.head)
            self.head = tmp
        else:
            tmp.setNext(current)
            previous.setNext(tmp)


    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


# mylist = UnorderedList()
# mylist.add(1)
# mylist.add(2)
# mylist.add(3)
# mylist.remove(1)
# print(mylist.search(1),mylist.size())


def reverse_list(head):
    """
    反转链表非递归
    """
    if head is None or head.next is None:
        return head
    pre = None
    cur = head
    h = head
    while cur:
        h = cur
        tmp = cur.getNext()
        cur.next = pre
        pre = cur
        cur = tmp
    return h


def reverse_list_s(head, newhead):
    """
    对于递归实现，首先反转从第二个结点到最后一个结点的链表，然后再将头结点放到已反转链表的最后，函数返回新链表的头结点。
    :return:
    """
    if head is None:
        return None
    # 头节点放到已反转链表的最后
    if head.next is None:
        newhead = head
    else:
        # 递归主程序
        newhead = reverse_list_s(head.next, newhead)
        head.next.next = head
        head.next = None
    return newhead


mylist = UnorderedList()
mylist.add(1)
mylist.add(2)
mylist.add(3)
mylist.add(4)
p = mylist.head
while p:
    print(p.getData())
    p = p.getNext()

# reverse_p = reverse_list(mylist.head)
# while reverse_p:
#     print ("######")
#     print(reverse_p.getData())
#     reverse_p = reverse_p.getNext()


newhead = None
reverse_p_s = reverse_list_s(mylist.head, newhead)
while reverse_p_s:
    print ("?????")
    print(reverse_p_s.getData())
    reverse_p_s = reverse_p_s.getNext()








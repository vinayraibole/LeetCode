class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = -1
        
    def get(self, index: int) -> int:
        if self.size < index or index < 0:
            return -1
        else:
            temp = self.head
            for i in range(index):
                temp = temp.next
            return temp.val
    
    def addAtHead(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val)
            self.size += 1
        else:
            temp = self.head
            self.head = Node(val)
            self.head.next = temp
            self.size += 1

    def addAtTail(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val)
            self.size += 1
        else:
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = Node(val)
            self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index - self.size > 1 or index < 0:
            return
        elif index == 0:
            self.addAtHead(val)
        elif index - self.size == 1:
            self.addAtTail(val)
        else:
            temp=self.head
            for i in range(index-1):
                temp = temp.next
            new = Node(val)
            new.next = temp.next
            temp.next = new
            self.size += 1
        
    def deleteAtIndex(self, index: int) -> None:
        if self.get(index) == -1:
            return
        elif index == 0:
            self.head = self.head.next
            self.size -= 1
        else:
            temp = self.head
            for i in range(index - 1):
                temp = temp.next
            temp.next = temp.next.next
            self.size -= 1
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
        
class linkedList:
    def __init__(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1
        
    def addNode(self, value1):
        newNode = Node(value1)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1
        
    def removeNode(self):
        if self.head is None:
            print('Linked List is Empty')
            return
        prev = self.head
        curr = self.head
        while curr.next:
            prev = curr
            curr = curr.next
        self.tail = prev
        self.tail.next = None
        self.length -= 1
        
    def addToBeginning(self, value2):
        newNode = Node(value2)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length+= 1
        return self
    
    
    def removeFromBeginning(self):
        if self.head is None:
            print('The Linked List is Empty')
            return
        prev = self.head
        current = self.head.next
        self.head = current
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        prev.next = None
        return self
        
        
        def get(self,num):
        if num < 0 or num >= self.length:
            return None
        current = self.head
        for i in range(num):
            current = current.next
        return current
    
    def set(self,num,value3):
        current = self.get(num)
        if current:
            current.data = value3
            return True
        return False
    
        
        
def main():
    myList = linkedList('charis')
    myList.addNode(23)
    myList.addNode('talent')
    # myList.addToBeginning(223)
    # myList.removeFromBeginning()
    
    print(myList.head.data)
    # value = myList.head
    # while(value):
    #     print(value.data)
    #     value = value.next
    
main()

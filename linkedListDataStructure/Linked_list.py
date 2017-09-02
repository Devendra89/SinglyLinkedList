
from linkedListDataStructure import Node

class LinkedList(object):
    
    def __init__(self, head= None):
        self.head = head
    
    def insert(self,data):
        new_node = Node.Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        
    def size(self):
        current = self.head
        count = 0 
        while current:
            count += 1
            current = current.get_next()
        return count
    
    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current        
    
    def delete(self,data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data()== data:
                found = True
            else:
                previous = current 
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())                
    def traverseList(self):
         
        actualNode = self.head
         
        while actualNode is not None:
            print("%d" %actualNode.data)
            actualNode = actualNode.next_node                     
        
    #===========================================================================
    # def traverseList(self):
    #     
    #     actualNode = self.head
    #     
    #     while actualNode is not None:
    #         print("%d" %actualNode.data)
    #         actualNode = actualNode.nextNode    
    #     
    # def insertStart(self,data):
    #     self.counter +=1
    #     
    #     newNode = Node(data)
    #     
    #     if not self.head:
    #         self.head = newNode
    #     else:
    #         newNode.nextNode =self.head
    #         self.head = newNode
    # 
    # def size(self):
    #     return self.counter
    # 
    # def insertEnd(self,data):
    #     
    #     if self.head is None:
    #         self.insertStart(data)  
    #         return
    #     self.counter +=1        
    #     newNode = Node(data)
    #     actualNode = self.head;
    #     
    #     while actualNode.nextNode is not None:
    #         actualNode = actualNode.nextNode
    #     
    #     actualNode.nextNode = newNode
    #     
    # def remove(self, data):
    #     self.counter -=1
    #     if self.head:
    #         if data== self.head.data:
    #             self.head = self.head.nextNode
    #         else:
    #             self.head.remove(data, self.head)    
    #===========================================================================
                        
            
                
                    
            
            
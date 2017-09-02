
class Node(object):
    
    def __init__(self,data=None,next_node=None):
        self.data = data
        self.next_node = next_node
        
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next_node
    
    def set_next(self,new_next):
        self.next_node = new_next
    
    
    #===========================================================================
    # def __init__(self,data):
    #     self.data = data
    #     self.nextNode= None;
    # def remove(self,data,previousNode):
    #     if self.data == data:
    #         previousNode.nextNode = self.nextNode
    #         del self.data
    #         del self.nextNode
    #     else:
    #         if self.nextNode is not None:
    #             self.nextNode.remove(data, self)        
    #===========================================================================
    

from linkedListDataStructure import Linked_list

#if __name__=="__main__":
    
linkedList = Linked_list.LinkedList()

linkedList.insert(12)
linkedList.insert(122)
linkedList.insert(3)
linkedList.insert(31)
print(linkedList.traverseList())
print("################")
print(linkedList.search(3))
print("################")
linkedList.delete(12)
print(linkedList.traverseList())
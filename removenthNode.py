class Node:
  def __init__(self, data):
    self.data = data
    self.nextElement = None

class LinkedList:
  def __init__(self):
    self.headNode = None

  def getHead(self):
    return self.headNode




        

class Solution:

    def insert(self,list,value):
    #Creating a new node 
        new_node = Node(value)

        #Checking to see if the list is empty, if it is simply point head to new node      
        if list.getHead() is None:
            list.headNode = new_node
            return

        #if list not empty, traverse the list to the last node
        temp = list.getHead()

        while temp.nextElement is not None:
            temp = temp.nextElement

        #Set the nextElement of the previous node to new node
        temp.nextElement = new_node
        return


    def remove(self,head,n):
        dummy=LinkedList()
        dummy.next=head
        fast=slow=dummy

        for _ in range(n):
            fast=fast.next
        while fast and fast.next:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return dummy.next


kel=Solution()
l=LinkedList()
kel.insert(2)
kel.insert(3)
kel.insert(4)
kel.insert(5)

while(l):
    print(l.val)
    l=l.next

print(l)

print(kel.remove(l,2))
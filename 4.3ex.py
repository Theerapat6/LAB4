class Node:
   def __init__(self, data=None):
      self.data_val = data
      self.next = None

class llist:
    def __init__(self):
        self.head = None
    def list(self):
      val = self.head
      while val is not None:
         print (val.data_val ,end = "\t")
         val = val.next

linkli = llist()
nnode0 = Node(44)
linkli.headval = nnode0
nnode1 = Node(36)
nnode2 = Node(90)
nnode3 = Node(10)
nnode4 = Node(60)
nnode5 = Node(99)

linkli.headval.next = nnode1
nnode1.next = nnode2
nnode2.next = nnode3
nnode3.next = nnode4
nnode4.next = nnode5

nodeR = Node(104)
nodeR.next = nnode0
linkli.head =nodeR

nodeO = Node(57)
nnode5.next = nodeO

nnode2.next = nnode4
nnode3.next = None

linkli.list()
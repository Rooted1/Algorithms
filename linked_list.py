from node import Node

class LinkedList:
  def __init__(self, head_node = None):
    self.head = head_node

  def add(self, val):
    new_head = Node(val)
    new_head.next = self.head
    self.head = new_head

  def insert(self, node_value, location):
    if not location:
      new_head = Node(node_value)
      new_head.next = self.head
      self.head = new_head
      return self

    prev = self.head
    node = Node(node_value)
    current_node = self.head.next

    while location > 1:
      prev = current_node
      current_node = current_node.next
      location -= 1
    
    prev.next = node
    node.next = current_node

    return self

# get nth element from last
  def n_from_last(self, n):
    if n > self.size():
      return None
    nodes_remaining = self.size() - 1 - n
    result = self.head 

    while nodes_remaining:
      result = result.next
      nodes_remaining -= 1

    return result
    
  def traverse(self):
    head = self.head
    print("Starting traversal from head")
    while head:
      print("visiting node: {0}".format(head.val))
      head = head.next
    print("Traversal complete")
    
  def size(self):
    node_count = 0
    current_node = self.head
    while current_node:
      node_count += 1
      current_node = current_node.next
    return node_count
  
  def __repr__(self):
    text = ''
    head = self.head
    while head:
      text += str(head.val) + ' -> '
      head = head.next
    return text
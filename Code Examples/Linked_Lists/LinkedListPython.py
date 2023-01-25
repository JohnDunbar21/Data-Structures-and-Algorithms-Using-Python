"""
Basic Node class with getters and setters.
"""
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

"""
Linked List class with beginning insertion, removal, swap, and string method.
"""
class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node

  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while(current_node != None):
      if(current_node.get_value() != None):
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list


  def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    if(current_node.get_value() == value_to_remove):
      self.head_node = current_node.get_next_node()
    else:
      while(current_node != None):
        next_node = current_node.get_next_node()
        if(next_node.get_value() == value_to_remove):
          current_node.set_next_node(next_node.get_next_node())
          current_node = None
        else:
          current_node = next_node

  def swap_nodes(self, input_list, val1, val2):
    node1_prev = None
    node2_prev = None
    node1 = self.head_node
    node2 = self.head_node

    if val1 == val2:
        print("Elements are the same - no swap needed")
        return

    while node1 is not None:
        if node1.get_value() == val1:
            break
        node1_prev = node1
        node1 = node1.get_next_node()

    while node2 is not None:
        if node2.get_value() == val2:
            break
        node2_prev = node2
        node2 = node2.get_next_node()

    if (node1 is None or node2 is None):
        print("Swap not possible - one or more element is not in the list")
        return

    if node1_prev is None:
        self.head_node = node2
    else:
        node1_prev.set_next_node(node2)

    if node2_prev is None:
        self.head_node = node1
    else:
        node2_prev.set_next_node(node1)

    temp = node1.get_next_node()
    node1.set_next_node(node2.get_next_node())
    node2.set_next_node(temp)


  def nth_last_node(self, n):
    current = None
    tail_seeker = self.head_node
    count = 1
    while tail_seeker:
        tail_seeker = tail_seeker.get_next_node()
        count += 1
        if count >= n + 1:
            if current is None:
                current = self.head_node
            else:
                current = current.get_next_node()
    return current

  def find_middle(self):
    fast = self.head_node
    slow = self.head_node
    while(fast != None):
        fast = fast.get_next_node()
        if(fast != None):
            fast = fast.get_next_node()
            slow = slow.get_next_node()
    return slow


  
"""
Test code
"""
linked_list = LinkedList(5)
linked_list.insert_beginning(70)
linked_list.insert_beginning(5675)
linked_list.insert_beginning(575)
linked_list.insert_beginning(65)
linked_list.insert_beginning(55)
linked_list.insert_beginning(90)

print("Original List")
print(linked_list.stringify_list())

linked_list.remove_node(70)

print("List After Removing 70")
print(linked_list.stringify_list())

linked_list.swap_nodes(linked_list, 90, 5)

print("List After Swapping 90 and 5")
print(linked_list.stringify_list())

print("Second Last Node")
nth_last_value = linked_list.nth_last_node(2)
print(nth_last_value.get_value())

print("Middle Node")
middle_node = linked_list.find_middle()
print(middle_node.get_value())
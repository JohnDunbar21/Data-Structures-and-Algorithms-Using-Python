"""
Basic node structure with getters and a setter for the pointer.
"""
class Node:
  def __init__(self, value, link_node=None):
    self.value = value
    self.link_node = link_node
    
  def set_link_node(self, link_node):
    self.link_node = link_node
    
  def get_link_node(self):
    return self.link_node
  
  def get_value(self):
    return self.value

"""
Creates three instances of the Node class
"""
yacko = Node("likes to yak")
wacko = Node("has a penchant for hoarding snacks")
dot = Node("enjoys spending time in movie lots")

"""
Sets the link node for two of the nodes
"""
yacko.set_link_node(dot)
dot.set_link_node(wacko)

"""
Retrieves the data stored in the nodes which have pointers to another node
"""
dots_data = yacko.get_link_node().get_value()
wackos_data = dot.get_link_node().get_value()

print(dots_data)
print(wackos_data)
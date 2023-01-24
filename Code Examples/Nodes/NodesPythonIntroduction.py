"""
Basic node structure that takes a data value. The pointer is set to 'None' by default.
"""
class Node:
  
  def __init__(self, value, link_node=None):
    self.value = value
    self.link_node = link_node
# Nodes

A __node__ is the fundamental component of any data structure, forming the basis of linked lists, stacks, queues, trees, etc.

An individual node will __contain data and links to other nodes__, where each data structure will add a different constraint or behaviour to create the desired structure.

## Node Implementations

The data stored in a node is limited solely by the programming language you use. A Link, or links, within a node are also known as __pointers__ (this is because they 'point' to another node).

A data structure typically implements nodes with __one or more__ pointers. If a pointer is `null`, then it means you have no further data stored in that particular path of the data structure.

## Node Linking

Depending on the data structure, nodes may only be linked to one other node. In this situation, components __must__ be carefully removed from the structure. If a node is removed carelessly, additional nodes may be compromised and be inaccessible to the application. This is called __orphaning__ whereby a node has no pointers to any other node.
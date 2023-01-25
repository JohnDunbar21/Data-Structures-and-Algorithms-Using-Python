# Linked Lists

The linked list serves as the foundation for more complex data structures, comprised of a series of nodes, it possesses a head, tail, and body. The linked list is terminated when a node's link is `None`.

Since nodes use links to denote the next node in the sequence, they are not required to be sequentially located in memory. This also means that insertion and removal is quick.

## Adding and Removing from a Linked List

### Adding a New Node

Adding a node to the beginning of the linked list means having to link the new head node to the current head node: in doing this, the connection with the following link nodes is maintained.

### Removing a Node

If not done carefully, removing a node can result in data being lost, creating orphaned nodes.

When removing a node, the links __must__ be updated to ensure data integrity.
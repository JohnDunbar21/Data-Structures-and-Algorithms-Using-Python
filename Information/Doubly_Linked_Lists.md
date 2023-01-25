# Doubly Linked Lists

The nodes in a doubly linked list contain three data values:

- Pointer to previous node
    - In the head node, this will be `None`
- Data node
- Pointer to next node
    - In the tail node, this will be `None`

## Adding to a Doubly Linked List

### Adding to the Head

When adding to the head, we must first check to see if there is a current head of the list: if not, then the list is empty and can make the new node both the head and tail whereby both pointers are `None`.

If the list is __not__ empty, then:

- Set the current head's position to the new head
- Set the new head's next pointer to the current head
- Set the new head's previous pointer to `None`

### Adding to the Tail

If the list is empty, we make a new node which is both the head and tail of the list, setting its pointers to `None`.

If the list is __not__ empty, then:

- Set the current tail's pointer to the new tail
- Set the new tail's previous pointer to the current tail
- Set the new tail's next pointer to `None`

## Removing from a Doubly Linked List

### Removing the Head

To remove the head, we set the previous pointer of the new head to `None` and update the head attribute of the list.

### Removing the Tail

To remove the tail, we set the next pointer of the new tail to `None` and update the tail attribute of the list.

### Removing from the Middle of the List

To remove an item from the middle of a list, we must:

- Set the prior node's next pointer to the removed node's next pointer
- Set the next node's previous pointer to the removed node's previous pointer
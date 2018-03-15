# Deque

A Deque (Double ended queue) is a variant of a Queue Abstract Data Structure which allows insertion and removal operations from either the front or the back of the list.

![deque](https://www.codeproject.com/KB/recipes/669131/deque.png)

A deque differs from the Queue in that it does not require FIFO constraints. Both Queues and Stacks can be considered specializations of deques, and can be implemented as composed deques!

## Common Deque Properties
- `front`
- `back`
- `is_empty`
- `_size`

## Common API Methods
- `insert_front()`
- `insert_back()`
- `remove_front()`
- `remove_back()`
- `find_nth_from[_front | _back]()`

## Practical application examples
- A real-world model of a ticket line (there need to be concessions for 'cutting' in line)
- A size limit can be applied to the deque which would allow for an implementation of the browsers history api

## Resources
- [Geeks for Geeks: Deque](https://www.geeksforgeeks.org/deque-set-1-introduction-applications/)
- [Deque Wiki](https://en.wikipedia.org/wiki/Double-ended_queue)

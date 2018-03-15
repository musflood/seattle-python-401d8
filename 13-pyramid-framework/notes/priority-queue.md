# Priority Queues

A priority queue in computer science terms relates to a basic or equivalent queue data structure, with the additional consideration of a priority value which dictates a higher level of ordering than the standard first in first out ordering.

Priority queues are often implemented with Heaps given the additional implementation considerations of
performance impact; i.e. O(1) insertions and O(N/K) removals, where K represents the number of Heaps utilized to group priorities.

![priorityQ](https://netmatze.files.wordpress.com/2014/08/priorityqueue.png)

## Common API Implementations
- `is_empty()` returns boolean value depending on whether there is anything in the queue
- `insert_with_priority()` inserts a new node into the queue, specifically into the heap grouping of that priority
- `pull_highest_priority()` removes a node from the heap with the highest priority



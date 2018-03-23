# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 05: Linked Lists

## Implement a Singly Linked List
**This is a solo assignment**

### Specification
- Create a new branch in your `data-structures-and-algorithms` repository called `linked-list`. **If you call it anything else, you will get ZERO CREDIT with NO COMMENTS**
- Create two files called `node.py` and `linked_list.py` in your `linked_list` directory
- Create a Class for a `Node` which is aware of the value as `val` and next as `_next`
    - Ensure that you have a `__str__` method defined to return the value of the node when printed
- Create a Class for a `LinkedList` which creates an empty Linked List when instantiated.
    - This class should be aware of a default `None` value assigned to `head` when the list is created.
    - This class should be aware of the `len` of the list, which represents the count of Nodes in the list at any time
    - This class should have the ability to accept an iterable as an argument when instantiated, such as `[1, 2, 3, 4]`, and creates a new Node in the list for each value in the iterable.
    - Define any further magic methods such as `len` and `str` to support user functionality and informative responses.
    - Define a method called `insert` which takes any value as an argument and adds that value to the `head` of the list with an O(1) Time performance.
    - Define a method called `find` which takes any value as an argument and returns `True` or `False` depending on whether that value exists as a Node value within the list.

- At no time should an exception or stack trace be show to the end user. Catch and handle any such exceptions and return a printed value or operation which cleanly represents the state and either Stops execution cleanly or provides the user with clear direction and output.
- Every bit of functionality that you have should be tested and documented.


### Submission
1. Create a pull request from your `linked-list` branch to your `master` branch.
2. In your open pull request, leave as a comment [a checklist](https://github.com/blog/1825-task-lists-in-all-markdown-documents) of the specifications, with the actual specifications you completed checked off.
3. Copy the link to your open pull request and paste it into the corresponding Canvas assignment.
4. Leave any comments you may have about the assignment in the comments box. This includes any difficulties you may have had with the assignment.
5. Merge `linked-list` into `master`

---

## Practice Statistics Basics
Over the next few weeks we'll be diving into the land of probability, statistics, data science, and machine learning.
To prime the pump a bit, it'd help to practice some of the basics of mathematics and statistics.

[Khan Academy](https://www.khanacademy.org/math/) has pretty good math resources.
Specifically you're going to want to visit...

- [Algebra 1](https://www.khanacademy.org/math/algebra)
- [Statistics and Probability](https://www.khanacademy.org/math/statistics-probability)

### Submission
There is no submission for this assignment.

---

## Learning Journal
Refer to the daily whiteboard challenge assignment in Canvas

---

## Coding Challenge
Refer to the daily whiteboard challenge assignment in Canvas

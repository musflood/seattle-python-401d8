# ![cf](http://i.imgur.com/7v5ASc8.png) Class 15: Binary Trees

## Implement a Binary Search Tree

**This is a solo assignment**

### Specifications
- Create a new branch in your `data-structures-and-algorithms` repository called `bst`. **If you call it anything else, you will get ZERO CREDIT with NO COMMENTS**
- Create a new directoruy called `binary_search_tree/`, with all of your standard module configuration for each directory
    - `__init__.py`, `README.md`, etc.
- Create a file called `bst.py`, as well as a test file and a config file for your tests.

- In `bst.py`:
    - Create a Class or a `Node` which is aware of the value as `val` and left and right children as `left` and `right` respectively
        - Ensure that you have a `__repr__` and `__str__` method defined to return appropriate representations of the node
    - Create a Class for a `BST`, which is aware of the root of the tree as `root`
        - Ensure that you have a `__repr__` and `__str__` method defined to return appropriate representations of the tree
        - This class should accept an iterable as an argument when initialized, such as `[1, 2, 3, 4]`, which creates a tree from that argument
        - This class should be aware of depth-first traversal methods for `in_order`, `pre_order`, and `post_order` traversals
        - This class should have the ability to `insert` a new node into the tree. Your insertion should follow an O(log n) search solution to find the correct place for inserting the new node.

- Ensure that your class and any subsequent methods are properly tested, and that your test coverage is above 80%.


### Submission
1. Create a pull request from your `bst` branch to your `master` branch.
2. In your open pull request, leave as a comment [a checklist](https://github.com/blog/1825-task-lists-in-all-markdown-documents) of the specifications, with the actual specifications you completed checked off.
3. Copy the link to your open pull request and paste it into the corresponding Canvas assignment.
4. Leave any comments you may have about the assignment in the comments box. This includes any difficulties you may have had with the assignment.
5. Merge `bst` into `master`


---

## Project Prep: Model Your Problem Domain
Refer to the Project Prep assignment in Canvas

---

## Learning Journal
Refer to the daily whiteboard challenge assignment in Canvas

---

## Coding Challenge
Refer to the daily whiteboard challenge assignment in Canvas

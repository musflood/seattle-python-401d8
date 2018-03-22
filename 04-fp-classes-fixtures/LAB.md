# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 04: Functional Programming, Python Classes, and Fixtures

## The Snakes Cafe: Step 4

**This is a partnered assignment**

You're continuing to build a command-line restaurant.
### Specifications

- Create a new branch in your `snakes-cafe` repository called `class-04-objects`. **If you call it anything else, you will get ZERO CREDIT with NO COMMENTS**
- Every menu category should have at least 12 items
- Create an `Order` class. Whatever means you were using to build orders before, replace them with methods and attributes belonging to this class.
    + Every `Order` should have a uuid
    + Every `Order` should have an `add_item` method that takes an item name and a quantity as arguments. There should be a default value for quantity if none is given.
    + Every `Order` should have a `remove_item` method that takes an item name and a quantity as arguments. There should be a default value for quantity if none is given.
    + Every `Order` should have a `display_order()` method that prints the user's current order to the console
    + Every `Order` should have a `print_receipt()` method that creates a file containing the text of the user's full order. The file name should be of the format `order-<the uuid>.txt` and should have the same output as `display_order`
    + All of the order input-checking that you used to do will be done by this class
    + The repr of `Order` instances should look like `<Order #ba99d8... | Items: 4 | Total: $754.23>`
    + When `print()` is called on an order instance, the user's current order is printed as if `display_order` was called.
    + When `len()` is called on an order instance, the number of items in the order is returned
    + You may have as many helper methods as you want. However, make sure that any attributes and methods that aren't intended for public use are prefixed with a single underscore
    + All of your methods should be narrow in scope
- Every bit of functionality that you have should be tested and documented.


### Submission

1. Create a pull request from your `class-04-objects` branch to your `master` branch.
2. In your open pull request, leave as a comment [a checklist](https://github.com/blog/1825-task-lists-in-all-markdown-documents) of the specifications, with the actual specifications you completed checked off.
3. Copy the link to your open pull request and paste it into the corresponding Canvas assignment.
4. Leave any comments you may have about the assignment in the comments box. This includes any difficulties you may have had with the assignment.
5. Merge `class-04-objects` into `master`

---

## Learning Journal
Refer to the daily whiteboard challenge assignment in Canvas

---

## Coding Challenge
Refer to the daily whiteboard challenge assignment in Canvas

# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 03: Errors, Files, and Packaging

## The Snakes Cafe: Step 3

**This is a partnered assignment**

You're continuing to build a command-line restaurant.

### Specifications

- Create a new branch in your `snakes-cafe` repository called `class-03-robust`. **If you call it anything else, you will get ZERO CREDIT with NO COMMENTS**
<!-- - Turn your `snakes-cafe` project into a Python package with the correct metadata for the name, authors, required installable packages, and any extras for testing -->
- Every menu category should have at least 9 items
- Add to your `snakes-cafe` project the option to provide a separate file as a menu with the appropriate help text (see [Lecture 01](../01-intro-to-python/notes/user_input.md)). If this option isn't used, the menu you've been building all week will be used.
- The optional separate menu must be a comma-separated value (`.csv`) file, where each row includes the menu item's name (str), category (str), price (float), and quantity (int) referring to the in-stock amount of that item.
- If the provided separate menu file isn't a CSV file, alert the user with an appropriate error message. Continue processing with the default menu. **Note: the user should never see an actual Python Exception**
- When the user adds an item to their order, they should have the option of providing the quantity as well.
    - If they don't provide the quantity, a quantity of 1 is assumed.
    - If the quantity they provide is invalid (negative or not a number), alert the user with an appropriate error message
    - If the quantity they provide is beyond whatever is left in stock, alert the user with an appropriate error message.
- If the user tries to add/remove an item that isn't on whatever menu has been loaded, alert the user with an appropriate error message
- If the user tries to remove an item that isn't a part of their order, alert the user with an appropriate error message
- No matter what, the user should never see a traceback. Not even for a Keyboard Interrupt.
- Every bit of functionality that you add should be tested.


### Submission

1. Create a pull request from your `class-03-robust` branch to your `master` branch.
2. In your open pull request, leave as a comment [a checklist](https://github.com/blog/1825-task-lists-in-all-markdown-documents) of the specifications, with the actual specifications you completed checked off.
3. Copy the link to your open pull request and paste it into the corresponding Canvas assignment.
4. Leave any comments you may have about the assignment in the comments box. This includes any difficulties you may have had with the assignment.
5. Merge `class-03-robust` into `master`

---

## Learning Journal
Refer to the daily whiteboard challenge assignment in Canvas

---

## Coding Challenge
Refer to the daily whiteboard challenge assignment in Canvas

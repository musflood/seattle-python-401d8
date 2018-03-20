# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 02: Modules, Containers, and Testing

## The Snakes Cafe: Test Plan

**This is a partnered assignment**

You're writing a test plan for today's Snake's Cafe assignment.
**It is recommended that you complete yesterday before you write a test plan or any code for your assignments today**.

### Specifications
- Create a markdown document called `test_plan.md` in your `snakes-cafe` repository on today's branch, `class-02-tdd`.
- List out in words each test that you intend to write
- For each test that you intend to write, name the function or functions that you intend to call and test
- If you change your tests, update your test plan

### Submission
1. Copy the markdown text from your test plan and paste it into the corresponding Canvas assignment
2. Submit the assignment

---

## The Snakes Cafe: Step 2

**This is a partnered assignment**

You're continuing to build a command-line restaurant

### Specifications
- Work on your daily branch in your `snakes-cafe` repository called `class-02-tdd`. **If you call it anything else, you will get ZERO CREDIT with NO COMMENTS**
- Your menu should get a "Sides" category
- Every menu category should have at least 6 items
- Your menu items should all get prices. Use whatever currency symbol you want, but make sure that the user knows what the prices and currencies are.
- Whenever the user adds an item to their order, they're notified of the total cost of their order up to that point.
- If the user types `order`, their entire order is printed to the console. For example:
```
*******************************************
The Snakes Cafe
"Eatability Counts"

Order #ba99d80b-fdb7-497d-b1be-e5b70164e1de
===========================================
Wings x1                              $2.00
Spring Rolls x3                       $7.50
Steak x1                             $12.00
Blood of the Innocent x1            $666.66
-------------------------------------------
Subtotal                            $688.16
Sales Tax                            $66.07
---------
Total Due                           $754.23
*******************************************
```
- Every order should get a universally unique identifier. Consider using the [uuid](https://docs.python.org/3/library/uuid.html#uuid.uuid4) package
- In the `order` printout you must include sales tax (9.6% in Seattle as of 2018) in the final total (round up to 2 decimal places)
- In the `order` printout, all of the costs should be right-justified, and all of the item names should be left-justified
- If the user types `menu`, the entire menu is printed to the console
- If the user types the name of any of your categories, the items in that category should be printed to the console
- If the user types `remove <ITEM NAME>`, 1 item of the type `<ITEM NAME>` should be removed from their order, and their order's total should be printed to the screen
- All input should be case-insensitive
- Keep your functions small, concise, and testable. **Every function that you write should be tested and documented**. The only functions that are exempt are the ones that take user input. Also, the `if __name__ == '__main__'` block does not need to be tested


### Submission
1. Create a pull request from your `class-02-tdd` branch to your `master` branch.
2. In your open pull request, leave as a comment [a checklist](https://github.com/blog/1825-task-lists-in-all-markdown-documents) of the specifications, with the actual specifications you completed checked off.
3. Copy the link to your open pull request and paste it into the corresponding Canvas assignment.
4. Leave any comments you may have about the assignment in the comments box. This includes any difficulties you may have had with the assignment.
5. Merge `class-02-tdd` into `master`

---

## Learning Journal
Refer to the daily whiteboard challenge assignment in Canvas

---

## Coding Challenge
Refer to the daily whiteboard challenge assignment in Canvas

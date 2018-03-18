# Day of Code

A programming language is simply syntactical sugar that describes logical processes.
The best way to learn how to use that syntactical sugar is to practice implementing your logic and strategy while speaking that language.
As such, I want you to spend every day writing a boatload of Python code.
Here’s an assignment to help facilitate that.

If you don’t already have one, create an account on Code Wars.
Set your language of choice to “Python”.

Code Wars is a website that allows you to take on a number of user-supplied code challenges in one of a host of languages.
The difficulty level for a given code challenge is set by the “kyu”.
**8th kyu** is the simplest level, testing more of the basic understanding of the language.
**7th kyu** is more complex and requires a slightly deeper understanding of language fundamentals.
**6th kyu** increases the complexity in thought and application, etc.
Every step down in kyu represents a substantially significant increase in difficulty.

**Your goal is to complete, on your own, 20 credits-worth of code challenges by 11:59pm. IF YOU DO NOT SUBMIT BY THIS TIME YOU WILL GET ZERO CREDIT**.
Here’s what this means in terms of what you’ll be attacking.
Each...

- 8th kyu: 1 credit
- 7th kyu: 2 credits
- 6th kyu: 4 credits
- 5th kyu: 5 credits
- 4th kyu: 7 credits
- 3rd kyu: 8 credits
- 2nd kyu: 10 credits
- 1st kyu: 20 credits

For reference, my profile is at the 5th kyu, and the person holding Position 1 in the Code Fellows clan is at the 2nd kyu.
The steps up in difficulty are, again, *significant*.

**You will need to budget your time well.**
If you wish to challenge yourself, step up in level.
Otherwise, stay at the level you’re comfortable and simply complete the challenges.
Assess your own capability as accurately as you can, and remember [the story of Icarus](https://en.wikipedia.org/wiki/Icarus).

### Specifications

- Create a branch in your `data-structures-and-katas` repository called `day-of-code`.
- For every code challenge that you complete, create a new **Python module** using the name of the challenge. At the top of the file, above all of your code, write a doc string that includes the “Best Practices” #1 solution. For example:

```python
"""Kata: Opposite Number - Return the opposite of the input number.

#1 Best Practices Solution by CrazyMerlyn & others

def opposite(number):
    return -number
"""
```

- Create an accompanying test file for each module you write. **Re-write the tests that are given to you by Code Wars using Pytest.** Add another 4 tests of your own to those, and ensure that they all pass.
- For code challenge that you complete, add to your `README.md` a line listing out the title and URL of of that code challenge, as well as the module name and test file for each. For example:

```markdown
## Completed Katas

**Opposite Number (8th kyu)**

- **Module**: `opposite_number.py`
- **Tests**: `test_opposite_number.py`
- **URL**: [challenge url](https://www.codewars.com/kata/opposite-number)

**Invert Values (8th kyu)**
...
```

## Submission

**IF YOU DO NOT SUBMIT IN TIME THEN YOU WILL GET ZERO CREDIT. THERE WILL BE NO RESUBMISSIONS FOR THIS ASSIGNMENT AFTER 11:59PM**

1. Create a pull request from your `day-of-code` branch to your `master` branch
2. In your open pull request, leave as a comment [a checklist](https://github.com/blog/1825-task-lists-in-all-markdown-documents) of the specifications, with the actual specifications you completed checked off.
3. Copy the link to your open pull request and paste it into the corresponding Canvas assignment.
4. Leave any comments you may have about the assignment in the comments box. This includes any difficulties you may have had with the assignment.
5. Merge `day-of-code` into `master`
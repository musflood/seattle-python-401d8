# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 06: Aggregate Analysis

## Describe and Visualize a Data Set

**This is a solo assignment**

The best way to hone your data analysis skills is consistent, deliberate practice.
One of the best places to acquire data for analysis is [Kaggle](https://www.kaggle.com/), so practice your abilities with some [Kaggle](https://www.kaggle.com/datasets) data sets.
Sign up for a Kaggle account (if you don't already have one).

### Specifications

- Create a repository called `data-science` and in that repository create a branch called `class-06-aggregation`
- Find and download the following data sets:
    + [Video Game Sales](https://www.kaggle.com/gregorut/videogamesales) - Sales data from more than 16,500 games
    + [Cycle Share Dataset](https://www.kaggle.com/pronto/cycle-share-dataset) - Bicycle Trip Data from Seattle's Cycle Share System
- Start two Jupyter Notebooks called `vg-stats` and `bike-stats`
- Add a markdown cell at the top of each notebook with the title of this assignment, an appropriate name for the data set, as well as your name and the date
- Load up each of these data sets into a Pandas DataFrame within each respective file.
    - _NOTE: There's an issue with one of the CSV files. You will need to find a way to handle that error... Google it, and work around it!_

- In the `vg-stats` notebook answer the following questions/do the following tasks. Note that the numbers quoted for sales are in the millions, and apply only for those games with over 100,000 sales.:
    1. Which company is the most common video game publisher?
    1. What’s the most common platform?
    1. What about the most common genre?
    1. What are the top 20 highest grossing games?
    1. For North American video game sales, what’s the median?
        - Provide a secondary output showing 'about' ten games surrounding the median sales output
    1. For the top-selling game of all time, how many standard deviations above/below the mean are its sales for North America?
    1. The Nintendo Wii seems to have outdone itself with games. How does its average number of sales compare with all of the other platforms?
    1. Come up with 3 more questions that can be answered with this data set.

- In the `bike-stats` notebook, answer the following questions/do the following tasks:
    1. What is the average trip duration for a borrowed bicycle?
    1. What's the most common age of a bicycle-sharer?
    1. Given all the weather data here, find the average precipitation per month, and the median precipitation.
    1. What’s the average number of bikes at a given bike station?
    1. When a bike station is modified, is it more likely that it’ll lose bikes or gain bikes? How do you know?
    1. Come up with 3 more questions that can be answered with this data set.
- When you're done answering all of the questions for each data set, clean up your notebooks leaving only cells that contain relevant data and calculations. Then restart and run your notebook so that the cell numbering is sequential from top to bottom

- **Have fun with the data!! Play around a bit, and see if there's anything else you can/want to do with the info available!**


### Submission

1. Create a pull request from your `class-06-aggregation` branch to your `master` branch.
2. In your open pull request, leave as a comment [a checklist](https://github.com/blog/1825-task-lists-in-all-markdown-documents) of the specifications, with the actual specifications you completed checked off.
3. Copy the link to your open pull request and paste it into the corresponding Canvas assignment.
4. Leave any comments you may have about the assignment in the comments box. This includes any difficulties you may have had with the assignment.
5. Merge `class-06-aggregation` into `master`

---

## Learning Journal
Refer to the daily whiteboard challenge assignment in Canvas

---

## Coding Challenge
Refer to the daily whiteboard challenge assignment in Canvas

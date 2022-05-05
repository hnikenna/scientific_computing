# Scientific Computing Projects with Python


### Table of Content
* Arithmetic Formatter
* Budget App
* Polygon Area Calculator
* Probability Calculator
* Time Calculator

[Arithmetic Formatter](arithmetic_formatter.py): I created a function `arithmetic_arranger()` 
that receives a list of strings that are arithmetic problems and 
returns the problems arranged vertically and side-by-side. 
>The function optionally takes a second argument that displays the answers when set to True.

[Budget App](budget_app.py): This project contains a class _Category_
that instantiates objects based on different budget categories like
food, clothing, and entertainment. The class also contains multiple 
methods like deposit, withdraw, get_balance, transfer and check_funds
that performs these operations of a finance management system.

[Polygon Area Calculator](polygon_area_calculator.py):
In this project I use **Object Oriented Programming** to create a 
Rectangle class and a Square class. The Square class is a 
subclass of Rectangle and inherit methods and attributes like `get_area()`,
 `get_diagonal()`, `get_picture()` that calculates different parameters
and also displays the image of how an input would look like.

[Probability Calculator](probability_calculator.py):
Suppose there is a hat containing 5 blue balls, 4 red balls, and 2 green balls. What is the probability that a random draw of 4 balls will contain at least 1 red ball and 2 green balls? While it would be possible to calculate the probability using advanced mathematics, an easier way is to write a program to perform a large number of experiments to estimate an approximate probability.

For this project, I wrote a program to determine the approximate probability of drawing certain balls randomly from a hat.

[Time Calculator](time_calculator.py):
Here a function named `add_time()` takes in two required parameters and one optional parameter:

* a start time in the 12-hour clock format (ending in AM or PM)
* a duration time that indicates the number of hours and minutes
(optional)
* a starting day of the week, case insensitive

The function adds the duration time and the start time and returns the result.

>If the result will be the next day, it shows (next day) after the time. If the result will be more than one day later, it shows (n days later) after the time, where "n" is the number of days later.

>If the function is given the optional starting day of the week parameter, then the output displays the day of the week of the result. 

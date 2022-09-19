# Intensive Foundations of Computer Science
This was the first CS class that I ever took and was also the first of four bridge classes designed to prepare those with non CS backgrounds for the program. This repo holds my [homework](/Homework), [labs](/Labs), and [project](/Project) work that I completed while taking this course.

## Course Topics
As this was an intro foundations class, we covered a lot of ground in 15 weeks:
  - Variables, strings, arithmetic operations
  - Functions and parameter passing; testing and debugging
  - Conditionals, boolean expressions, strings
  - Iteration (while loops, for loops) and strings
  - Lists and dictionaries
  - Recursion
  - File processing; exception handling
  - Classes and objects; stacks and queues
  - Event-driven programming
  - Program efficiency; search + sort

## Final Project
Four our final project, we had to create a Connect Four game using all of the knowledge gained from the course.
![Connect Four Screenshot](/Project/screenshot.jpg)

My project has the following features:
  - Text interface that allows the user to select or input:
    - if they want to play agains the computer or another human
    - their name (two names if playing against another human)
    - the color of their game piece (either red or yellow)
    - if they want to use default board dimensions (and the # row and # cols if not)
  - A visual interface that shows:
    - any saved scores (that are saved and read from text files)
    - active user / current turn
    - a simple animation showing a piece falling into place onto the board
    - error message if human user tries to place a piece in a full column
    - winner of the game and subsequent save success
  - Game play where:
    - human user(s) click an arrow to drop a game piece
    - computer user randomly drops a piece in any open column
    - after each move is made, a check is done for a line of any four colors
    - human player results are saved and loaded via .txt files

You can browse my final submission code [here](/Project/submission) and watch a quick video demo [here](https://youtu.be/csNT23PWrr4)

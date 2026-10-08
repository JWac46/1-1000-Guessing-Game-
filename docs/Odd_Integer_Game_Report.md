# **Odd Integer Guessing Game Report**

**Participants:**

* Jackson Waclawski  
* Doug Varney  
* Cameron Nebel

## **Development Process**

For this project, our group created a Python guessing game where the player guesses an odd integer between 1 and 1000\. We used GitHub to collaborate, share code, review each other's work, and track our progress through commits.

We worked together by dividing up parts of the project and checking each other's code. After making changes, we tested the program and fixed any problems we found. We continued this process until the game was running correctly without errors.

## **Test-Driven Development**

We used Python's unittest library to test the game. Our tests check that both the player's input and the game's answer are odd numbers.

def test\_input(self):  
    testGame \= Guess\_Game()  
    guess \= testGame.get\_input()  
    self.assertTrue(guess % 2 \!= 0\)

def test\_answer(self):  
    testGame \= Guess\_Game()  
    answer \= testGame.get\_answer()  
    self.assertTrue(answer % 2 \!= 0\)

These tests helped us catch problems and make sure the main parts of the game were working correctly.

## **GitHub and Collaboration**

GitHub allowed us to work on the same project and keep track of everyone's contributions. We used commits to record changes and reviewed each other's code before finishing the project.

Working together made debugging easier because another person could find problems that the original programmer might not notice.

## **Challenges and Solutions**

Our main challenges involved getting the game and unit tests to work correctly together. When we found problems, we looked at the errors, reviewed the code together, and made changes. We then ran the tests again to make sure the problem was fixed.

## **Pair Programming**

Pair programming helped us solve problems faster because we could discuss the code and get another person's perspective. It also helped us understand parts of the project that we did not write ourselves.

This is similar to real software development because developers regularly work together, review code, use GitHub, and help each other debug problems.

## **Conclusion**

This project gave us experience with Python, unit testing, GitHub, and teamwork. Using pair programming and code reviews helped us find and fix problems. The project also showed us how collaboration and testing are important parts of real software development.


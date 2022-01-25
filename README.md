# Battleship Royale

Battleship Royale is a Python terminal based game, that users can play and control with their keybord.

Based on the original Battleship board game, players will fire missiles at their opponents ships in n attempt to sink them all before the enemy sinks all of theirs.

<img src="assets/images/readme/am-i-responsive-quizzical-min.PNG">

## Gameplay
<hr>
Player will initially be prompted to add their name before they pick their difficulty level.<br>
There are 3 difficulties:

- Easy = play area size 5 and 4 ships
- Medium = play area size 7 and 6 ships
- Hard = play area size 9 and 8 ships

Once the difficulty is set, the game boards are generated and the player will be instructed to enter an orientation and start coordinate to place the first ship. <br>
This will repeat until all player ships are placed. There are checks in place to ensure all inputs are valid and no ships are crashing into eachother.<br>
The computers board is created identically to the players board except the parameters are generated using a randomising function. The same checks are in place here too. <br>
Once all the ships are placed, the player will be prompted to guess a location. If the player guesses a location where an enemy ship is located, that location will be marked as a hit and vice-versa for a miss.<br>
After each player guess and check, the computer will pick a random location using the same randomising function from earlier and use the same checks as the player input.<br>
The guessing continues until one players ships are all sank.<br>
The winner is the last one standing.
   
## Features
<hr>

### Existing Features

- __Difficulty Selection__

  - Allows users to easily choose their desired difficulty.
  - Changes the size of the board and the number of ships in play.
  
  <img src="assets/images/readme/start-page-min.PNG">

- __User Input__

  - Multiple points of interaction throughout the game.
  - Allows user to personalise the game with their name.
  - Most fields only requre a single character, making gameplay much faster.
  
  <img src="assets/images/readme/rules-min.PNG">

- __Input Validation__

    - Each input instance is passed through an approprite validation sequence to ensure we send the correct data to the correct place.
    - Certain checks will ask the player to repeat the input until a valid value is passed through.

<img src="assets/images/readme/quiz-page-min.PNG">

- __Automated Opponent__

    - The computer opponent is fully automated and will perform all necesary game tasks without player interference.
    - This adds replayability and will keep users engaged for more than one game.

<img src="assets/images/readme/question-answers-min.PNG">

- __Score Counter__ 

  - The score counter is displayed on screen and will increment by 1 on every correct answer.
  - This allows a winning score to be set and also indicates user performance.

<img src="assets/images/readme/score-min.PNG">

- __Lives Counter__ 

  - The lives counter is displayed on screen and will decrement by 1 on every incorrect answer.
  - The lives are set to 3 by default and will stop the game if the user has lost all 3.

<img src="assets/images/readme/lives-min.PNG">

- __Message and Next Question__

    - This will show the correct conditional message depending on the users answer after they have selected their answer.
    - A button to continue the game is also displayed. Pushing this will advance to the next question.

<img src="assets/images/readme/correct-answer-min.PNG">
<img src="assets/images/readme/wrong-answer-min.PNG">

- __End Game Screen__

    - This appears if either of 2 conditions (game win or game lose) are met and will display the game result to the user.
    - There is also a restart button for the user to press if they would like to start the game again.

<img src="assets/images/readme/you-win-min.PNG">
<img src="assets/images/readme/loser-min.PNG">

### Features left to Implement

    - Difficulty Selection.
    - Selectable Trivia Categories.
    - Multiple Rounds.
    - Username and Scoreboard.

### Technology Used 

    - Github
    - Gitpod
    - HTML 5
    - CSS 3
    - JavaScript

## Testing

<hr>

Manual testing was done through devices I own and included my laptop, phone and tablet. I also tested the website on popular web browsers on my windows laptop. These included Chrome, Firefox, Edge, Opera and Safari.

A Lighthouse test was performed in Chrome dev tools for performance and accessibility.

<img src="assets/images/readme/lighthouse-result-min.PNG">

### Validator Testing

- HTML
  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fharryodubhghaill.github.io%2Fjavascript-essentials-portfolio-project%2F).
- CSS
  - No errors were found when passing through the official [Jigsaw validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fharryodubhghaill.github.io%2Fjavascript-essentials-portfolio-project%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en).
- JavaScript
  - No errors were returned when passing through [JSHint](https://jshint.com/).

## Deployment

<hr>

- The site was deployed to GitHub pages. The steps to deploy are as follows: 
  - In the GitHub repository, navigate to the Settings tab 
  - From the source section drop-down menu, select the Main Branch
  - Once the Main Branch has been selected, the page will be automatically refreshed with a detailed ribbon   display to indicate the successful deployment. 

The live link can be found here - https://harryodubhghaill.github.io/javascript-essentials-portfolio-project/


## Credits 

<hr>

### Code 

- API implimentation info came from Youtube channel ["The Coding Train"](https://www.youtube.com/watch?v=uxf0--uiX0I&t=835s).

### Media

- Questions are from an open source API [Open Trivia Database](https://opentdb.com/).
- Favicon was found here [Favicon](https://www.flaticon.com/free-icons/quiz).
- Fonts were sourced from [Google Fonts](https://fonts.google.com/).
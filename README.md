# Flappy Leo
### Group Members: Amiteash Paul, Aditya Balakrishnan, and Event Sharku

## Project Description
Flappy Leo is a clone of the popular mobile game Flappy Bird inspired by the famous "Paris folded in half" scene from the hit movie *Inception*. The game is a continuous touch game, where a bird has to maneuver itself through the space between columns and try to increase its score. We replaced the bird with Leo, the columns with Parisian-like buildings, and altered the concept, incentives and nature of the game, with additional self-designed accessories. 

## Overall Concept
The movie Inception revolves around Leonardo DiCaprio's character, being a thief who is trying to win time. The movie involves the subversion of dreams and reality, with one of its renowned artistic scenes involving the city of Paris being folded upside down on itself, emulating a staggered series of upside-down and rightside-up columns.

The movie deals with serious themes of loss and time, so we decided to add levity by converting this much-loved movie and incorporating its complex themes into the addictively simple game of Flappy Bird, a mobile sensation in the 2010s. We wanted Leo moving across the skies of Paris, while attempting to cross through 'Paris folding in half' while escaping his demons and chasing his unattainable goals, hence generating an infinite game with score increments. 

## Game Design and Features
While Flappy Bird is created as a mobile game with continuous touch, we replaced the continuous finger touch with that of the spacebar, controlling the degree of levitation of Leo's floating head. 

As Leo flies through the sky, he must attempt to enter the spaces between buildings by changing the height of his flight repeatedly, as the buildings are unevenly sized. There are infinite randomly generated buildings that move to the left through the game screen.

If Leo collides with any of the buildings, he dies and the game ends. If Leo falls to the ground, he crashes and the game ends. Time has won. 

The setting consists of a cloudy night sky with eerie music emulating the themed scene, while the buildings share Paris' architectural theme. There is an option for the music to be muted on the top right of the screen.

In order to add difficulty and capture the characteristic physics experimentation of the movie, the gravity of the game changes after every 5 points scored, i.e. the direction of flight flips. 

## Brainstorming
We wanted to thematize a simple game, and figure out the difficulties of coding seemingly simple gameplay for users. We decided the concept of our version of the game, and then theorized our three main and two sub classes. 
We wanted to have a Player class that moved at a regular speed, and we were able to code a ground object in the game that could detect when Leo touched the surface, and thus end the game. 

We had a difficult time figuring the buildings of the building class, and we decided to use the dimensions of the screen to make buildings start from the top and bottom of the screen while leaving a constant space in between, albeit at different heights. We created a function to generate a number of random buildings and create an additional building infinitely once the function's set number of buildings was exhausted. Whenever a building moved offscreen, it was popped from the list to save memory.

We created a score counter to increment every time Leo successfully passed through the space between the buildings.

We then worked on adding graphics, additional features, and working out technicalities for introductions/end screens/gameplay. 

We finally added our gravity reversal feature, by manipulating the gravity of the game.

## Original Work
We created our own music for the game via Chrome Music Lab, an online simple-to-use synthesizer.

We used our own graphics to create the background and a majority of the graphics of the game, including the clouds, ground, game over screen, buildings, etc. Apart from this, we edited online images to obtain our Leo player character.

We then wanted to add features and difficulty, so we added a mute feature to remove the music in the game, as well as gravity reversal. 

## Implementation Process
We designed three main classes: a Player class, a Game class, and a parent Obstacle class, imitating the physics of collision objects with Ground and Building subclasses.
We added the aforementioned features to these classes, with Amiteash working on the Game class, the Obstacle class, the Player class, and the background music, Aditya working on the Building class, the Game Class and game design, and Event working on the Obstacle class, sounds, graphics, and backgrounds. 

## Reflection
This game was a fundamentally hands-on application of all of the programming concepts we have utilised over the semester.

The project incentivised us to work through the errors, bugs, and logical leaps that occur in coding softwares and our minds, and we had to ensure that every specification was accurate in order to deliver a successful final product.

We hope we paid homage to a game that guided our childhood, by making the addictively simple to play addictively exciting to code. 

Our gratitude is extended to Professor Sana Odeh, our instructor Dena Ahmed, and the various online resources and softwares we utilised to make our final product. 

## Miscellaneous Resources Used

**Processing Reference**: https://processing.org/reference
**p5.js Rference**: https://p5js.org/reference/
**Chrome Music Lab**: https://musiclab.chromeexperiments.com/Song-Maker/

Graphics Creation and Editing done on **Adobe Illustrator** and **Adobe Photoshop**

Code Reference: Super Mario Example Code by Professor Sana Odeh
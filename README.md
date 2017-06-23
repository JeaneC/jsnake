This game is my first solo-project in python.

This program uses Pygame to re-create the classic snake game.
https://www.pygame.org/news

V 0.05 - Program hardly created. Just created a bunch of basic files ( a lot are blank)
- settings.py created
- scoreboard.py created
_ game_stats.py created
- game_functions.py created
- button.py created
- j_snake.py created
- snake.py created

Update V 0.30
- The game is more defined now
- Food does randomly spawn everywhere
- The snake's body has yet to be fixed yet though, and for now only stays as 1 block

Update V 0.40
- Uh... The program kinda got worse...
- Not sure how to make the snake bigger

Update V 0.5
- I found out the mistake!
- Python, unlike the other languages, references objects
- So when I created a new object, I wanted it to have very similar stats to an older one
- So I set it equal to each other, and then I tried to modify the older stats, but
- That really just backfired, since that made Object A become Object B
- The program is starting to come together

Update V 1.0
- Game works as intended for the most part
- Future updates will fix bugs and the interface

Update V 1.0.1
- Nothing important, just comment tweaking

Update v 1.0.5
- A few test runs, some notable bugs
- Bug 1, when it eats something, a random snake block, departs from the group
- Bug 2, even though I put safetey measures to preven this, the snake can collide
- With the piece next to it, and cause you to lose the game
- Bug 1 is probably because the turning point is so small it can be missed

Update V 1.1
- I think the bug is coming straight from my turnPoint class
- A possible fix to this is to create a larger turnPoint collision radius
- I put a fix that didn't fix anything =P
- I can't find the root cause of the problem, but I could probably create a re-alignment method that would
- fix it to the user's eyes
- Oh and I included a video!

Update v 1.2
- I changed the method behind check_turning_point
- But that didn't fix the block randomy detaching from the snake =P
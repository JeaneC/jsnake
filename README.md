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
# Game of Life!

### An implementation of John Conway's "Game of Life" cellular automata, made with Python as a CLI app.
---
In order to run, excecute the game_of_life.py file with Python 3. There's two optional arguments you can pass when doing so: 
* A path to a file storing an initial state for the progam to load.
* The number of iterations or frames per second you want Game of Life to run at.

When no path argument is passed, a randomly renerated 50x50 state will run.
(If you pass both arguments make sure to put them in the order in which they're listed above)

I've included two example _initial state files_: toad_state.txt and gosper_glider_gun.txt. You can see an image of the "Gosper Glider Gun" below. 

An initial state file is just a file containing a matrix 
of 0s and 1s, representing dead and alive cells respectively. So feel free to make your own.

---
### The Gosper Glider Gun
![Gosper glider gun GIF](https://s9.gifyu.com/images/ezgif.com-gif-maker04f188b6a77287de.gif)
![Gosper glider gun](https://i.ibb.co/dPts5WZ/Gosper-Glider-Gun.png)
### A random state (T+0)
![One example state](https://i.ibb.co/qpDX7hv/Game-Of-Life.png)
### ...and the following (T+1)
![Another example state](https://i.ibb.co/tL48yv2/Game-Of-Life2.png)

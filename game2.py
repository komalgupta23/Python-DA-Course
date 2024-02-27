import pgzrun
import random

# to move ypur character
class Hero(Actor):
    def move (self):
        if keyboard.left:
            self.x -= 5
        elif keyboard.right:
            self.x += 5
        elif keyboard.up:
            self.y -= 5
        elif keyboard.down:
            self.y += 5
       

WIDTH = 500
WIDTH = 800

p = Hero('ironman',(100,100))

b = Rect((300, 100), (50, 50))

def draw():
    screen.fill('white')
    p.draw()
    screen.draw.filled_rect(b, 'blue')
def update():
    p.move()

pgzrun.go()

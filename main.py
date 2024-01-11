import tkinter as tk
import random, sys, os

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3

class Snake():
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coords = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coords.append([0,0])

        for x,y in self.coords:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill="white", tag="snake")
            self.squares.append(square)

class Food():
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE

        self.coords = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill="red", tag="food")
    
def next_turn(snake, food):
    x,y = snake.coords[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coords.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill="white")
    snake.squares.insert(0, square)

    if x == food.coords[0] and y == food.coords[1]:
        global score
        score += 1
        label.config(text=f"Score:{score}")
        canvas.delete("food")
        food = Food()
    
    else:
        del snake.coords[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()
    else:
        win.after(SPEED, next_turn, snake, food)

def check_collisions(snake):
    x,y = snake.coords[0]
    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True
    
    for body_part in snake.coords[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

def game_over():
    canvas.delete("all")
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=("consolas", 70), text="GAME OVER", fill="red")
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2 + 100,
                       font=("consolas", 40), text="Press 'R' to restart", fill="white")
   
def onKeyPress(e):
    key = e.keysym
    global direction
    if key == "Left":
        if direction != "right":
            direction = "left"
    elif key == "Right":
        if direction != "left":
            direction = "right"
    elif key == "Up":
        if direction != "down":
            direction = "up"
    elif key == "Down":
        if direction != "up":
            direction = "down"
    elif key == "r":
        os.execl(sys.executable, f'"{sys.executable}"', *sys.argv)
      
win = tk.Tk()
win.title("Snake Game")
win.resizable(False, False)

score = 0
direction = "down"

label = tk.Label(win, text=f"Score:{score}", font=("consolas", 40))
label.pack()

canvas = tk.Canvas(win, width=GAME_WIDTH, height=GAME_HEIGHT, background="black")
canvas.pack()

win.update()

win_width = win.winfo_width()
win_height = win.winfo_height()
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

x = int((screen_width/2) - (win_width/2))
y = int((screen_height/2) - (win_height/2))

win.geometry(f"{win_width}x{win_height}+{x}+{y}")
win.bind("<KeyPress>", onKeyPress)

snake = Snake()
food = Food()

next_turn(snake, food)

win.mainloop()
 
print("Score:", score)








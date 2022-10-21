# a121_catch_a_turtle.py
#-----import statements-----
import turtle
import random
import leaderboard as lb
#-----game configuration----

colors = [
  "yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple",
  "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green",
  "darkgreen", "chocolate", "brown", "black", "gray"
]
shapes = ["circle", "square", "arrow", "classic", "triangle"]
font_setup = ("Arial", 20, "normal")
size = 7.5
shapeindex = 0
shape = "turtle"
timer = 30
counter_interval = 1000
timer_up = False
score = 0
lbname = "leaderboard.txt"
name = input('What is your name? ')
#-----initialize turtle-----

t = turtle.Turtle()
t.shape(shape)
t.shapesize(int(size))
t.fillcolor(random.choice(colors[1:]))
score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(160, 160)
score_writer.pendown()

counter = turtle.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(-160, 160)
counter.pendown()


#-----game functions--------
# manages the leaderboard for top 5 scorers
def manage_leaderboard():

  global score
  global t

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(lbname)
  leader_scores_list = lb.get_scores(lbname)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(lbname, leader_names_list, leader_scores_list, name,
                          score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, t, score)

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, t, score)
  t.hideturtle()


# countdown function
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    t.hideturtle()
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)


# update and display the score
def updateScore():
  global score
  score = score + 1
  score_writer.clear()
  score_writer.write(score, font=font_setup)


def resize():
  global size
  global shapeindex
  size = size - .2
  t.shapesize(size)


def spotClicked(x, y):
  changePosition()
  updateScore()


def changeColor():

  t.fillcolor(random.choice(colors[1:]))


def changePosition():

  new_xpos = random.randint(-200, 200)
  new_ypos = random.randint(-150, 150)
  t.hideturtle()
  changeColor()
  resize()
  t.penup()
  t.goto(new_xpos, new_ypos)
  t.pendown()
  t.showturtle()


def start_game():
  t.onclick(spotClicked)
  counter.getscreen().ontimer(countdown, counter_interval)


#----------events----------
start_game()

wn = turtle.Screen()
wn.screensize()
wn.setup(width=1.0, height=1.0)
wn.mainloop()

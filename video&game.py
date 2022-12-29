# Description: This is a simple video game that I created using Python and the Turtle module.
# The game is called Space Invaders2998. The player is a blue triangle and the enemies are red circles.
# The player can move left and right using the left and right arrow keys. The player can shoot bullets
# using the space bar. The enemies move down the screen and the player must shoot them before they reach
# the bottom of the screen. The player's score is displayed in the top left corner of the screen. The game
# ends when the player's score reaches 100 or when the player is hit by an enemy.
#that is the idea of the game and just have a few problems with the code
#the first problem is that the enemies are not moving down the screen
#the second problem is that the bullets are not shooting
#the third problem is that the game is not ending when the player's score reaches 100 or when the player is hit by an enemy
#somoone please help me with this code and contribute to it. thank you


import os                 # for os.path
import random            # for random.choice
import time              # for time.sleep
import math               # for math.sqrt
import turtle            # for turtle graphics

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("skyblue")            # background color of the screen
wn.title("Space Invaders")         # title of the screen

# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)        # set the position of the turtle
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):            # draw a square
    border_pen.fd(600)
    border_pen.lt(90)          # turn left 90 degrees
border_pen.hideturtle()          # hide the turtle

# Set the score to 0
score = 0

# Draw the score on the screen
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")   # color of the text
score_pen.penup()
score_pen.setposition(-290, 310)
scorestring = "Score: %s" %score      # %s is a placeholder for the score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()


# Create the player turtle
player = turtle.Turtle()      # create a turtle object
player.color("blue")            # color of the player
player.shape("triangle")        # shape of the player
player.penup()
player.speed(0)         # speed of the player
player.setposition(0, -250)    # position of the player
player.setheading(90)

playerspeed = 15                   # speed of the player

# Choose a number of enemies
number_of_enemies = 7
# Create an empty list of enemies
enemies = []

# Add enemies to the list
for i in range(number_of_enemies):
    # Create the enemy
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

enemyspeed = 2

# Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

# Define bullet state

# ready - ready to fire

# fire - bullet is firing

bulletstate = "ready"

# Move the player left and right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():

    # Declare bulletstate as a global if it needs changed
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        # Move the bullet to just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

# Create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

# Main game loop
while True:
        for enemy in enemies:
            # Move the enemy
            x = enemy.xcor()
            x += enemyspeed
            enemy.setx(x)
    
            # Move the enemy back and down
            if enemy.xcor() > 280:
                # Move all enemies down
                for e in enemies:
                    y = e.ycor()
                    y -= 40
                    e.sety(y)
                # Change enemy direction
                enemyspeed *= -1
    
            if enemy.xcor() < -280:
                # Move all enemies down
                for e in enemies:
                    y = e.ycor()
                    y -= 40
                    e.sety(y)
                # Change enemy direction
                enemyspeed *= -1
    
            # Check for a collision between the bullet and the enemy
            if isCollision(bullet, enemy):
                # Reset the bullet
                bullet.hideturtle()
                bulletstate = "ready"
                bullet.setposition(0, -400)
                # Reset the enemy
                x = random.randint(-200, 200)
                y = random.randint(100, 250)
                enemy.setposition(x, y)
                # Update the score
                score += 10
                scorestring = "Score: %s" %score
                score_pen.clear()
                score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
    
            if isCollision(player, enemy):
                player.hideturtle()
                enemy.hideturtle()
                print("Game Over")
                break
    
        # Move the bullet
        if bulletstate == "fire":
            y = bullet.ycor()
            y += bulletspeed
            bullet.sety(y)
    
        # Check to see if the bullet has gone to the top
        if bullet.ycor() > 275:
            bullet.hideturtle()
            bulletstate = "ready"
        for enemy in enemies:
            # Move the enemy
            x = enemy.xcor()
            x += enemyspeed
            enemy.setx(x)
    
            # Move the enemy back and down
            if enemy.xcor() > 280:
                # Move all enemies down
                for e in enemies:
                    y = e.ycor()
                    y -= 40
                    e.sety(y)
                # Change enemy direction
                enemyspeed *= -1
    
            if enemy.xcor() < -280:
                # Move all enemies down
                for e in enemies:
                    y = e.ycor()
                    y -= 40
                    e.sety(y)
                # Change enemy direction
                enemyspeed *= -1
    
            # Check for a collision between the bullet and the enemy
            if isCollision(bullet, enemy):
                # Reset the bullet
                bullet.hideturtle()
                bulletstate = "ready"
                bullet.setposition(0, -400)
                # Reset the enemy
                x = random.randint(-200, 200)
                y = random.randint(100, 250)
                enemy.setposition(x, y)
                # Update the score
                score += 10
                scorestring = "Score: %s" %score
                score_pen.clear()
                score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
    
            if isCollision(player, enemy):
                player.hideturtle()
                enemy.hideturtle()
                print("Game Over")
                break
    
        # Move the bullet
        if bulletstate == "fire":
            y = bullet.ycor()
            y += bulletspeed
            bullet.sety(y)
    
        # Check to see if the bullet has gone to the top
        if bullet.ycor() > 275:
            bullet.hideturtle()
            bulletstate = "ready"
# Move the enemy
        for enemy in enemies:
            x = enemy.xcor()
            x += enemyspeed
            enemy.setx(x)

            # Move the enemy back and down
            if enemy.xcor() > 280:
                # Move all enemies down
                for e in enemies:
                    y = e.ycor()
                    y -= 40
                    e.sety(y)
                # Change enemy direction
                enemyspeed *= -1

            if enemy.xcor() < -280:
                # Move all enemies down
                for e in enemies:
                    y = e.ycor()
                    y -= 40
                    e.sety(y)
                # Change enemy direction
                enemyspeed *= -1
            else :
                print("Game Over")
                break

            # Check for a collision between the bullet and the enemy
            if isCollision(bullet, enemy):
                # Reset the bullet
                bullet.hideturtle()
                bulletstate = "ready"
                bullet.setposition(0, -400)
                # Reset the enemy
                x = random.randint(-200, 200)
                y = random.randint(100, 250)
                enemy.setposition(x, y)
                # Update the score
                score += 10
                scorestring = "Score: %s" %score
                score_pen.clear()
                score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

            if isCollision(player, enemy): # collision
                player.hideturtle()
                enemy.hideturtle()
                print("Game Over")
                break


        # Move the bullet
        if bulletstate == "fire":
            y = bullet.ycor()
            y += bulletspeed
            bullet.sety(y)

        # Check to see if the bullet has gone to the top
        if bullet.ycor() > 275:
            bullet.hideturtle()
            bulletstate = "ready"

        wn.mainloop()

        if score == 100:
            print("You win")
            break
        else:
            print("Game Over")
            break
    
# collision
def isCollision(t1, t2):
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if d < 20:
        return True
    else:
        return False

# Keyboard bindings
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(fire_bullet, "space")

# Main game loop
while True:
    for  enemy in enemies:
        # Move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        # Move the enemy back and down
        if enemy.xcor() > 280:
            # Move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            # Change enemy direction
            enemyspeed *= -1

        if enemy.xcor() < -280:
            # Move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            # Change enemy direction
            enemyspeed *= -1

        # Check for a collision between the bullet and the enemy
        if isCollision(bullet, enemy):
            # Reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            # Reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            # Update the score
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

# missile collision
            missile = turtle.Turtle()
            missilestate = "ready"
            missile.setposition(0, -400)
            missile.hideturtle()
            missilestate = "ready"
            missile.setposition(0, -400)
            # Reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            # Update the score
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

        # Check for a collision between the missile and the enemy

        if isCollision(missile, enemy):
            # Reset the missile
            missile.hideturtle()
            missilestate = "ready"
            missile.setposition(0, -400)
            # Reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            # Update the score
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

            missile.move()    # Move the missile
            missilestate = "fire"   # Change the missile state
            x = player.xcor()
            y = player.ycor() + 10
            missile.setposition(x, y)
            missile.showturtle()












     








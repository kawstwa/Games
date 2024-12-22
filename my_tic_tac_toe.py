import turtle

sc = turtle.Screen()
turtle.setworldcoordinates(-10,-10,10,10)
turtle.bgcolor('yellow')
turtle.title('TIC TAC TOE')
turtle.hideturtle()
turtle.tracer(0)
turtle.pensize(20)
turtle.penup()
moves = 9
crosses = []
circles = []
game = True
winner = False

def line(heading):
    turtle.seth(heading)
    turtle.pendown()
    turtle.fd(18)
    turtle.penup()
    
def draw_board():
    turtle.goto(-9,3)
    line(0)
    turtle.goto(-9,-3)
    line(0)
    turtle.goto(-3,9)
    line(270)
    turtle.goto(3,9)
    line(270)

def score(text):
    turtle.goto(-7, -2)
    turtle.color('red')
    turtle.write(text, font=('Arial', 90, 'bold'))

def draw_cross(x,y):
    turtle.color('blue')
    turtle.goto(x,y)
    turtle.pendown()
    turtle.goto(x+4,y-4)
    turtle.penup()
    turtle.goto(x+4,y)
    turtle.pendown()
    turtle.goto(x,y-4)
    turtle.penup()

def draw_circle(x,y):
    turtle.goto(x,y-2)
    turtle.color('green')
    turtle.pendown()
    turtle.circle(2,steps=100)
    turtle.penup()

def check_winner(func, text, x,y):
    global moves, winner, game
    moves-=1
    func.append((x,y))
    x_values=[]
    y_values = []
    for item in func:
        x_values.append(item[0])
        y_values.append(item[1])
    if x_values.count(max(x_values, key=x_values.count)) == 3 or y_values.count(max(y_values, key=y_values.count)) == 3: winner = True

    diag_1 = [(-8, 8),(-2, 2),(4, -4)]
    diag_2 = [(4, 8),(-2, 2),(-8, -4)]
    if diag_1[0] in func and diag_1[1] in func and diag_1[2] in func: winner = True
    if diag_2[0] in func and diag_2[1] in func and diag_2[2] in func: winner = True
      
    if winner:        
            score(text)
            game=False

def draw(x,y):
    global moves, winner
    if moves % 2 == 0:
        draw_circle(x,y)
        check_winner(circles, "O WINS!",x,y)
    else:
        draw_cross(x,y)
        check_winner(crosses, 'X WINS!',x,y)
    if moves ==0 and not winner:
        text = "Its a TIE"
        score(text)

def play(x,y):
    global moves
    if moves > 0:
        if -9 < x < -3: x = -8
        elif -3 < x < 3: x = -2
        elif 3 < x < 9: x= 4
        if 9 > y > 3: y = 8
        elif 3 > y > -3: y = 2
        elif -3 > y > -9: y=-4
        if (x,y) not in crosses or (x,y) not in circles: draw(x,y)
        else: return
            
draw_board()

if game:
    turtle.onscreenclick(play)

turtle.mainloop()
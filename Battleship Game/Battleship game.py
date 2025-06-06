from flask import *
from random import *

#main program

##board = [["O" for i in range(6)] for i in range(5)]
##board[0] = None
##
##for i in range(1,len(board)):
##    board[i][0] = None
##x = randint(1,5)
##y = randint(1,4)
##board[y][x] = "S"
##for i in board[1:]:
##    if i == None:
##        print(i)
##    else:
##        
##        print(" ".join(i[1:]))

app = Flask(__name__)
@app.route("/")

def home():
    global board,x,y
    board = [["O" for i in range(6)] for i in range(5)]
    board[0] = None

    for i in range(1,len(board)):
        board[i][0] = None
    x = randint(1,4)#row
    y = randint(1,5)#column
    return render_template("Battleship.html")

@app.route("/shoot", methods = ["POST"])

def shoot():
    global board,x,y

    data = request.form
    x_coord = int(data["x"])
    y_coord = int(data["y"])
    if x_coord == x and y_coord == y:
        return render_template("winner.html")
    else:
        board[x_coord][y_coord] = "X"
        return render_template("continuation.html",board = board)
    
if __name__ == "__main__":
    app.run(port = 5010, debug = True)



 

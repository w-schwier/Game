import random
import tkinter

playerXPos = 0 
playerYPos = 0

def getIntInput(prompt, accepted):
    while True:
        value = input(prompt).lower()
        intValue = int(value)
        if intValue in accepted:
            return intValue
        else:
            print(value)
            print("Try again numbnuts, may i suggest one of...", accepted)

class game:
    "main game class"

    roomList = []
    numbPlayers = getIntInput("How many people are playing (Must be between 3 - 6)? ", [3, 4, 5, 6])
   

class room:
    "class containing room data"

    

    def __init__(self, xPos, yPos, floor, nDoor, sDoor, eDoor, wDoor, basement, ground, upper, event, omen, item): 
        self.xPos = xPos
        self.yPos = yPos
        self.floor = floor
        self.nDoor = nDoor
        self.sDoor = sDoor
        self.eDoor = eDoor
        self.wDoor = wDoor
        self.basement = basement
        self.ground = ground
        self.upper = upper
        self.event = event
        self.omen = omen
        self.item = item 

    def getRoom():
        count = 0
        while count <= len(game.roomList):
            if playerXPos == game.roomList[count].xPos:
                if playerYPos == game.roomList[count].yPos:
                    return count     
            count += 1

    def roomInfo(count):
        if game.roomList[count].nDoor == "true":
            print ("There is a door to the north")
        if game.roomList[count].sDoor == "true":
            print ("There is a door to the south")
        if game.roomList[count].eDoor == "true":
            print ("There is a door to the east")
        if game.roomList[count].wDoor == "true":
            print ("There is a door to the west")

        

    

    def doorCheck(direction):
        if direction == "north":
            if self.nDoor == "true":
                return "true"
        if direction == "south":
            if self.sDoor == "true":
                return "true"
        if direction == "east":
            if self.eDoor == "true":
                return "true"
        if direction == "west":
            if self.wDoor == "true":
                return true
        return "false"

            

class card:
    "class containing card data and methods"

    def __init__(self, cardType, text):
        balls = 1



entranceHall = room(0, 0, 1, "true", "false", "true", "true", "false", "true", "true", "false", "false", "false")

game.roomList.append(entranceHall)

foyer = room(0, 1, 1, "true", "true", "true", "true", "false", "true", "false", "false", "false", "false")

game.roomList.append(foyer) 

grandStaircase = room(0, 2, 1, "false", "true", "false", "false", "false", "true", "false", "false", "false", "false")

game.roomList.append(grandStaircase)

def getInput(prompt, rejectedText, accecpted):
    while 1:
        inputValue = input(prompt)
        if inputValue in accecpted:
            return inputValue
        print(rejectedText)
    

def move():
    print("You are in room", playerXPos, ",", playerYPos)
    room.roomInfo(room.getRoom())
    direction = getInput("Which door do you take? ", "That's not a compass point and you know it!", ["north", "south", "east", "west"])
    print(direction)
    while room.doorCheck(direction) == "false":
        print("You walk straight into a wall, well done spaz") 
    if direction == "north":
        print("yes")
        global playerYPos
        playerYPos += 1
    print("you are in room", playerXPos, ",", playerYPos)
    
print("balls")
move()
#top = tkinter.Tk() 
#c = tkinter.Canvas(top, bg = "blue", height=480, width=640, cursor = "dot")        
#coord = 10, 50, 240, 210
#balls = c.create_oval(100, 50, 240, 210, fill="red")
#c.pack()
#balls2 = c.create_oval(200, 300, 100, 50, fill ="orange")
#c.update()
#extra tits 

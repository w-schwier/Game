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

    

    def __init__(self, roomName, xPos, yPos, floor, nDoor, sDoor, eDoor, wDoor, basement, ground, upper, event, omen, item, comments): 
        self.roomName = roomName
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
        self.comments = comments

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
                return "true"
        

            

class card:
    "class containing card data and methods"

    def __init__(self, cardType, text):
        balls = 1



entranceHall = room("Entrance Hall", 0, 0, 1, "true", "false", "true", "true", "false", "true", "true", "false", "false", "false", "")

game.roomList.append(entranceHall)

foyer = room("Foyer", 0, 1, 1, "true", "true", "true", "true", "false", "true", "false", "false", "false", "false", "")

game.roomList.append(foyer) 

grandStaircase = room("Grand Staircase", 0, 2, 1, "false", "true", "false", "false", "false", "true", "false", "false", "false", "false", "")

game.roomList.append(grandStaircase)

bedroom = room("Bedroom", 9, 9, 9, "false", "false", "true", "true", "false", "false",  "true", "true", "false", "false", "")
tower = room("Tower", 9, 9, 9, "false", "false", "true", "true", "false", "false",  "true", "true", "false", "false", "You can attempt a Might roll of 3+ to cross. If you fail you stop moving")
conservatory = room("Conservatory", 9, 9, 9, "true", "false", "false", "false", "false", "true",  "true", "true", "false", "false", "")
researchLaboratory = room("Research Laboratory", 9, 9, 9, "true", "true", "false", "false", "true", "false",  "true", "true", "false", "false", "")
ballroom = room("Ballroom", 9, 9, 9, "true", "true", "true", "true", "false", "true",  "false", "true", "false", "false", "")
patio = room("Patio", 9, 9, 9, "true", "true", "false", "true", "false", "true",  "false", "true", "false", "false", "")
gardens = room("Gardens", 9, 9, 9, "true", "true", "false", "false", "false", "true",  "false", "true", "false", "false", "")
creakyHallway = room("Creaky Hallway", 9, 9, 9, "true", "true", "true", "true", "true", "true",  "true", "false", "false", "false", "")
undergroundLake = room("Underground Lake", 9, 9, 9, "true", "false", "true", "false", "true", "false",  "false", "true", "false", "false", "")
organRoom = room("Organ Room", 9, 9, 9, "false", "true", "false", "true", "true", "true",  "true", "true", "false", "false", "")
dustyHallway = room("Dusty Hallway", 9, 9, 9, "true", "true", "true", "true", "true", "true",  "true", "false", "false", "false", "")
gameRoom = room("Game Room", 9, 9, 9, "true", "true", "true", "false", "true", "true", "true", "true", "false", "false", "")
statuaryCorridor = room("Statuary Corridor", 9, 9, 9, "true", "true", "false", "false", "true", "true", "true", "true", "false", "false", "")
chapel = room("Chapel", 9, 9, 9, "true", "false", "false", "false", "flase", "true", "true", "true", "false", "false", "Once per game, if you end your turn here, gain 1 sanity.")
crypt = room("Crypt", 9, 9, 9, "true", "false", "false", "false", "true", "false", "false", "true", "false", "false", "If you end your turn here, take 1 point of mental damage")
attic = room("Attic", 9, 9, 9, "false", "true", "false", "false", "false", "false", "true", "true", "false", "false", "When exiting, you must attempt a Speed roll of 3+. If you fail, lose 1 Might (but continue moving).")
operatingLaboratory = room("Operating Laboratory", 9, 9, 9, "false", "true", "true", "false", "true", "false", "true", "true", "false", "false", "")
library = room("Library", 9, 9, 9, "false", "true", "false", "true", "false", "true", "true", "true", "false", "false", "Once per game, if you end your turn here, gain 1 Knowledge.")
graveyard = room("Graveyard", 9, 9, 9, "false", "true", "false", "false", "false", "true", "false", "true", "false", "false", "When exiting, you must attempt a Sanity roll of 4+. If you fail, lose 1 Knowledge (but keep moving).")


def getInput(prompt, rejectedText, accecpted):
    while 1:
        inputValue = input(prompt)
        if inputValue in accecpted:
            return inputValue
        print(rejectedText)
    

def move():
    print("You are in room ", "(", playerXPos, ",", playerYPos, ")")
    # put in print(room.roomName) or some such shit
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
    

move()
#top = tkinter.Tk() 
#c = tkinter.Canvas(top, bg = "blue", height=480, width=640, cursor = "dot")        
#coord = 10, 50, 240, 210
#balls = c.create_oval(100, 50, 240, 210, fill="red")
#c.pack()
#balls2 = c.create_oval(200, 300, 100, 50, fill ="orange")
#c.update()

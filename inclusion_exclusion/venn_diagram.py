# A script for visualising venn diagrams with n sets, using turtle
import turtle

NUM_SETS = 6 # number of sets to form the venn diagram with

turtle.title("Venn Diagram")

s = turtle.getscreen()
t = turtle.Turtle()

t.penup()
t.rt(90)
t.fd(300)
t.lt(90)
t.pendown()

# n = int(input("How many sets are there?"))

def drawEllipse(rad, mult=1):
     
  # rad --> radius of arc
    for _ in range(2):
        # two arcs
        t.circle(rad//2*mult,90)
        t.circle(rad*mult,90)

def getShape(numSets):
    #Calculate how many groups need to be formed to create venn diagram
    numGroups = 2**numSets

    numSides = 2
    
    while((numSides)*(numSets**2) - (numSides)*numSets + 2 < numGroups):
        numSides += 1

    drawShape(numSides)

def drawShape(numSides):

    t.circle(400/numSides,180/numSides)
    for i in range(numSides):
        t.fd(300/(numSides**(0.5)))
        if(i != numSides-1):
          t.circle(400/numSides,360/numSides)
    t.circle(400/numSides,180/numSides)

# Function to learn turtle. Drawing a smiley face
def drawSmileyFace():
    t.speed(10)
    t.circle(300)

    t.penup()
    t.lt(135)
    t.fd(200)
    t.rt(180)
    t.pendown()
    t.circle(200, 90)

    t.penup()
    t.home()

    t.fd(70)
    t.lt(90)
    t.fd(60)
    t.rt(135)
    t.pendown()

    drawEllipse(50)

    t.penup()
    t.home()

    t.lt(180)
    t.fd(70)
    t.rt(90)
    t.fd(60)
    t.lt(135)
    t.pendown()

    drawEllipse(50, -1)




# drawSmileyFace()

#Draw shape that could form an n-set venn diagram
getShape(NUM_SETS)


turtle.exitonclick()
################################################################################################
# Name: Adam Stafford
# Date: 2024-04-15
# Description: Implements a 2D point class and a coordinate system on which to plot points (v2).
################################################################################################
from tkinter import *
from random import randint, choice, sample
from math import sqrt

# the 2D point class
class Point:
    # the constructor
    def __init__(self, x=0.0, y=0.0):
        # initialize components with default (0.0,0.0)
        self._x = float(x)
        self._y = float(y)

    # accessors and mutators
    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    def get_y(self):
        return self._y

    def set_y(self, value):
        self._y = value

    x = property(get_x, set_x)
    y = property(get_y, set_y)

    # calculates and returns the distance between two points
    def dist(self, other):
        return sqrt((self._x - other._x) ** 2 + (self._y - other._y) ** 2)

    # calculates and returns the midpoint between two points
    def midpt(self, other):
        return Point((self._x + other._x) / 2.0, (self._y + other._y) / 2.0)

    # returns a string representation of the point: (x,y)
    def __str__(self):
        return f"({self._x},{self._y})"

# the coordinate system class: (0,0) is in the top-left corner
# inherits from the Canvas class of Tkinter
class ChaosGame(Canvas):
    # class variables
    # the default point radius is 0 pixels (i.e., no center to the oval)
    MIDPOINT_RADIUS = 1
    
    VERTEX_RADIUS = 3
    # colors to choose from when plotting points
    COLORS = [ "black", "red"]
    # the constructor
    def __init__(self, parent):
        # call the constructor in the superclass
        Canvas.__init__(self, parent, bg="lightblue")
        # organize the canvas
        self.pack(fill=BOTH, expand=1)

    # plots a specified number of points
    #three vertices plotted, one top middle, one bottom left, one bottom right
    def plotPoints(self, n):
        v1 = Point(WIDTH // 2, 2)
        v2 = Point(1, HEIGHT - 9)
        v3 = Point(WIDTH - 9, HEIGHT - 9)
        #put points into list so program can manipulate it
        vertices = [v1, v2, v3]

        #instead of having three different lines, cirumvented by just putting it in a loop.
        for vertex in vertices:
            self.plot(vertex, "red", ChaosGame.VERTEX_RADIUS)
            
        #code for making sure the first point plotted from the 2 of the 3 vertices is plotted randomly.
        initial_vertice_plot = sample(vertices, 2)
        #caluclated midpoint will take two random vertice points from sample method and call midpoint function on them.
        calculated_midpoint = initial_vertice_plot[0].midpt(initial_vertice_plot[1])
        #after midpoint value is found, will utilize self.plot function to paste onto GUI
        self.plot(calculated_midpoint, "black", ChaosGame.MIDPOINT_RADIUS)
        
        #loop which will plot midpoints until 50000 have been plotted
        for i in range(n):
            #v (vertices) will look at vertice list and choose one of the three at random,
            #but making sure its only taking one (CHATGPT fixed my original error by placing the [0] into my function).
            v = sample(vertices, 1)[0]
            #same as the previous midpoint calculation a few lines above, called the midpt calculation functiin.
            calculated_midpoint = calculated_midpoint.midpt(v)
            #calling the plot method to plot the calculated midpoint 
            self.plot(calculated_midpoint, "black", ChaosGame.MIDPOINT_RADIUS)

    # plot a single point in the color specified
    #added an additional argument "radius"
    def plot(self, point, color, radius):
        #removed the point_radius and replaced with radius argument. Noticed that I could never see the red dots the original way.
        self.create_oval(point.x - radius, point.y - radius, point.x + radius, point.y + radius, outline=color, fill=color)

###########################################
# the default size of the canvas is 800x800
WIDTH = 600
HEIGHT = 520
# the number of points to plot
NUM_POINTS = 50000

# create the window
window = Tk()
window.geometry(f"{WIDTH}x{HEIGHT}")
window.title("The Chaos Game")
# create the coordinate system as a Tkinter canvas inside the window
s = ChaosGame(window)
# plot some random points
s.plotPoints(NUM_POINTS)
# wait for the window to close
window.mainloop()


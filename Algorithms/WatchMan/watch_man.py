import math
import sys
import pygame
import eztext

SCREEN_HEIGHT = 512
SCREEN_WIDTH = 1250
WHITE = (255,255,255)
ORANGE = (253,131,32)
GREEN = (158,226,45)
PINK = (249,39,114)
PURPLE = (171, 129, 255)
RED = (201,9,9)
LIGHTBLUE = (0,255,255)
SLATE = (39,40,34)

X_DRAWING_OFFSET = SCREEN_WIDTH/2

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#a class for points
class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
	def draw(self,surface, color):
		pygame.draw.circle(surface, color,(self.x+X_DRAWING_OFFSET,SCREEN_HEIGHT-self.y),5)
		


#class for points with values
class vPoint(Point):
	def __init__(self,x,y, value):
		Point.__init__(self,x,y)
		self.value = value
		self.vision = []
	

#lineSegment class to hold two points
class lineSegment:
	def __init__(self, point1, point2, color):
		self.point1 = point1
		self.point2 = point2
		self.used = False
		self.color = color



	def draw(self,surface, color, width):
		pygame.draw.line(surface, color, (self.point1.x+X_DRAWING_OFFSET,SCREEN_HEIGHT-self.point1.y), (self.point2.x+X_DRAWING_OFFSET,SCREEN_HEIGHT-self.point2.y), width)

#arch segment class to hold three points on a circle
class arcSegment(lineSegment):
	def __init__(self, point1, point2, dx, dy):
		lineSegment.__init__(self,point1,point2)
		self.dx = dx
		self.dy = dy

def determine_intersection(segment1, segment2):

	#returns true if an intersection on the interval is found
	#returns false in there is no such intersection

	#local variables to hold values of segments
	X1, Y1 = segment1.point1.x, segment1.point1.y
	X2, Y2 = segment1.point2.x, segment1.point2.y
	X3, Y3 = segment2.point1.x, segment2.point1.y
	X4, Y4 = segment2.point2.x, segment2.point2.y

	#If the the X interval of the first segment does not crossover the Xinterval of the second segment then there is no mutual intersection
	if max(X1, X2) < min(X3, X4) or max(X3,X4) < min(X1,X2) or max(Y3,Y4) < min(Y1,Y2) or  max(Y1,Y2) < min(Y3,Y4):
		print "no mutual interval"
		return False  

	#interval2 of possible intersection on the x axis
	xInterval1 = [ max(min(X1,X2),min(X3,X4)), min(max(X1,X2),max(X3, X4)) ]
	xInterval2 = [ max(min(X3,X4),min(X1,X2)), min(max(X3,X4),max(X1, X2)) ]

	#interval of possible intersection on the y axis
	yInterval1 = [ max(min(Y1,Y2),min(Y3,Y4)), min(max(Y1,Y2),max(Y3, Y4)) ]
	yInterval2 = [ max(min(Y3,Y4),min(Y1,Y2)), min(max(Y3,Y4),max(Y1, Y2)) ]

	#find the slope of the two line segments
	#we need to be careful not to divide by 0
	denom1 = float(X2-X1)
	denom2 = float(X4-X3)
	if(denom1 == 0 or denom2 == 0):
		if(denom1 == denom2):
			print "equal zero denominators"
			return False #parallel vertical lines
		elif max(Y1,Y2) < min(Y3,Y4) or max(Y3,Y4) < min(Y1,Y2):
			print "no overlaping yInterval"
			return False
		elif denom1 == 0:
			slope = (Y4-Y3)/denom2
			yIntercept = Y3 - slope*X3
			Yi = slope*X1+yIntercept
			if((Yi < yInterval1[0]) or (Yi > yInterval1[1]) or (Yi < yInterval2[0]) or (Yi > yInterval2[1])):
				return False 	#no intersection
		elif denom2 == 0:
			slope = (Y2-Y1)/denom1
			yIntercept = Y1 - slope*X1
			Yi = slope*X3+yIntercept
			if((Yi < yInterval1[0]) or (Yi > yInterval1[1]) or (Yi < yInterval2[0]) or (Yi > yInterval2[1])):
				return False 	#no intersection
		else:
			return True #the vertical line intersects the 


	#calculate the slope
	M1 = (Y2-Y1)/denom1
	M2 = (Y4-Y3)/denom2

	#if the two slopes are horizantal then the line segments are parallel
	if M1 == M2:
		print "equal slopes"
		return False
	
	#find the Y-intercepts(b1 and b2), the points used don't matter so long as its one from each line segment
	b1 = Y1 - M1*X1 
	b2 = Y3 - M2*X3



	#using algrebra we can find the x coordinate where the two lines intersect
	Xi = (b2 - b1)/(M1 - M2)


	#now we just need to check that the x coordinate of intersection is on our interval
	if((Xi < xInterval1[0]) or (Xi > xInterval1[1]) or (Xi < xInterval2[0]) or (Xi > xInterval2[1])):
		print "intersection out of bounds"
		return False #the intersection is outside the interval 
	else:
		print "intersects"
		return True


def find_guard_vision(valueList):
	screen.fill((39,40,34))
	#some local varibles
	numWalls, numArt, numGuards, numVertices = 0,0,0,0
	points = []
	arts = []
	guards = []
	walls = []
	acceptableLines = []

	#convert values
	if len(valueList[0].value): numWalls = int(valueList[0].value)
	#if len(valueList[1].value): numArt = int(valueList[1].value)
	#if len(valueList[2].value): numGuards = int(valueList[2].value)
	#if len(valueList[3].value): numVertices = int(valueList[3].value)
	inputPoints = valueList[4].value.split(';')
	inputArts = valueList[5].value.split(';')
	inputGuards = valueList[6].value.split(';')

	#convert values and place in lists
	for p in inputPoints: 
		if(len(p)):
			p = p.split(',')
			x = 2*int(p[0])
			y = 2*int(p[1])
			points.append(Point(x,y))

	#split the values into a list of Point objects
	for art in inputArts:
		if(len(art)):
			art = art.split(',')
			arts.append(vPoint(2*int(art[0]),2*int(art[1]), int(art[2])))

	#split the values into a list of Point objects
	for guard in inputGuards:
		if(len(art)):
			guard = guard.split(',')
			guards.append(vPoint(2*int(guard[0]),2*int(guard[1]), int(guard[2])))

	#list of walls
	for i in range(numWalls):
		if i == numWalls-1:
			walls.append(lineSegment(points[i], points[0], PURPLE))

		else: walls.append(lineSegment(points[i], points[i+1], PURPLE))

	#for every guard create a temporary line segment and then check if that line segment intersects any walls
	for guard in guards:
		for art in arts:
			tempLine = lineSegment(guard, art, ORANGE) 
			intersects = False
			for wall in walls:
				if(determine_intersection(wall, tempLine)):
					print wall.point1.x,wall.point1.y,wall.point2.x,wall.point2.y
					intersects = True

			#if the line segment intersects a wall then do not include it into the vision list of the point
			if (not intersects):
				guard.vision.append(art)
				art.vision.append(guard)
				acceptableLines.append(tempLine)
				print acceptableLines




			
			#print art.vision
			#print guard.vision
	#now all guards should have a list of arts it can "see"
	#and all arts should have a list of guards it can "see"

	print arts
	for art in arts:
		print art.vision
	
	if not determine_suitability(acceptableLines,arts):

		button2 = eztext.Button(caption = "That doesn't work! :(", pos = (800,400), boxColor = RED,length = 200, width = 24)
		button2.draw(screen)

	else:
		button2 = eztext.Button(caption = "Nice work! :)", pos = (800,400), boxColor = GREEN, length = 200, width = 24)
		button2.draw(screen)


	#all of this just draws



	for point in points:
		point.draw(screen,PURPLE)

	for art in arts:
		art.draw(screen, PINK)

	for guard in guards:
		guard.draw(screen, GREEN)

	for line in acceptableLines:
		line.draw(screen, line.color, 3)

	for wall in walls:
		wall.draw(screen, wall.color, 3)
	
	#print len(points), len(arts), len(guards)


def determine_suitability(edgeList, arts):
	#edge.point1 = guard 
	#edge.point2 = art

	#the time complexity of this algorithm is ridculous
	# O(edge!)
	allZero = True
	for art in arts:
		if art.value != 0:
			allZero = False

	if allZero: return True 	#if all the arts are guarded then the solution is found

	#generate every possibility
	for edge in edgeList:
		if not edge.used:
			if edge.point1.value > 0 and edge.point2.value > 0:
				edge.used = True
				edge.color = LIGHTBLUE
				edge.point1.value -= 1
				edge.point2.value -= 1
				if determine_suitability(edgeList,arts): 
					print "True"
					return True
				edge.used = False
				edge.color = ORANGE
				edge.point1.value += 1
				edge.point2.value += 1
	#if the control gets to this point then there is no solution
	print False
	return False
	

def main():

	#python initializing
	textSurface = pygame.Surface((X_DRAWING_OFFSET-10,SCREEN_HEIGHT))

	pygame.display.set_caption("Watch, Man!")
	clock = pygame.time.Clock()
	#fill the screen pretty
	screen.fill((39,40,34))
	#make the text input boxes
	textBoxList = []
	textBoxList.append(eztext.Input(x = 9, y = 24, maxlength = 2, color = WHITE, prompt = 'Walls?', length = 100, width = 24 ,restricted = '0123456789'))
	textBoxList.append(eztext.Input(x =	118, y = 24, maxlength = 2, color = WHITE, prompt = 'Art?', length = 100, width= 24, restricted = '0123456789'))
	textBoxList.append(eztext.Input(x = 248, y = 24, maxlength = 2, color = WHITE, prompt = 'Guards?', length = 100, width= 24, restricted = '0123456789'))
	textBoxList.append(eztext.Input(x = 9, y = 80, maxlength = 2, color = WHITE, prompt = '# of Vertices', length =100 , width= 24, restricted = '0123456789'))
	textBoxList.append(eztext.Input(x = 9, y = 132, maxlength = 100, color = WHITE, prompt = 'Coordinates of Vertices', length = X_DRAWING_OFFSET-25 , width= 24, restricted = '0123456789,();'))
	textBoxList.append(eztext.Input(x = 9, y = 184, maxlength = 100, color = WHITE, prompt = 'Coordinates of Art', length = X_DRAWING_OFFSET-25 , width= 24, restricted = '0123456789,();'))
	textBoxList.append(eztext.Input(x = 9, y = 236, maxlength = 100, color = WHITE, prompt = 'Coordinates of Guards', length = X_DRAWING_OFFSET-25 , width= 24, restricted = '0123456789,();'))
	button = eztext.Button(caption = "GO!", pos = (150, 300), length = 48, width = 24)
	legend = eztext.Button(caption = "guards = GREEN, arts = PINK, points = PURPLE, good = LIGHTBLUE, bad = ORANGE", pos = (X_DRAWING_OFFSET-5,9), length =SCREEN_WIDTH-X_DRAWING_OFFSET+5, width = 24,boxColor = SLATE)

	


	quit = False
	while(not quit):
		textSurface.fill((39,40,34))

		#frame rate = 30fps
		clock.tick(30)

		#Event variable list
		events = pygame.event.get()

		#get lists that finds the vision of the guards
		if button.onClicked(events):
			find_guard_vision(textBoxList)
			
			

		#find if the paintings are being guarded appropriately

		#print arts, guards, walls
		
		#check events
		for event in events:
			if event.type == pygame.QUIT:
				quit = True

		#update text on screen
		for textBox in textBoxList:
			textBox.update(events)
			textBox.draw(textSurface)


		legend.draw(screen)
		button.draw(textSurface)
		pygame.draw.line(textSurface, GREEN, (X_DRAWING_OFFSET-13,0), (X_DRAWING_OFFSET-13,SCREEN_HEIGHT), 2)
		screen.blit(textSurface,(0,0))
		pygame.display.flip()

if __name__ == '__main__':
	sys.exit(main())





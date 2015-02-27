from Map import Map
from random import random

class Dot:
    def __init__(self,map,i,id):
      self.map = map
      self.previous = i
      self.current = i
      self.id = id
      self.updatePosition()

    def walk(self):
      g = self.map.getGraph()
      currentV = g.getVertex(self.current)
      r = random()
      w = []
      for key in currentV.getConnections():
	w.append([currentV.getWeight(key), key])
      w.sort(key = lambda row:row[0])
      totalW = 0.0
      for t in w:
	totalW += t[0]
	if (r <= totalW):
	  self.previous = self.current
	  self.current = t[1].id
	  # print 'move from ' + str(self.previous) + ' to ' + str(self.current)
	  self.updatePosition()
	  return (self.getX(), self.getY())
      print 'ERROR: r=' + str(r) + ' totalW=' + str(totalW) + ' prev=' + str(self.previous) + ' cur=' + str(self.current)

    def getX(self):
      return self.x

    def getY(self):
      return self.y

    def getId(self):
      return self.id

    def updatePosition(self):
      factor = 0.6
      half = factor / 2.0
      r = random()
      rx = random() * factor
      ry = random() * factor
      g = self.map.getGraph()
      # print 'update from ' + str(self.previous) + ' to ' + str(self.current)
      previousV = g.getVertex(self.previous)
      currentV = g.getVertex(self.current)
      if (self.previous == self.current):
	self.x = currentV.getX() + rx - half
	self.y = currentV.getY() + ry - half
      else:
	previousX = previousV.getX()
	previousY = previousV.getY()
	currentX = currentV.getX()
	currentY = currentV.getY()
	if (currentX == previousX):
	  # print 'currentX == previousX'
	  self.x = currentX + rx - half
	  # self.y = currentY + ry - half
	  self.y = currentY + (previousY - currentY) * r
	elif (currentY == previousY):
	  # print 'currentY == previousY'
	  self.x = currentX + (previousX - currentX) * r
	  # self.x = currentX + rx - half
	  self.y = currentY + ry - half
	else:
	  # print 'Neither'
	  self.x = currentX + (previousX - currentX) * r
	  self.y = currentY + (previousY - currentY) * r
	  # self.x = currentX + rx - half
	  # self.y = currentY + ry - half

map = Map()
d0 = Dot(map, 2, 0)
for i in range(8):
  pos = d0.walk()
  # print str(d0.getId()) + ',' + str(i) + ',' +  str(pos[0]) + ',' + str(pos[1])

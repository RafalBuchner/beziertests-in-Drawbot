from drawBot import *

def setEnvironment(can=1000,movement=0):
    
    size(can,can)
    translate(can/2+movement,can/2+movement)
    stroke(0,0,0,0.3)
    lineDash(100,100)
    line((0,can),(0,-can))
    line((can,0),(-can,0))
    stroke(None)
    lineDash(None)

def drawPoint(P,pointSize=6, color=(1,0,0,.9)):
    x,y = P
    fill(*color)
    oval(x-pointSize/2,y-pointSize/2 , pointSize, pointSize)
    fill(None)
    
def drawCross(P,cursor=False,crossSize=10, color=(1,0,0,.9), can=1000):
    x,y = P
    stroke(*color)
    save()
    translate(x,y)
    if not cursor:
        rotate(45)
    line((0,-crossSize/2),(0,crossSize/2))
    line((-crossSize/2,0),(crossSize/2,0))
    
    stroke(0,0,0,0.1)
    
    if cursor:
        line((0,can),(0,-can))
        line((can,0),(-can,0))
    
    restore()
    
    if cursor:
        line((x,-crossSize/2),(x,crossSize/2))
        line((-crossSize/2,y),(crossSize/2,y))

        stroke(None)
        fill(*color)
        text("{}".format(x), (x+5,crossSize/2) )
        text("{}".format(y), (crossSize/2, y+5) )
    
    stroke(None)
    fill(None)
    
def drawBezier(*pointList):
    p1x,p1y = pointList[0]
    p2x,p2y = pointList[1]
    p3x,p3y = pointList[2]
    p4x,p4y = pointList[3]
    bez = BezierPath()
    bez.moveTo((p1x,p1y))
    bez.curveTo((p2x,p2y), (p3x,p3y), (p4x,p4y))
    stroke(0,0.4,1)
    drawPath(bez)
    stroke(0,0,0,.1)
    line(pointList[0],pointList[1])
    line(pointList[2],pointList[3])
    for p in pointList:
        drawPoint(p)
    

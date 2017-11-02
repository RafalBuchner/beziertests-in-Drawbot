from easyEnvironment import *
import math
setEnvironment(1000,-100)
crossLine = (392, 266)
P1 = (20, 30)
P2 = (126, 354)
P3 = (322, 336)
P4 = (404, 158)




drawCross(crossLine,True)
drawBezier(P1,P2,P3,P4)

###########################
def getLut(P1,P2,P3,P4):
    table = []
    for x in range(1,100):
        table.append( cBezier(x/100,P1,P2,P3,P4) )
    return table

def closest(pointOffCurve, P1,P2,P3,P4):
    """Returns closest point"""
    ### add option for closest point's t-value (you have to work with getLut)
    LUT = getLut(P1,P2,P3,P4)
    minimalDist = 10000
    position = -1
    distance = 0
    for n in range(len(LUT)):
        distance = lenghtAB(pointOffCurve, LUT[n])

        if distance < minimalDist:
            minimalDist = distance
            position = n

    if position == -1:
        # print "HUJNIA"
        return None

    return LUT[position]

def lenghtAB(A,B):
    bx,by = B
    ax,ay = A
    sqA = (bx - ax) **2
    sqB = (by - ay) **2
    sqC = sqA + sqB
    if sqC > 0:
        lengthAB = math.sqrt(sqC)
        return lengthAB
    else:
        return 0

def rotatePoint( P,angle, originPoint):
    """Rotates x/y around x_orig/y_orig by angle and returns result as [x,y]."""
    alfa = radians(angle)
    px,py=P
    originPointX, originPointY = originPoint

    x = ( px - originPointX ) * math.cos( alfa ) - ( py - originPointY ) * math.sin( alfa ) + originPointX
    y = ( px - originPointX ) * math.sin( alfa ) + ( py - originPointY ) * math.cos( alfa ) + originPointY

    return x, y
                  
def angle( A, B ):
    """returns angle between line AB and axis x"""
    ax, ay = A
    bx, by = B
    xDiff = ax - bx
    yDiff = ay - by
    if yDiff== 0 or xDiff== 0:
        tangens = 0
    else:
        tangens = yDiff / xDiff

    angle = math.atan( tangens )
    return degrees(angle)
                  
def cBezier(t, *pointList):
    """returns coordinates for factor called "t"(from 0 to 1). Based on cubic bezier formula.
    """
    p1x,p1y = pointList[0]
    p2x,p2y = pointList[1]
    p3x,p3y = pointList[2]
    p4x,p4y = pointList[3]
    if len(pointList) == 4:
        x = p1x*(1-t)**3 + p2x*3*t*(1-t)**2 + p3x*3*t**2*(1-t) + p4x*t**3
        y = p1y*(1-t)**3 + p2y*3*t*(1-t)**2 + p3y*3*t**2*(1-t) + p4y*t**3

        return x, y
    else:
        print "ERROR: cBezier() should have 4 points"


def derivativeBezier(t,*pointList):
    """ calculates derivative values for given control points and current t-factor """
    p1x,p1y = pointList[0]
    p2x,p2y = pointList[1]
    p3x,p3y = pointList[2]
    p4x,p4y = pointList[3]
    
    summaX = -3*p1x*(1 - t)**2 + p2x*(3*(1 - t)**2 - 6*(1 - t)*t) + p3x*(6*(1 - t)*t - 3*t**2) + 3*p4x*t**2
    summaY = -3*p1y*(1 - t)**2 + p2y*(3*(1 - t)**2 - 6*(1 - t)*t) + p3y*(6*(1 - t)*t - 3*t**2) + 3*p4y*t**2
    return summaX,summaY

def calculateTangentAngle(t, *pointList):
    """Calculates tangent angle for curve's current t-factor"""
    P1,P2,P3,P4 = pointList
    xT,yT = cBezier(t, P1,P2,P3,P4)
    xB,yB = derivativeBezier(t,*pointList)
    
    # stroke(0) ###test
    # line((xT,yT),(xT+xB,yT+yB)) ###test
    
    return angle((0,0),(xB,yB))




lineDash(5,5)
#### closest Point problem
closestOnCurve = closest(crossLine, P1,P2,P3,P4)
drawPoint(closestOnCurve,color=(0,0.5,1))

line(crossLine,closestOnCurve)


#### Tangent problem    
tValue = 0.17
tPx,tPy = cBezier(tValue, P1,P2,P3,P4)
tanAngle = calculateTangentAngle(tValue, P1,P2,P3,P4)


tanPx1,tanPy1 = rotatePoint( (0,100),tanAngle, (0,0)) # needed for StemThickness
tanPx2,tanPy2 = rotatePoint( (0,100),tanAngle-180, (0,0)) # needed for StemThickness
tanPx3,tanPy3 = rotatePoint( (0,100),tanAngle-90, (0,0))
tanPx4,tanPy4 = rotatePoint( (0,100),tanAngle-270, (0,0))
stroke(1,1,0)
line((tPx,tPy),(tanPx1+tPx,tanPy1+tPy))
stroke(1,0,0)
line((tPx,tPy),(tanPx2+tPx,tanPy2+tPy))
stroke(1,0,1)
line((tPx,tPy),(tanPx3+tPx,tanPy3+tPy))
stroke(0,1,1)
line((tPx,tPy),(tanPx4+tPx,tanPy4+tPy))



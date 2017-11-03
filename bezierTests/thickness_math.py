"""NEXT STEP: expand the curve to the whole segment with lines and few beziers and try to be able to work on that"""
import math



def closestPointAndT(pointOffCurve, P1,P2,P3,P4):
    """Returns closest point"""
    ### add option for closest point's t-value (you have to work with getLut)
    LUT = getLut(P1,P2,P3,P4, getT=True)
    minimalDist = 10000
    position = -1
    distance = 0
    for n in range(len(LUT)):
        distance = lenghtAB(pointOffCurve, LUT[n][0])

        if distance < minimalDist:
            minimalDist = distance
            position = n

    if position == -1:
        return None

    return LUT[position]

def lenghtAB(A,B):
    """Returns distance value between two points: A and B"""
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
    alfa = math.radians(angle)
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
    return math.degrees(angle)

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

    return angle((0,0),(xB,yB))
    
def getLut(P1,P2,P3,P4, getT=False, accuracy = 100):
    """Returns Look Up Table, which contains pointsOnCurve for cBezier, if getT=True tjen returns table with points and their factors"""
    lut_table = []
    for i in range(accuracy):
        
        print "" ###test
        t=i/accuracy
        print "OnCurve:{} || t:{} || i:{} || accuracy: {}".format(cBezier(t,P1,P2,P3,P4),t,i,accuracy)
        if not getT:
            
            lut_table.append( cBezier(t,P1,P2,P3,P4) )
        else:
            lut_table.append( (cBezier(t,P1,P2,P3,P4),t) )

    return lut_table


#test
P1 = (20, 30)
P2 = (-100, 336)
P3 = (322, 336)
P4 = (404, 158)
getLut(P1,P2,P3,P4)


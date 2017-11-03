"""NEXT STEP: expand the curve to the whole segment with lines and few beziers and try to be able to work on that"""
from easyEnvironment import *
from thickness_math import *
setEnvironment(800, -202)

cursorPoint = (-22, 480)
P1 = (20, 30)
P2 = (-100, 336)
P3 = (322, 336)
P4 = (404, 158)

drawCross(cursorPoint,True)
drawBezier(P1,P2,P3,P4)
print getLut(P1,P2,P3,P4)
lineDash(5,5)
#### closest Point problem
closestPoint, closestPoint_t = closestPointAndT(cursorPoint, P1,P2,P3,P4)
print closestPoint
drawPoint(closestPoint,color=(0,0.5,1))

line(cursorPoint,closestPoint)


#### Tangent problem
# tValue = 0.17
tValue = closestPoint_t ### connected problems into one solution
tPx,tPy = cBezier(tValue, P1,P2,P3,P4)
tanAngle = calculateTangentAngle(tValue, P1,P2,P3,P4)


tanPx1,tanPy1 = rotatePoint( (0,1000),tanAngle, (0,0)) # needed for StemThickness
tanPx2,tanPy2 = rotatePoint( (0,1000),tanAngle-180, (0,0)) # needed for StemThickness
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

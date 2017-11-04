"""NEXT STEP: expand the curve to the whole segment with lines and few beziers and try to be able to work on that"""
from easyEnvironment import *
from thickness_math import *

setEnvironment(786, -226)

cursorPoint = (460, 20)
P1 = (20, 30)
P2 = (446, 354)
P3 = (208, 334)
P4 = (404, 158)

def lineIntersection(A,B, C,D):
    ax,ay = A
    bx,by = B
    cx,cy = C
    dx,dy = D
    nx=(ax*by-ay*bx)*(cx-dx)-(ax-bx)*(cx*dy-cy*dx)
    ny=(ax*by-ay*bx)*(cy-dy)-(ay-by)*(cx*dy-cy*dx)
    d =(ax-bx)*(cy-dy)-(ay-by)*(cx-dx)
    if d==0:
        return false
        
    print nx
    return (nx/d, ny/d)
    
stroke(0,0.1,0.3)
line(P1,P2)
line(P3,P4)
drawPoint(lineIntersection(P1,P2,P3,P4))
for i in [P1,P2,P3,P4]:
    drawPoint(i)

# drawCross(cursorPoint,True)
# drawBezier(P1,P2,P3,P4)
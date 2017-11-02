from easyEnvironment import *
import math
setEnvironment(3000,-100)
crossLine = (552, 394)
P1 = (20, 30)
P2 = (126, 354)
P3 = (322, 336)
P4 = (404, 158)




drawCross(crossLine,True)
drawBezier(P1,P2,P3,P4)

###########################
pascalTriangle = [      [1],           # n=0
                       [1,1],          # n=1
                      [1,2,1],         # n=2
                     [1,3,3,1],        # n=3
                    [1,4,6,4,1],       # n=4
                   [1,5,10,10,5,1],    # n=5
                  [1,6,15,20,15,6,1]]  # n=6
                  
def angle( A, B ):
    """zmienna wskazująca kąt (w radianach) między odcinkiem, który przecina wskazane dwa punkty, a osią x"""
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

def binomial(n,k):
    #######Błagam, wymyśl nie generyczny kod na to, musisz zrobić stałą wartość
    #######Dąż do tego aby funkcję binomal wypierdolić

    while n >= len(pascalTriangle):
        s = len(pascalTriangle)
        nextRow = []
        nextRow[0] = 1
        for i in range(s):
            prev = s-1
            nextRow[i]= pascalTriangle[prev][i-1] + pascalTriangle[prev][i]
        nextRow[s] = 1
        pascalTriangle.append(nextRow)
    return pascalTriangle[n][k]

def derivativeBezier(n,t,*pointList):
    #######Błagam, wymyśl nie generyczny kod na to, musisz zrobić stałą wartość

    p1x,p1y = pointList[0]
    p2x,p2y = pointList[1]
    p3x,p3y = pointList[2]
    p4x,p4y = pointList[3]
    Wx = [p1x,p2x,p3x,p4x]
    Wy = [p1y,p2y,p3y,p4y]
    
    # derivativeBezier(n,t,*pointList):
    # summaX = 0 #we wzorze wartosc i poczatkowa
    # summaY = 0 #we wzorze wartosc i poczatkowa
    # i = 0
    # k = n - 1
    # while i <= k:
    #     # zapis sumaryczny: dumian newtona o wartosci gornej n, dolnej i, pomnoz to z (1-t)do potegi n-1 razy t do potegi i
    #     summaX += binomial(k,i) * (1-t)**(k-i) * t**i * n*(Wx[i+1] - Wx[i])
    #     summaY += binomial(k,i) * (1-t)**(k-i) * t**i * n*(Wy[i+1] - Wy[i])
    #     i += 1
    
    summaX = -3*p1x*(1 - t)**2 + p2x*(3*(1 - t)**2 - 6*(1 - t)*t) + p3x*(6*(1 - t)*t - 3*t**2) + 3*p4x*t**2
    summaY = -3*p1y*(1 - t)**2 + p2y*(3*(1 - t)**2 - 6*(1 - t)*t) + p3y*(6*(1 - t)*t - 3*t**2) + 3*p4y*t**2

    return summaX,summaY

def calculateTangentAngle(t, *pointList):
    P1,P2,P3,P4 = pointList
    
    xT,yT = cBezier(t, P1,P2,P3,P4)
    
    xB,yB = derivativeBezier(3,t,*pointList)
    # later you have to create special opperation for t = 0 and t = 1


    stroke(0) ###test
    line((xT,yT),(xT+xB,yT+yB)) ###test
    
    return angle((0,0),(xB,yB))

    
tValue = 0.2
tPoint = cBezier(tValue, P1,P2,P3,P4)
tanAngle = calculateTangentAngle(tValue, P1,P2,P3,P4)
drawCross(tPoint,color=(1,0,1))


### test
# stroke(None)
# for i in range(100):
#     i = i/100
#     drawPoint(derivativeBezier(3,i, P1,P2,P3,P4))
# print d
# stroke(0,1,0)
# line((0,0),(100,0))
# save()
# rotate(d)
# line((0,0),(100,0))
# restore()




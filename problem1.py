# Problem 1
# Finding intersection of two rectangles. 
#
# Write a function that takes the following arguments as input: 
#
# x1, y1, x2, y2 (coordinates of rectangle 1)
# a1, b1, a2, b2 (coordinates of rectangle 2) 
#
# The function should try and figure out whether the rectangles overlap or not. If they do, then it should return true, else return false. 
#
# The coordinates are float values, and can be large numbers. They can also be negative (in cartesian coordinate space).
#
#
# Solution:
# Given: Coordinates (x1,y1) and (x2,y2) of 2 points of a rectangle
# Description: Problem is incomplete
# Reason: If the 2 points are diagonally opposite, the third vertex can be anywhere in the semi-circle with the line joining the two given points as diameter
# If the 2 points are adjacent, the third point can be anyhwere in the line perpendicular to the line joining the two given points
# Assumption: Coordinates of third point (x3,y3) are correctly given for both rectangles, therefore the fourth point can be found


# This function takes in 3 points and finds the fourth point of rectangle
def completeRect(x1,y1,x2,y2,x3,y3) :
    len1=(x1-x2)**2+(y1-y2)**2
    len2=(x1-x3)**2+(y1-y3)**2
    len3=(x2-x3)**2+(y2-y3)**2
    # These 3 points form sides of a triangle, one of which will be a diagonal of the rectangle - Pythagoras theorem applied
    if((len1+len2)==len3) :  # 2 and 3 are ends of a diagonal
        x4=x2+x3-x1
        y4=y2+y3-y1
        diag1v1=2
        diag1v2=3
        # Therefore other diagonal will have 1 and 4 as ends
        diag2v1=1
        diag2v2=4
    elif((len1+len3)==len2) : # 1 and 3 are ends of a diagonal
        x4=x1+x3-x2
        y4=y1+y3-y2
        diag1v1=1
        diag1v2=3
        # Therefore other diagonal will have 2 and 4 as ends
        diag2v1=2
        diag2v2=4
    else : # 1 and 2 are ends of a diagonal
        x4=x1+x2-x3
        y4=y1+y2-y3
        diag1v1=1
        diag1v2=2
        # Therefore other diagonal will have 3 and 4 as ends
        diag2v1=3
        diag2v2=4
# Diagonal subscripts are also returned to reduce the number of steps in isInsideRect function from 6 (4C2) to 4
    return [x4,y4,diag1v1,diag1v2,diag2v1,diag2v2]



# This function generates the equation of line joining 2 points
def line(x1,y1,x2,y2) :
# Slope
    m=(y2-y1)/(x2-x1)
# Intercept
    c=(y1*x2-y2*x1)/(x2-x1)
    return [m,c]



# This function finds whether given point (x,y) is inside rectangle given by coordinates a,b
def isInsideRect(x,y,a,b,d1,d2) :
    list1=[1,2]
    m=[0,0,0,0]
    c=[0,0,0,0]
    val=[0,0,0,0]
    k=0
    ret=False
# A point lies between 2 parallel lines if the values obtained by substituting the point into equaiton of lines are of opposite sign (product is negative)
# This function returns True even if the point lies on one of the sides
    for i in list1 :
        for j in list1 :
            m[k],c[k]=line(a[d1[i-1]-1],b[d1[i-1]-1],a[d2[j-1]-1],b[d2[j-1]-1])
            val[k]=y-m[k]*x-c[k]
            k=k+1
    if(m[0]==m[2]) :
        prod1=val[0]*val[2]
        prod2=val[1]*val[3]
    else :
        prod1=val[0]*val[3]
        prod2=val[1]*val[2]
    if((prod1<=0) * (prod2<=0)) :
        ret=True
    return ret



# This function checks whether there is overlap between the two rectangles
# This funciton returns True even if the overlap is along a line and not a region
def overlap(rect1,rect2) :
# Obtain 4th point and end points of diagonals (subscripts) for first and second rectangles
    x4,y4,r1d1v1,r1d1v2,r1d2v1,r1d2v2=completeRect(rect1[0],rect1[1],rect1[2],rect1[3],rect1[4],rect1[5])
    a4,b4,r2d1v1,r2d1v2,r2d2v1,r2d2v2=completeRect(rect2[0],rect2[1],rect2[2],rect2[3],rect2[4],rect2[5])
    ret=False
# Putting together the coordinates of both rectangles and their diagonals (subscripts)
    x=[rect1[0],rect1[2],rect1[4],x4]
    y=[rect1[1],rect1[3],rect1[5],y4]
    a=[rect2[0],rect2[2],rect2[4],a4]
    b=[rect2[1],rect2[3],rect2[5],b4]
    r1d1=[r1d1v1,r1d1v2]
    r1d2=[r1d2v1,r1d2v2]
    r2d1=[r2d1v1,r2d1v2]
    r2d2=[r2d2v1,r2d2v2]
    list1=[1,2,3,4]
# Count the number of points of rectangle 1 inside/on rectangle 2 and vice versa
    add1=0
    add2=0
    for i in list1 :
        add1=add1+isInsideRect(x[i-1],y[i-1],a,b,r2d1,r2d2)
        add2=add2+isInsideRect(a[i-1],b[i-1],x,y,r1d1,r1d2)
    if((add1>0) + (add2>0)) :
        ret=True
    return ret
    


# Testing using example
x1=0
y1=0
x2=1
y2=1
x3=-1
y3=1
a1=0
b1=0
a2=1
b2=1
a3=-1
b3=1
rect1=[x1,y1,x2,y2,x3,y3]
rect2=[a1,b1,a2,b2,a3,b3]
print(overlap(rect1,rect2))

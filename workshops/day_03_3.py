""" 
NUMPY 
"""
import numpy as np # alias# The for function is useful but has limitations 
import matplotlib.pyplot as plt

# Normal loop
for i in range(1, 11):
    print(i)
    
"""
OUTPUT : 
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
"""

# numpy loop 
for i in np.arange(1, 11, 0.5):
    print(i)
# create numbers with floating points 
"""
OUTPUT : 
1.0 1.5 2.0 2.5 3.0 3.5 4.0 4.5 5.0 5.5 6.0 6.5 7.0 7.5 8.0 8.5 9.0 9.5 10.0 10.5
"""

# squaring the numbers for 1 to 5 in python
squares = []
for i in range(1, 6):
    squares.append(i**2)
print(squares)
# OUTPUT : [1, 4, 9, 16, 25]

# doing the same thing using numpy
squares = np.arange(1,6)**2
print(squares)
# [ 1  4  9 16 25] easier and works better with less coding (no loops required)

x = np.arange(1,6)
y = x**2

plt.plot(x, y, "r*")
plt.show()

print(x+y)
#  [ 2  6 12 20 30] adds element by element 

x = np.arange(1,6)
y = x**2
print(x*y)

# calculating dot product 
print(x.dot(y)) # 225 
print(x.shape)
print(y.shape)

# calculating cross product 
print(np.matmul(x,y)) # 225

# can't transpose (one dimension)
x.T

# convert into array from list 
alist = [1, 2, 5, 6, 15, 22]
anparray = np.array(alist)
print(anparray)
# [ 1  2  5  6 15 22] 

# to make a matrix from the list 
matrix = np.reshape(alist, [2,3])
print(matrix)
"""
OUTPUT : 
[[ 1  2  5]
 [ 6 15 22]]

"""
 # OR make it this shape from the start 
alist2 = [[1,2,5],[6,15,22]] 
data2 = np.array(alist2)
data2.shape # (2, 3)

# able to transpose
data2.T
"""
array([[ 1,  6],
       [ 2, 15],
       [ 5, 22]])
"""

alist = [1, 2, 5, 6, 15, 22]
data = np.array(alist)


alist = [1 , 2, 5, 6, 15, 22]
data  = np.array(alist)
data2 = data.reshape([2,3])
data3 = np.reshape(data,[2,3])
data4 = np.matmul(data2.T, data3)
"""
OUTPUT : 
array([[ 37,  92, 137],
       [ 92, 229, 340],
       [137, 340, 509]])
"""

crossdata = np.cross(data2[0,:], data3[1,:])
"""
OUTPUT: 
array([-31,   8,   3])

"""

# Solve linear equations
a = np.array([[1, 2, 3],[4, 5, 6],[7, 8, -9]])
b = np.array([3, -4, 2])

# find determinant
d = np.linalg.det(a)
# if STATEMENT not a LOOP
if(d>0):
    print(f"d = {d}, so this matrix is solvable")
# OUTPUT : d = 53.999999999999986, so this matrix is solvable

# linalg submodule for linear algebra
sol = np.linalg.solve(a,b) # finding solution for system of equations given above 


################################################################

import numpy as np 

# like read_csv from pandas but less options, it gives numpy array 
# note you can specify if you only want to access certain  columns 
data = np.loadtxt("C:/Users/alice/CHPC/file.csv", skiprows=1, delimiter=",")
pressure = data[:,0]
flowrate = data[:,1]

# Polynomial curve fit (SciPy for more complex functions like arbitary curve fits)
fit = np.polyfit(pressure, flowrate, 3)
# OUTPUT : solution gives the coefficients 

# evaluate pressure 
flowfit = np.polyval(fit, pressure)

# make a graph 
plt.plot(pressure, flowrate, "go")
plt.plot(pressure, flowfit, "k-")
plt.xlabel("pressure (Pa)")
plt.ylabel("flow rate ($m^3/s$)")  # access Latex syntax
plt.show()

# find average of orig data for each column 
data_avg = np.mean(data, 0)
# average pressure = 5, av flow = 42 

# finding average of a specific column (in this case the 2nd column)
data_avg[1]

# To filter data for plot 
pressure < 4
"""
OUTPUT : 

    Tells us which values of the array do or do not satisfy a certain criteria (Boolean values T/F)
    array([ True,  True,  True,  True, False, False, False, False, False,
           False, False])
    
"""
 
# To filter out for only values that are true (NOTE : only for arrays and not lists)
 pressure[pressure < 4] # specifes using the output array 
 """
 array([0., 1., 2., 3.])
 """
 
# Example : modelling called monte carlo 
# Large # of random point on 2D plane point by x = (0, 1) and y = (0, 1)
# Q: randomly generating points in co-ordinate plane 

n = 10
x = np.random.uniform(size=n)
y = np.random.uniform(size=n)
plt.plot(x[x*x+y*y<=1], y[x*x+y*y<=1], "bo")
plt.plot(x[x*x+y*y>1],y[x*x+y*y>1], "ro")
plt.title("Calculating $\pi$")
plt.show()
plt.savefig("pi.jpg")

print(sum(x*x+y*y<=1)/n*4)
# OUTPUT : 3.1321333333333334
# good estimate for the value of pi (would be far more difficult without numpy)

"""
(x*x + y*y)<=1

Calculates how many points are in the 1/4 circle 
array([0.42150268, 0.0859138 , 0.85793399, ..., 0.08887786, 0.4586671 ,
       0.68500912])
"""












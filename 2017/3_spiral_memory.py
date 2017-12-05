import math
from decimal import *

input = 277678

sqrt = Decimal(math.sqrt(input))
roundedSqrt = round(sqrt,0)
nearestSq = roundedSqrt * roundedSqrt
x = 0
y = 0

if roundedSqrt % 2 == 0:
	sqY = (roundedSqrt / 2)
	sqX = roundedSqrt / 2 - 1
else:
	sqY = math.floor(roundedSqrt / 2)
	sqX = sqY

if nearestSq == roundedSqrt:
	x = sqX
	y = sqY
else:
	if input > nearestSq:
		x = sqX + 1
		adj = (nearestSq + 1)
		if (input - adj) <= sqY:
			y = sqY - (input - adj)
		else:
			y = abs(((input - adj) - sqY))
	else:
		y = sqY
		if (nearestSq - input) >= sqX:
			x = (nearestSq - input) - sqX
		else:
			x = abs((nearestSq - input) - sqX)

print("sqrt", sqrt)
print("roundedSqrt", roundedSqrt)
print("nearestSq", nearestSq)
print("Nearest Square Coord", sqX, ",", sqY)
print("Input Coord", x, ",", y)
print("Distance:", (x+y))
# isRotation(x, y) [15 pts]
# Write the function isRotation(x, y) that takes two non-negative integers x and y, both 
# guaranteed to not contain any 0's, and 
# returns True if x is a rotation of the digits of y and False otherwise. For example, 
# 3412 is a rotation of 1234. Any number 
# is a rotation of itself.

def isrotation(x, y):
	
	a=str(x)
	b=str(y)
	l=len(a)
	if a[::-1]==b:
		return True
	for i in range(l):
		c=a[i:l]+a[:i]
		if c==b:
			return True
	return False
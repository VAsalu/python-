def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVDING %d / %d" % (a, b)
	print a / b


print "Let's do some math with just functions!"

age = add(22, 1)
height = subtract(78, 4)
weight = multiply(115, 2)
iq = divide(100, 2)

print "age: %d, height: %d, weight: %d, iq: %d" % (age, height, weight, iq)


# A Puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iiq, 2))))

print "That becomes: ", what, "Can you do it by hand?"
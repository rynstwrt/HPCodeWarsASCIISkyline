import math

inpt = "4\n4 4 8\n10 10 4\n13 5 6\n2 4 4"

pic = ""

buildings = inpt.split("\n")[1:]

maxW = maxH = 0

for building in buildings:
	xcoord, width, height = map(int, building.split(" "))
	totalW = xcoord + width
	if totalW > maxW: maxW = totalW
	if height > maxH: maxH = height

pic = (" " * maxW + "\n") * maxH

def replaceAt(row, col, new):
	global pic
	lines = pic.split("\n")
	chars = list(lines[row])
	chars[col] = new
	lines[row] = ''.join(chars)
	pic =  "\n".join(lines)

def draw(xcoord, width, height):
	global pic
	for h in range(maxH):
		for w in range(maxW):

			fromBottom = maxH - h

			#sides
			if (w == xcoord or w == xcoord + width) and height >= fromBottom:
				replaceAt(h, w, "|")

			#roof
			if w >= xcoord and w <= xcoord + width and height == fromBottom:
				replaceAt(h, w, "-")

			#windows
			if w > xcoord and w < xcoord + width and height > fromBottom:
				replaceAt(h, w, "#")

for building in buildings:
	xcoord, width, height = map(int, building.split(" "))
	draw(xcoord - 1, width - 1, height - 1)

print pic, "1234567890" * int(math.ceil(maxW / 10))

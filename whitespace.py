#cus im lazy and like to copy
# coding=utf8

text = '<insert damm text>'
firstType = ' '
secondType =  ' '
binaryString = ''

for char in text: #Foreach char
	if char == firstType: #Check if it is the first type
		binaryString += '0' #Mark it as 0 <change as needed>
	else:
		binaryString += '1' #Mark it as 1

print(binaryString) #Print result

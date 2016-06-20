x = int(raw_input("Enter the value of row: "))
y = int(raw_input("Enter the value of column: "))

a = [[0 for row in range(0,x)] for col in range(0,y)]
b = [[0 for row in range(0,x)] for col in range(0,y)]
result = [[0 for row in range(0,x)] for col in range(0,y)]

print("Enter elements of first matrix: ")
for i in range(x):
	for j in range(y):
		a[i][j] = int(raw_input())

print("Enter the elements of second matrix: ")
for i in range(x):
	for j in range(y):
		b[i][j]=int(raw_input())

print
print("Elements of First matrix is: ")
for row in a:
	print(row)

print
print ("Elements of second matrix")
for row in b:
	print(row)

#iterate through rows
for i in range(len(a)):
	#iterate through columns
	for j in range(len(a[0])):
		result[i][j] = a[i][j]+b[i][j]

print
#print the sum of 2 matrices
print("Sum of the two matrices is: ")
for r in result:
	print(r)
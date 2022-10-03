# JOSUA PANGIHUTAN SITANGGANG 2021081366

name = "Josua Pangihutan Sitanggang dengan NIM"
NIM = " 20210801366"
print(name + NIM)

number = input('Type a number and enter:')
print('The number is :' + number)

# program 2x2 matrix

firstMatrix = [
    [1, 3], 
    [5, 7]
]
secondMatrix = [
    [2, 4], 
    [6, 8]
]
result = [[0, 0], [0, 0]];


# ADD 2 MATRIKS
for a in range(0, len(firstMatrix)):
    for b in range(0,len(secondMatrix[0])):
        result[a][b] = firstMatrix[a][b] + secondMatrix[a][b]

print('RESULT ADD 2 MATRIKS')    
for c in result:
    print(c)

for a in range(0, len(firstMatrix)):
    for b in range(0,len(firstMatrix[0])):
        result[a][b] = firstMatrix[a][b] - secondMatrix[a][b]

print('RESULT MIN 2 MATRIKS')    
for c in result:
    print(c)
vec = [-4, -2, 0, 2, 4]
a = [x*2 for x in vec]
print(a)

b = [x for x in vec if x>= 0]
print(b)

c = [abs(x) for x in vec]
print(c)

freshfruit = ['   banana', ' loganberry   ', 'passion  fruit   ']
d = [weapon.strip() for weapon in freshfruit]
print(d)

e = [(x, x**2) for x in range(6)]
print(e)

vec = [[1,2,3], [4,5,6], [7,8,9]]
f = [num for elem in vec for num in elem]
print(f)

matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)


import math



file = open('input.txt', 'r')
numbers = file.readline().split()
a = float(numbers[1])
z = float(numbers[0])
d = (1 / ((z - 2 * a) ** 2)) - z ** 2
f = d ** 2/3


print(f"a = {a}\nz = {z}\nd = {d}\nf = {f}")

x = open("output.txt", 'w')
x.write(f"d = {d}\nf = {f}")
import math


def data(file_path='input.txt'):
    with open(file_path, 'r') as file:
        numbers = file.readline().split()
        a = float(numbers[1])
        z = float(numbers[0])
        d = (1 / (z - 2*a)**2) - z**2
        f = d ** (2 / 3)
    return a, z, d, f
result = data()

result_str = f"x: {result[0]}\n n: {result[1]}\n m: {result[2]}\n f: {result[3]}"
print(result_str)
with open("output.txt", 'w') as f:
    f.write(result_str)
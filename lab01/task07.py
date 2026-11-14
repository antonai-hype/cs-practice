number = int(input(1234))
d1 = number // 1000
d2 = (number // 100) % 10
d3 = (number // 10) % 10
d4 = number % 10
print(d1)
print(d2)
print(d3)
print(d4)
print(d1 + d2 + d3 + d4)
print(d4 * 1000 + d3 * 100 + d2 * 10 + d1)
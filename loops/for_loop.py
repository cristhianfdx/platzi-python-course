# range(start, end, step)

print(range(5)) # [0, 1, 2, 3, 4]
print(range(5, 40, 3)) # [5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38]

for i in range(5):
    print(i)

# 0
# 1
# 2
# 3
# 4

for i in range(5):
    print('Hello')

# Hello
# Hello
# Hello
# Hello
# Hello

for i in range(30):
    if i % 3 != 0:
        continue
    else:
        print(i**2)

# 0
# 9
# 36
# 81
# 144
# 225
# 324
# 441
# 576
# 729

for i in range(30):
    if i % 3 == 0:
        print(i**2)
    elif i == 22:
        break

# 0
# 9
# 36
# 81
# 144
# 225
# 324
# 441

for s in 'platzi':
    print(s)

# p
# l
# a
# t
# z
# i
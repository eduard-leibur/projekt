järjend = [1, 2, 3, 4, 5, 6]
uus = []

for i in range(len(järjend) // 2):
    uus.append(järjend[i])
    uus.append(järjend[len(järjend) - (i + 1)])
print(uus)

import random
n = 1
print(str(n))
for _ in range(n):
    m = 10
    print(str(m))
    distances = []
    for _ in range(m):
        idk = random.randint(1,25)
        distances.append(idk)
    string1 = ""
    for x in distances:
        string1 += str(x) + " "
    print(string1)

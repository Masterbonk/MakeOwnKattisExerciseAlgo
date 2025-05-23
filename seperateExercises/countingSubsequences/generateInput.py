import random
#t = random.randint(1,10)
t=10
print(str(t))
for _ in range(t):
    print()
    #n = random.randint(1,1000000)
    n = 1000000
    print(str(n))
    list = []
    for _ in range(n):
        list.append(random.randint(-20000,20000))
    print(' '.join(str(x) for x in list))
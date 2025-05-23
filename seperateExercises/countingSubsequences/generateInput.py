import random
#t = random.randint(1,10)
f = open(f"10ThatWorks", "w")


t=10
f.writelines(str(t)+ '\n')
for _ in range(t):
    f.writelines('\n')
    #n = random.randint(1,1000000)
    n = 10
    f.writelines(str(n)+ '\n')
    list = []
    for _ in range(n):
        list.append(random.randint(-20000,20000))
    f.writelines(' '.join(str(x) for x in list)+ '\n')
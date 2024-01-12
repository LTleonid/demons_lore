import random
r1 = 0
r0 = 0
r2 = 0
for i in range(100):
    r = random.randint(0,2)
    if r == 0:
        r0 += 1
    if r == 1:
        r1 += 1
    if r == 2:
        r2 += 1
print(f'{r1=},{r2=},{r0=}')
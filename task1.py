import random
from collections import Counter

n = int(input("Количество монет "))
melon = Counter([random.randint(0,1) for i in range(n)])
zero = melon[0]
one= melon[1]
print(melon)

if zero > one:
    print(f"Нужно перевернуть {one} монет с решки на орла, их меньше")    # орел - сторона с орлом, решка сторона с номиналом "1"
else:
    print(f"Нужно перевернуть {zero} монет с орла на решку, их меньше")    




import random

randArr = []

for i in range(0, 10):
	randArr.append(random.randint(1,20))

randArr = list(dict.fromkeys(randArr))

print(randArr)
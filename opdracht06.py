from isUniek import isUniek
import random

arr = []

for i in range(1, random.randint(5,20)):
	arr.append(random.randint(1,20))

print(arr)
print(isUniek(arr))
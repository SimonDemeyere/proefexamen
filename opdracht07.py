from isUniek import isUniek

number = int(input("Geef een getal:"))
arr = []

for i in range(1, number + 1):
	if (number % 2 != 0 and number // 2 + 1 == i):
		print(number, i)
		arr.append(i)
	arr.append(i)

print(arr)
isUniek(arr)

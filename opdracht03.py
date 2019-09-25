number = int(input("Geef een getal:"))

arr1 = []
arr2 = []
arr3 = []
lenArr = []

s = ""

for i in range(1, number, 4):
	arr1.append(i)

for i in range(2, number, 7):
	arr2.append(i)

for i in range(0, len(arr1)):
	arr2.insert(i + 2, arr1[i])



print(arr1)
print(arr2)
print(s[:-1])
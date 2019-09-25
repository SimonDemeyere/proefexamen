from gemiddelde import gemiddelde

lijstEen = []
lijstTwee = []

number = int(input("Geef een getal:"))

for i in range(1, number + 1):
	if (i % 5 == 0 or i == 1):
		lijstEen.append(i)
	else:
		lijstTwee.append(i)

print("lijstEen =", lijstEen)
print("lijstTwee =",lijstTwee)
print("De som van lijstEen =", sum(lijstEen))
print("Het gemiddelde van lijstTwee =", gemiddelde(lijstTwee))
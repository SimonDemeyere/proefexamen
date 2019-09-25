def drieMiddelstekarakters(string):
	halfOfRest = 0
	if (len(string) % 2 != 0):
		rest = len(string) - 3
		halfOfRest = int(rest // 2)
		# if halfOfRest % 2 == 0:
		# 	halfOfRest - 1
		# print(halfOfRest)
	else:
		print("Geen oneven woord")

	print(string[halfOfRest:][:-halfOfRest])
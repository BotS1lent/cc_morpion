print("test2")
i = 0
C0 = ['C0']
C1 = ['C1']
C2 = ['C2']
C3 = ['C3']
C4 = ['C4']
C5 = ['C5']
C6 = ['C6']
C7 = ['C7']
C8 = ['C8']
M1 = C0 + C1 + C2
M2 = C3 + C4 + C5
M3 = C6 + C7 + C8
game = M1 + M2 + M3
print(M1)
print(M2)
print(M3)


while i!=9 :
	print("Au tour des croix !")
	X = input('')
	while X 

		print(M1)
		print(M2)
		print(M3)
	else :
		print("TRICHEUR, réessaie")
	i += 1
	if i == 9 :
		break

	print("Au tour des cercles!")
	O = input('')
	if O in game :
		del game[O]
		print(M1)
		print(M2)
		print(M3)

	i += 1
	if i == 9 :
		break

print ("Partie fini")
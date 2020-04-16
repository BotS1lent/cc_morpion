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
	if X in game :
		if X in M1 :
			A = M1.index(X)
			M1[A]="X"
		
		elif X in M2 :
			A = M2.index(X)
			M2[A]="X"
			del home[A]
		elif X in M3 :
			A = M3.index(X)
			M3[A]="X"
			del home[A]
		print(game)
		print(M1)
		print(M2)
		print(M3)
	else :
		print("TRICHEUR, saute ton tour")
	i += 1
	if i == 9 :
		break

	print("Au tour des cercles!")
	O = input('')
	if O in game :
		if O in M1 :
			A = M1.index(O)
			M1[A]="O"
		if O in M2 :
			A = M2.index(O)
			M2[A]="O"
		if O in M3 :
			A = M3.index(O)
			M3[A]="O"
		print(game)
		print(M1)
		print(M2)
		print(M3)
	else :
		print("TRICHEUR, saute ton tour")
	i += 1
	if i == 9 :
		break

print ("Partie fini")
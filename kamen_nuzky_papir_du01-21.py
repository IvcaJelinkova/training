# hra kámen, nůžky, papír
# 1. hodina PyLadies kurzu pro začátečníky

from random import randrange
tah_pocitace = randrange (3)

if tah_pocitace == 0: 
	tah_pocitace = "kámen"
elif tah_pocitace == 1: 
	tah_pocitace = "nůžky"
else: 
	tah_pocitace = "papír"

print()
tah_hrace = input("Jaký je tvůj tah? (Zadej kámen, nůžky nebo papír.): \t")
while True:
	if tah_hrace == "kámen": 
		if tah_pocitace == "kámen":
			print("Remíza! ")
		elif tah_pocitace == "nůžky": 
			print("Vyhrál jsi! ")
		else: 
			print("Prohrál jsi! ")
		break

	elif tah_hrace == "nůžky": 
		if tah_pocitace == "nůžky":
			print("Remíza! ")
		elif tah_pocitace == "kámen": 
			print("Prohrál jsi! ")
		else: 
			print("Vyhrál jsi! ")
		break

	elif tah_hrace == "papír": 
		if tah_pocitace == "papír": 
			print("Remíza! ")
		elif tah_pocitace == "kámen": 
			print("Vyhrál jsi! ")
		else: 
			print("Prohrál jsi! ")
		break

	else: 
		print("Pardon, znám jen kámen, nůžky, papír. ")
		tah_hrace = tah_hrace = input("Jaký je tvůj tah? (Zadej kámen, nůžky nebo papír.): \t")

print("   Tah PC:  ", tah_pocitace)
print("   Tvůj tah:", tah_hrace, "\n")

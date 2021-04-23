#lecture du fichier (mon input)
f = open('day3.txt','r')
a=f.readlines()
n=len(a)


#création de la map avec n répétitions
def create_map(L):
	n = len(L)
	Map = []
	for i in range (n):
		Map.append(L[i].split('\n')[0]*n)
	return Map

Map = create_map(a)

#fonction  pour compter le nb d'arbre ayant comme paramètre r pas à droite et 1 pas en bas
def compte_arbre(L,r,d=1):
	arbre = 0
	j = 0
	for i in range (0,len(L),d):
		if j < len(L[i]):
			if L[i][j] == "#":
				arbre +=1
			#we add +j because we used a function to create the "missing part" of the environment [create_map]
			j+=r
	return arbre 


def compte_arbre_v2(L,r1,r3,r5,r7,d2):
	arbre = [compte_arbre(L,r1),compte_arbre(L,r3),compte_arbre(L,r5),compte_arbre(L,r7),compte_arbre(L,r1,d2)]
	compte = 0
	j = 0
	#partie pour compter avec  un pas à droite et 2 en bas
	#on utilise cette fonction car dans la partie du dessus on
	"""for i in range(0,len(L),2):
		if j <len(L):
			if L[i][j] == "#":
				compte +=1
			j+=1
	arbre.append(compte)"""
	print(arbre)
	return arbre[0]*arbre[1]*arbre[2]*arbre[3]*arbre[4]


v1 = compte_arbre(Map,3)
print("Réponse pour la v1 = ",v1) #189

v2 = compte_arbre_v2(Map,1,3,5,7,2)
print("Réponse pour la v2 = ",v2) #1718180100
			


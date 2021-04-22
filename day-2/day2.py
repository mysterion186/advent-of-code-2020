f = open("day2.txt")
lines = f.readlines()


# get the highest and lowest time a letter occur and the letter
def get_infos(L):
	i_prev = 0
	n1 = 0
	n2 = 0
	ni = 0
	char =""
	for k in range (len(L)):
		for i in range (len(L[k])):
			if L[k][i] == "-":
				n1 = L[k][i_prev:i]
				i_prev = i+1
			elif L[k][i] == " ":
				n2 =  L[k][i_prev:i-3]

				#char = L[k][i-1]
			elif L[k][i] == ":" :
				char = L[k][i-1]
				ni = i

	return [n1,n2,char,ni]



def compte(L):
	
	#print(info)
	compte_final = 0
	
	for k in range (len(L)):
		info = get_infos([L[k]]) #contient le nb mini, max et la lettre qu'on veut dans le mdp
		#print(info)
		compte = 0
		new_list = L[k][info[3]+2:]
		#print(new_list)
		for char in L[k][info[3]+2:]:

			if char == info[2]:
				compte = compte+1
				#print(compte)
		if int(info[0])<=compte<=int(info[1]):
			compte_final= compte_final +1
	return ("nb de mdp qui respect = {} ".format(compte_final))


print(compte(lines))


def check_password(L):
	compte_final = 0
	invalide = 0
	for k in range (len(L)):
		info = get_infos([L[k]]) #contient le nb mini, max et la lettre qu'on veut dans le mdp
		#print(info)
		compte = 0
		new_list = L[k][info[3]+2:]
		#print(new_list)
		if new_list[(int(info[0])-1)] == info[2] and new_list[(int(info[1])-1)] == info[2] :
			invalide+=1

		else :

			if new_list[(int(info[0])-1)] == info[2] :
				compte_final+=1
			elif new_list[(int(info[1])-1)] == info[2] :
				compte_final+=1

	return ("nb de mdp qui respect la nouvelle convention : {}\nle nb de mot de passe invalide est  : {}".format(compte_final,invalide))



print("*"*50)
print(check_password(lines))






















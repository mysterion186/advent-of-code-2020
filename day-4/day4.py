f = open("day4.txt",'r')
a = f.readlines()
g=open("input.txt",'r')
b= g.readlines()

#crée une liste où chaque élément contient les informations d'un passport
def create (L):
	passport = []
	char = ""
	for i in range(len(L)-1):
		if L[i]!= '\n' and L[i+1] == '\n' :
			if char == "":
				passport.append(L[i].split('\n')[0])
			else :
				passport.append(char+" "+L[i].split('\n')[0])
				char = ""
		else :
			char = char + " " + L[i].split('\n')[0]
	return passport
			


#vérifie que le passport est valide selon le type V1
def passport_info(char):
	valide = 0
	for i in range(len(char)):
		if char[i:i+3]=="byr":
			valide+=1
		if char[i:i+3]=="iyr":
			valide+=1
		if char[i:i+3]=="eyr":
			valide+=1
		if char[i:i+3]=="hgt":
			valide+=1
		if char[i:i+3]=="hcl":
			valide+=1
		if char[i:i+3]=="ecl":
			valide+=1
		if char[i:i+3]=="pid":
			valide+=1
	if valide == 7 :
		return True
	return False

def passport_info_v2_wrong(char):
	valide = 0 
	L_hcl = ['a','b','c','d','e','f','0','1','2','3','4','5','6','7','8','9'] #contient les vvaleur que peut prendre hcl
	L_ecl = ['amb','blu','brn','gry','grn','hzl','oth']
	if passport_info(char):
		for i in range(len(char)):
			if char[i:i+3]=="byr":
				if  1920<=int(char[i+4:i+8])<=2002:
					valide+=1
					#print("ok byr")
			if char[i:i+3]=="iyr":
				if 2010<=int(char[i+4:i+8])<=2020:
					valide+=1
					#print("ok iyr")
			if char[i:i+3]=="eyr":
				if 2020<=int(char[i+4:i+8])<=2030:
					valide+=1
					#print("ok eyr")
			if char[i:i+3]=="hgt":
				if char[i+7:i+9] == 'cm':
					if 150<=int(char[i+4:i+7])<=193:
						valide+=1
						#print("hgt cm ")
				elif char[i+6:i+8]=="in":
					if 59<=int(char[i+4:i+6])<=76:
						valide+=1
						#print("hgt in")
			if char[i:i+3]=="hcl":
				#print("hcl in")
				#print("hcl",char[i+4] , "test"+char[i+11]+"test")
				#print(char[i+5:i+12]+"a")
				if char[i+4] == '#':
					v_test = 0
					#print("test hcl valide ")
					for c in  char[i+5:i+11] :
						for elt in L_hcl:
							#print("c={} elt = {}".format(c,elt))
							if c == elt:
								#print("ok")
								v_test +=1
					#print("v_test ",v_test)
					if v_test == 6 :
						valide+=1
						#print("ok hcl")
			if char[i:i+3]=="ecl":
				#print("ecl in")
				for elt in L_ecl:
					if elt == char[i+4:i+7]:
						valide +=1
						#print("ecl ok ")
				#valide+=1
			if char[i:i+3]=="pid":
				invalide_id = 0
				if len(char[i+5:i+13])==9:
					try :
						a = int(char[i+5:i+13])
						valide +=1
					#print("ok id")
					except ValueError :
						invalide_id +=1 
				#print("test", valide)
	if valide == 7 :
		return True
	return False



# on décompose les test en plusieurs sous fonctions pour faciliter le débuguage
# verif pour byr
def condition_byr(char):
	for i in range(len(char)):
		if char[i:i+3]=="byr":
			if  1920<=int(char[i+4:i+8])<=2002:
				return True
	return False 

#vérif ppour iyr 
def condition_iyr(char):

	for i in range(len(char)):
		if char[i:i+3]=="iyr":
			if 2010<=int(char[i+4:i+8])<=2020:
				return True
	return False

#vérif pour eyr 
def  condition_eyr(char):
	for i in range(len(char)):
		if char[i:i+3]=="eyr":
			if 2020<=int(char[i+4:i+8])<=2030:
				return True
	return False
#vérif pour hgt
def condition_hgt(char):
	for i in range(len(char)):
		if char[i:i+3]=="hgt":
			if char[i+7:i+9] == 'cm':
				if 150<=int(char[i+4:i+7])<=193:
					return True
			elif char[i+6:i+8]=="in":
				if 59<=int(char[i+4:i+6])<=76:
						return True
	return False

#vérif pour hcl 
def condition_hcl(char):
	L_hcl = ['a','b','c','d','e','f','0','1','2','3','4','5','6','7','8','9'] #contient les vvaleur que peut prendre hcl
	for i in range(len(char)):
		if char[i:i+3]=="hcl":
				#print("hcl in")
				#print("hcl",char[i+4] , "test"+char[i+11]+"test")
				#print(char[i+5:i+12]+"a")
			if char[i+4] == '#' and char[i+11]=='\n':
				v_test = 0
					#print("test hcl valide ")
				for c in  char[i+5:i+11] :
					for elt in L_hcl:
							#print("c={} elt = {}".format(c,elt))
						if c == elt:
								#print("ok")
							v_test +=1
					#print("v_test ",v_test)
				if v_test == 6 :
					return True
						#print("ok hcl")
	return False

#vérif pour ecl
def condition_ecl(char):
	L_ecl = ['amb','blu','brn','gry','grn','hzl','oth']
	for i in range(len(char)):
		if char[i:i+3]=="ecl":
				#print("ecl in")
			for elt in L_ecl:
				if elt == char[i+4:i+7]:
					return True
	return False

#vérif pour pid
def condition_pid(char):
	for i in range(len(char)):
		if char[i:i+3]=="pid":
			invalide_id = 0
			try :
				a = int(char[i+5:i+13])
				return True
					#print("ok id")
			except ValueError :
				invalide_id +=1 
	return False

# utilisation de toutes les fonctions du dessus pour voir si ça marche :
def passport_valide_info_v2(L):
	valide = 0
	for k in range (len(L)):
		#print("avant le if")
		if condition_pid(L[k]) and condition_ecl(L[k]) and condition_hcl(L[k]) and condition_byr(L[k]) and condition_iyr(L[k]) and condition_eyr(L[k]) and condition_hgt(L[k]):
			valide +=1
			#print("on rentre dans le if")
	return valide



#retourne le nb de passport qui répondent aux critères 
def compte_valide_passport(L):
	valide = 0
	for k in range (len(L)):
		if passport_info(L[k]):
			valide+=1
	return valide



def affiche(L):
	for i in range (len(L)):
		print(L[i])



def compte_valide_passport_v2(L):
	valide = 0
	for k in range(len(L)):
		#print("avant le if ",valide)
		if passport_info_v2_wrong:
			#print("passage par le if")
			valide +=1
	return valide



print("nb de passport valide = ",compte_valide_passport(create(a)))
"""
print("nb de passport valide v2 = ",passport_valide_info_v2(create(a)))
"""
print("Kadir = ",compte_valide_passport(create(b)))
#print(create(a))
"""
print("byr = ",condition_byr("pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1900 hcl:#623a2f  "))
print("iyr = ",condition_iyr("pid:087499704 hgt:74in ecl:grn iyr:2052 eyr:2030 byr:1980 hcl:#623a2f  "))
print("eyr = ",condition_eyr("pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2330 byr:1980 hcl:#623a2f  "))
print("hgt = ",condition_hgt("pid:087499704 hgt:744in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f  "))
print("hcl = ",condition_hcl("pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623Va2f  "))
print("ecl = ",condition_ecl("pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f  "))
print("pid = ",condition_pid("pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f  "))
print("final  = ",passport_valide_info_v2(["pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f  "]))
print("final ECHEC   = ",passport_valide_info_v2(["hcl:dab227 iyr:2012 ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277"]))

"""






"""
print("True valeur =",compte_valide_passport_v2(["pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f"]))
#print(affiche(create(a)))

print("False = ",compte_valide_passport_v2([3]))

hello = "0005"
print(hello)
print(type(int(hello)))

"""




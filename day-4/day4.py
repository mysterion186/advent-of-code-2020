#read the file
with open("day4.txt","r") as f :
	raw_passport = f.readlines()

#get cleaned passport data :
#one element of the list will be a passport stored as a string
def get_clean_passport(raw_passport):
	clean_passport = []
	#use this indice to get one single passport/string
	i_prev = 0
	temp = ""
	for i in range(len(raw_passport)):
		if raw_passport[i] == "\n":
			#update the value of i_prev
			i_prev = i+1
			#add the passport to the cleaned list and reset temp
			clean_passport.append(temp)
			temp = "" 
		else :
			temp += raw_passport[i].replace("\n"," ") 
	#in case the final line isn't a \n we loose one password, to prevent this we test temp 
	#to be sure that it is not empty
	if temp !="":
		clean_passport.append(temp)
	return clean_passport 

#check if the field is in the passport
def check_field(passport,field):
	if field in passport:
		return True
	return False

#function to test if all the field
#v = True == part one and v = False == part two
def day_4 (clean_passport,v = True ):
	field_list = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
	count = 0
	field_count = 0
	for passport in clean_passport :
		#check all the field in the passport
		for field in field_list :
			if check_field (passport,field):
				if not v :
					if validator(passport,field):
						 field_count+=1
				else :
					field_count+=1 #get the number of present fields in the passport
		#if field_count == 7 means that all the fiels are in the passport
		if field_count == 7 :
			count+=1
		#reset of the field_count
		field_count = 0
	return count


#print("Solution for the part 1 : ",day_4(get_clean_passport(raw_passport))) #213


#return the field value 
def get_field_value(passport,field):
	field_indice = passport.index(field+":")
	value = passport[field_indice+4:passport.index(" ",field_indice)]
	return value 

#check if  byr is valid
def valid_byr(passport):
	value = int(get_field_value(passport,"byr"))
	if value <= 2002 and value >= 1920: 
		return True
	return False

#check if iyr is valid
def valid_iyr(passport):
	value = int(get_field_value(passport,"iyr"))
	if value <= 2020 and value >= 2010: 
		return True
	return False
#check if eyr is valid
def valid_eyr(passport):
	value = int(get_field_value(passport,"eyr"))
	if value <= 2030 and value >= 2020: 
		return True
	return False

#check if hgt is valid
def valid_hgt(passport):
	value = get_field_value(passport,"hgt")
	if value[-2:] =="in":
		height = int(value[0:-2])
		if height >= 59 and height <= 76 :
			return True
	elif value[-2:] == "cm":
		height = int(value[0:-2])
		if height >=150 and height <= 193:
			return True
	return False

#check if hcl is valid
def valid_hcl(passport):
	value = get_field_value(passport,'hcl')
	valid_char = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
	if len(value)==7 and value[0]=='#':
		for char in value[1:]:
			if char not in valid_char :
				return False
	else :
		return False
	return True

#check if ecl is valid 
def valid_ecl(passport):
	value = get_field_value(passport,"ecl")
	valid_color = ["amb","blu","brn","gry","grn","hzl","oth"]
	if value in valid_color:
		return True
	return False

#check if pid is valid 
def valid_pid(passport):
	value = get_field_value(passport,'pid')
	if len(value)==9 and value.isnumeric():
		return True
	return False

#main validator function which call all the sub validators
def validator(passport,field):
	if field =="byr":
		return valid_byr(passport)
	elif field =="iyr":
		return valid_iyr(passport)
	elif field =="eyr":
		return valid_eyr(passport)
	elif field =="hgt":
		return valid_hgt(passport)
	elif field =="hcl":
		return valid_hcl(passport)
	elif field =="ecl":
		return valid_ecl(passport)
	elif field =="pid":
		return valid_pid(passport)
	return False 


print("Solution for the part 2 : ",day_4(get_clean_passport(raw_passport),v= False)) #213

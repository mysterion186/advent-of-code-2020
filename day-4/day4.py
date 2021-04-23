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

#function to test if all the field
def day_4 (clean_passport):
	field_list = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
	count = 0
	field_count = 0
	for passport in clean_passport :
		#check all the field in the passport
		for field in field_list :
			if check_field (passport,field):
				field_count+=1 #get the number of present fields in the passport
		#if field_count == 7 means that all the fiels are in the passport
		if field_count == 7 :
			count+=1
		#reset of the field_count
		field_count = 0
	return count

def check_field(passport,field):
	if field in passport:
		return True
	return False

print("Solution for the part 1 : ",day_4(get_clean_passport(raw_passport))) #213
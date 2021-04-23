f = open("day2.txt")
lines = f.readlines()
f.close()

#will return a list containing all the password policy info
def get_password_info(password):
	password_info = [] #will contain the lowest,highest and the charactere that respect the company policy
	n_low = password[0:password.index("-")]
	n_high = password[password.index("-")+1:password.index(" ")] #index return the first index that match the value
	char = password[password.index(' ')+1:password.index(":")]
	return [n_low,n_high,char]

#print(test[test.index(" ",test.index(":"))+1:])

#check if a given password verify the company policy
def count_char(password):
	count = 0
	values = get_password_info(password)
	for char in password[password.index(" ",password.index(":"))+1:]:
		if char == values[2]:
			count+=1
	if count <= int(values[1]) and count >= int(values[0]):
		return True
	return False

def day_2(password_list,v):
	count = 0
	for raw_password in password_list:
		password = raw_password.split('\n')[0]
		if v == 1 :
			if count_char(password):
				count +=1
		else :
			if count_char_v2(password):
				count +=1
	return count

print("Solution part 1 day 2 : ",day_2(lines,1)) #620

#check the new company policy
def count_char_v2(password):
	values = get_password_info(password)
	#get the password 
	clean_password = password[password.index(" ",password.index(":"))+1:]
	#use variable to have a more readable code
	n_low = int(values[0])-1
	n_high = int(values[1])-1
	#check that the the characteres are different 
	if clean_password[n_low] == clean_password[n_high]:
		return False 
	#check if of the number respect the criteria
	else :
		if clean_password[n_low] == values[2]:
			return True 
		elif clean_password[n_high]==values[2]:
			return True 
	return False 


print("Solution part 2 day 2 : ",day_2(lines,2)) #727

test = "17-19 p: pwpzpfbrcaaaaaaaaaaa"
# count_char_v2(test)
#test = "1-3 b: cdefg"
print(count_char_v2(test))
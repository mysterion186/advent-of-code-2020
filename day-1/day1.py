with open("day1.txt","r") as f :
	a = f.readlines()

#convert the entry into a workable list
def get_clean_value(a):
	clean = []
	for num in a :
		clean.append(int(num.split("\n")[0]))
	return clean


b = get_clean_value(a)


#function to answer to the first part 
def day_1(L):
	for i in range (0,len(L)):
		for j in range (i+1,len(L)):
			if L[i] + L[j] == 2020 : 
				print (L[i])
				print(L[j])
				return L[i]*L[j]
	print("pas de nb")

day1=day_1(b)
print("Solution for the first part : ",day1) #786811

#fucntion to answer to the second part
def day_1_v2(L):
	for i in range (0,len(L)):
		for j in range (i+1,len(L)):
			for k in range (j+1,len(L)):
				if int(L[i])+int(L[j])+int(L[k]) == 2020 :
					print((L[i]))
					print((L[j]))
					print((L[k]))
					return (L[i])*(L[k])*(L[j])
	print ("pas de nb")



d = day_1_v2(b)
print("Solution for the second part :  ", d) #199068980
